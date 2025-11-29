import redis
import json
import time
import os
import sys
from typing import Optional, Dict, Any, List
from urllib.parse import urlparse, parse_qsl, quote
from pathlib import Path
from dotenv import load_dotenv
from celery import Celery
from playwright.sync_api import sync_playwright
from curl_cffi import requests
from collections import OrderedDict
from playwright_stealth.stealth import Stealth 

# Load .env from parent directory
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

sys.path.append(str(Path(__file__).parent.parent / 'shared'))
from storage import upload_file
from proxy import ProxyManager

# Initialize Celery
celery_app = Celery(
    'tiktok_scraper',
    broker=f"redis://{os.getenv('REDIS_HOST', 'localhost')}:{os.getenv('REDIS_PORT', 6379)}/0"
)



class TikTokProfileScraper: 
    def __init__(self, output_dir="tiktok_videos", session_file="profile_session.json"):
        self.output_dir = output_dir
        self.session_file = session_file
        self.proxy_manager = ProxyManager()
        
        # Session data
        self.cookies = None
        self.headers = None
        self.api_params = {}
        self.api_params_items = None
        
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        

    def _setup_output_directory(self):
        os.makedirs(self.output_dir, exist_ok=True)        

    def get_fresh_session_data(self, min_requests: int = 5):
        print("=" * 70)
        print("Capturing TikTok FYP API request using Playwright...")
        print("=" * 70)

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                locale='en-US',
                timezone_id='America/New_York'
            )
            page = context.new_page()

            stealth = Stealth()
            stealth.apply_stealth_sync(page)
            captured_requests = []

            def handle_request(request):
                if 'api/post/item_list/' in request.url:
                    captured_requests.append({'url': request.url, 'headers': request.headers})
                    print(f"   ✓ Captured recommend/item_list request #{len(captured_requests)}")

            page.on('request', handle_request)

            try:
                page.goto('https://www.tiktok.com/@nike', wait_until='domcontentloaded', timeout=60000)
                time.sleep(3)

                scrolls = 0
                while len(captured_requests) < min_requests and scrolls < 10:
                    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                    scrolls += 1
                    time.sleep(2)

                if not captured_requests:
                    print("✗ No API requests captured")
                    return False

                selected = captured_requests[-1]
                captured_url = selected['url']
                captured_headers = selected['headers']

                print("captured url: ", captured_url)
                print("captured headers: ", captured_headers)

                browser_cookies = context.cookies()
                self.cookies = {c['name']: c['value'] for c in browser_cookies}

                # preserve query param order exactly
                parsed = urlparse(captured_url)
                pairs = parse_qsl(parsed.query, keep_blank_values=True)
                self.api_params_items = list(pairs)
                self.api_params = OrderedDict()
                for k, v in pairs:
                    if k not in self.api_params:
                        self.api_params[k] = v

                self.headers = captured_headers
                print(f"✓ Captured {len(self.api_params)} parameters in original order")
                print(f"✓ Captured {len(self.headers)} headers")
                return True

            except Exception as e:
                print("✗ Error:", e)
                import traceback
                traceback.print_exc()
                return False
            finally:
                browser.close()

    def get_user_sec_uid(self, username: str) -> Optional[str]:
        """Get secUid from user profile page"""
        try:
            import re
            
            profile_url = f"https://www.tiktok.com/@{username}"
            
            response = requests.get(
                profile_url,
                impersonate="chrome131",
                timeout=30
            )
            
            if response.status_code != 200:
                print(f"✗ Failed to fetch profile: {response.status_code}")
                return None

            match = re.search(r'"secUid":"(MS4wLjABAAAA[^"]+)"', response.text)
            if match:
                sec_uid = match.group(1)
                print(f"✓ Found secUid for @{username}")
                return sec_uid

            print(f"✗ Could not find secUid for @{username}")
            return None

        except Exception as e:
            print(f"✗ Error getting secUid: {e}")
            return None
        
    def get_cookies(self) -> Dict[str, str]:
        if self.cookies is None:
            raise Exception("Cookies not initialized. Call get_fresh_session_data() first.")
        return self.cookies

    def get_headers(self) -> Dict[str, str]:
        if self.headers is None:
            raise Exception("Headers not initialized. Call get_fresh_session_data() first.")
        return self.headers
    
    def build_api_url(self, sec_uid: str, cursor: int = 0, count: int = 30) -> str:
        """
        Build TikTok API URL preserving byte identity:
        - Preserve captured WebIdLastTime
        - Preserve order
        - Do not re-encode or change signature params
        """
        base_url = "https://www.tiktok.com/api/post/item_list/"

        if not self.api_params_items:
            raise Exception("API parameters not initialized. Call get_fresh_session_data() first.")

        pairs = list(self.api_params_items)

        # update only safe fields (do not touch WebIdLastTime)
        def set_or_replace(pairs_list, key, value):
            for i, (k, _) in enumerate(pairs_list):
                if k == key:
                    pairs_list[i] = (key, str(value))
                    return
            pairs_list.append((key, str(value)))

        set_or_replace(pairs, "secUid", sec_uid)
        set_or_replace(pairs, "cursor", str(cursor))
        set_or_replace(pairs, "count", str(count))
        set_or_replace(pairs, "focus_state", "true")
        set_or_replace(pairs, "is_page_visible", "true")

        # deduplicate X-Bogus/X-Gnarly/msToken if any appear twice
        sig_keys = {"msToken", "X-Bogus", "X-Gnarly"}
        seen = {k: False for k in sig_keys}
        deduped = []
        for k, v in pairs:
            if k in sig_keys:
                if not seen[k]:
                    deduped.append((k, v))
                    seen[k] = True
            else:
                deduped.append((k, v))
        pairs = deduped

        # encode normally, but skip encoding '/' in signature keys
        def encode_pair(k, v):
            if k in ("msToken", "X-Bogus", "X-Gnarly"):
                return f"{quote(k, safe='')}={quote(v, safe='/=')}"
            return f"{quote(k, safe='')}={quote(v, safe='')}"

        query = "&".join(encode_pair(k, v) for k, v in pairs)
        return f"{base_url}?{query}"
    

    def fetch_user_videos(self, username: str, sec_uid: str, cursor: int = 0) -> Optional[Dict[str, Any]]:
        """Fetch videos from user profile"""

        if not self.get_fresh_session_data(min_requests=5):
            print("✗ Failed to capture session data.")
            return
        
        try:
            url = self.build_api_url(sec_uid, cursor)
            
            # Update referer header for this specific user
            headers = self.headers.copy()
            headers["referer"] = f"https://www.tiktok.com/@{username}"

            print(f"📡 Fetching @{username} (cursor={cursor})...")

            print(f"constructed url: {url}")
            print(f"headers: {headers}")
                  

            # Get proxy
            proxy_config = self.proxy_manager.get_proxy_config(ProxyManager.PROXY_TYPE_DATACENTER)

            response = requests.get(
                url,
                headers=headers,
                cookies=self.cookies,
                impersonate="chrome131",
                proxies=proxy_config,
                timeout=30
            )

            if response.status_code != 200:
                print(f"   ✗ Status {response.status_code}")
                return None

            data = response.json()
            
            if 'itemList' in data and data['itemList']:
                print(f"   ✓ Got {len(data['itemList'])} videos")
                return data
            else:
                print(f"   ⊗ No videos in response")
                return None

        except Exception as e:
            print(f"   ✗ Error: {e}")
            return None
    

    

if __name__ == "__main__":
    username = "nike"
    scraper = TikTokProfileScraper()

    sec_uid = scraper.get_user_sec_uid(username)

    scraper.fetch_user_videos(
        username, 
        sec_uid, 
        cursor = 0, 
    )

    