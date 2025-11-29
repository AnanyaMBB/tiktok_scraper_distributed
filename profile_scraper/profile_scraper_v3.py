"""
TikTok Profile Scraper v4 - Signature-Preserving Version

This version captures the exact API request and preserves ALL parameters
including count and cursor from the original capture. Only secUid is changed
for different users.

The X-Bogus/X-Gnarly signatures may be tied to specific parameter combinations,
so we preserve everything exactly as captured.
"""

import json
import time
import os
import sys
import random
import re
from typing import Optional, Dict, Any, List
from urllib.parse import urlparse, parse_qsl, quote, urlencode
from pathlib import Path
from collections import OrderedDict

try:
    from patchright.sync_api import sync_playwright, Page, BrowserContext
    USING_PATCHRIGHT = True
    print("✓ Using Patchright (undetected Playwright)")
except ImportError:
    from playwright.sync_api import sync_playwright, Page, BrowserContext
    USING_PATCHRIGHT = False
    print("⚠ Patchright not installed, using regular Playwright")

from curl_cffi import requests


class HumanBehavior:
    """Simulate human-like browser interactions"""
    
    @staticmethod
    def random_delay(min_ms: int = 500, max_ms: int = 2000):
        delay = random.randint(min_ms, max_ms) / 1000
        time.sleep(delay)
    
    @staticmethod
    def smooth_scroll(page: Page, distance: int = 500):
        page.evaluate(f"""
            window.scrollBy({{
                top: {distance},
                behavior: 'smooth'
            }});
        """)
    
    @staticmethod
    def random_mouse_movement(page: Page):
        try:
            viewport = page.viewport_size
            if viewport:
                x = random.randint(100, viewport['width'] - 100)
                y = random.randint(100, viewport['height'] - 100)
                page.mouse.move(x, y)
        except Exception:
            pass


class TikTokProfileScraper:
    """
    TikTok Profile Scraper with signature preservation.
    
    Captures API requests with their exact parameters and signatures,
    then replays them with minimal modifications.
    """
    
    DEFAULT_USER_DATA_DIR = os.path.join(os.path.expanduser("~"), ".tiktok_scraper_profile")
    
    def __init__(
        self,
        output_dir: str = "tiktok_videos",
        session_file: str = "profile_session.json",
        user_data_dir: Optional[str] = None,
        headless: bool = False,
        proxy_config: Optional[Dict] = None
    ):
        self.output_dir = output_dir
        self.session_file = session_file
        self.user_data_dir = user_data_dir or self.DEFAULT_USER_DATA_DIR
        self.headless = headless
        self.proxy_config = proxy_config
        
        # Session data - store the COMPLETE captured request
        self.cookies = None
        self.headers = None
        self.captured_url = None  # Store the full captured URL
        self.api_params_items = None  # Ordered list of (key, value) pairs
        
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(self.user_data_dir, exist_ok=True)
    
    def _get_browser_args(self) -> List[str]:
        args = [
            "--disable-blink-features=AutomationControlled",
            "--disable-dev-shm-usage",
            "--no-first-run",
            "--no-default-browser-check",
        ]
        if self.headless:
            args.append("--headless=new")
        return args
    
    def get_fresh_session_data(self, target_username: str = "nike", min_requests: int = 5) -> bool:
        """
        Capture TikTok API session data.
        Stores the COMPLETE URL with all parameters intact.
        """
        print("=" * 70)
        print("Capturing TikTok Profile API request...")
        print(f"Using: {'Patchright' if USING_PATCHRIGHT else 'Playwright'}")
        print("=" * 70)
        
        with sync_playwright() as p:
            context_options = {
                "viewport": {"width": 1920, "height": 1080},
                "locale": "en-US",
                "timezone_id": "America/New_York",
            }
            
            if self.proxy_config:
                context_options["proxy"] = self.proxy_config
            
            try:
                if USING_PATCHRIGHT:
                    context = p.chromium.launch_persistent_context(
                        user_data_dir=self.user_data_dir,
                        channel="chrome",
                        headless=self.headless,
                        args=self._get_browser_args(),
                        **context_options
                    )
                else:
                    browser = p.chromium.launch(
                        headless=self.headless,
                        channel="chrome",
                        args=self._get_browser_args()
                    )
                    context = browser.new_context(**context_options)
                
                page = context.new_page()
                captured_requests = []
                
                def handle_request(request):
                    if 'api/post/item_list/' in request.url:
                        captured_requests.append({
                            'url': request.url,
                            'headers': dict(request.headers)
                        })
                        print(f"   ✓ Captured item_list request #{len(captured_requests)}")
                
                page.on('request', handle_request)
                
                print(f"Navigating to @{target_username}...")
                
                # Sometimes visit homepage first
                if random.random() > 0.5:
                    print("   → Visiting homepage first...")
                    page.goto('https://www.tiktok.com/', wait_until='domcontentloaded', timeout=60000)
                    HumanBehavior.random_delay(2000, 4000)
                
                page.goto(
                    f'https://www.tiktok.com/@{target_username}',
                    wait_until='domcontentloaded',
                    timeout=60000
                )
                
                HumanBehavior.random_delay(3000, 5000)
                
                # Scroll to trigger API calls
                scrolls = 0
                max_scrolls = 15
                
                while len(captured_requests) < min_requests and scrolls < max_scrolls:
                    HumanBehavior.random_mouse_movement(page)
                    scroll_distance = random.randint(400, 800)
                    HumanBehavior.smooth_scroll(page, scroll_distance)
                    scrolls += 1
                    HumanBehavior.random_delay(1500, 3000)
                    print(f"   → Scroll {scrolls}/{max_scrolls}, captured: {len(captured_requests)}")
                
                if not captured_requests:
                    print("✗ No API requests captured")
                    debug_screenshot = os.path.join(self.output_dir, "debug_screenshot.png")
                    page.screenshot(path=debug_screenshot)
                    print(f"   → Saved debug screenshot: {debug_screenshot}")
                    return False
                
                # Use the FIRST request (cursor=0) if available, otherwise last
                # First request typically has cursor=0
                selected = captured_requests[0]
                self.captured_url = selected['url']
                self.headers = selected['headers']
                
                print(f"\n✓ Successfully captured {len(captured_requests)} requests")
                print(f"   Using request #1 (first captured)")
                
                # Parse and store parameters in order
                parsed = urlparse(self.captured_url)
                self.api_params_items = parse_qsl(parsed.query, keep_blank_values=True)
                
                # Extract cookies
                browser_cookies = context.cookies()
                self.cookies = {c['name']: c['value'] for c in browser_cookies}
                
                print(f"✓ Captured URL with {len(self.api_params_items)} parameters")
                print(f"✓ Captured {len(self.headers)} headers")
                print(f"✓ Captured {len(self.cookies)} cookies")
                
                # Print key params for debugging
                params_dict = dict(self.api_params_items)
                print(f"\n   Key parameters:")
                print(f"   - cursor: {params_dict.get('cursor', 'N/A')}")
                print(f"   - count: {params_dict.get('count', 'N/A')}")
                print(f"   - secUid: {params_dict.get('secUid', 'N/A')[:30]}...")
                
                self._save_session()
                return True
                
            except Exception as e:
                print(f"✗ Error: {e}")
                import traceback
                traceback.print_exc()
                return False
            
            finally:
                if USING_PATCHRIGHT:
                    context.close()
                else:
                    browser.close()
    
    def _save_session(self):
        """Save session data for reuse"""
        session_path = os.path.join(self.output_dir, self.session_file)
        session_data = {
            'captured_url': self.captured_url,
            'headers': self.headers,
            'cookies': self.cookies,
            'api_params_items': self.api_params_items,
            'timestamp': time.time()
        }
        
        with open(session_path, 'w') as f:
            json.dump(session_data, f, indent=2)
        print(f"✓ Session saved to {session_path}")
    
    def _load_session(self) -> bool:
        """Load session data if available and fresh"""
        session_path = os.path.join(self.output_dir, self.session_file)
        
        if not os.path.exists(session_path):
            return False
        
        try:
            with open(session_path, 'r') as f:
                session_data = json.load(f)
            
            # Check if session is too old (> 30 minutes for safety)
            if time.time() - session_data.get('timestamp', 0) > 1800:
                print("⚠ Session expired (>30 min), need fresh capture")
                return False
            
            self.captured_url = session_data['captured_url']
            self.headers = session_data['headers']
            self.cookies = session_data['cookies']
            self.api_params_items = session_data['api_params_items']
            
            print("✓ Loaded existing session")
            return True
        except Exception as e:
            print(f"⚠ Failed to load session: {e}")
            return False
    
    def get_user_sec_uid(self, username: str) -> Optional[str]:
        """Get secUid from user profile page"""
        try:
            profile_url = f"https://www.tiktok.com/@{username}"
            response = requests.get(profile_url, impersonate="chrome131", timeout=30)
            
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
    
    def build_api_url_exact(self, sec_uid: Optional[str] = None) -> str:
        """
        Build API URL preserving EVERYTHING exactly as captured.
        
        Only secUid is optionally changed. All other params including
        cursor, count, signatures stay exactly the same.
        """
        base_url = "https://www.tiktok.com/api/post/item_list/"
        
        if not self.api_params_items:
            raise Exception("API parameters not initialized. Call get_fresh_session_data() first.")
        
        # Start with exact copy of captured parameters
        pairs = list(self.api_params_items)
        
        # Only update secUid if provided
        if sec_uid is not None:
            for i, (k, v) in enumerate(pairs):
                if k == "secUid":
                    pairs[i] = ("secUid", sec_uid)
                    break
        
        # Deduplicate signature keys (keep first occurrence)
        sig_keys = {"msToken", "X-Bogus", "X-Gnarly"}
        seen = set()
        deduped = []
        for k, v in pairs:
            if k in sig_keys:
                if k not in seen:
                    deduped.append((k, v))
                    seen.add(k)
            else:
                deduped.append((k, v))
        pairs = deduped
        
        # Encode preserving special chars in signature values
        def encode_pair(k, v):
            if k in ("msToken", "X-Bogus", "X-Gnarly"):
                return f"{quote(k, safe='')}={quote(v, safe='/=+')}"
            return f"{quote(k, safe='')}={quote(v, safe='')}"
        
        query = "&".join(encode_pair(k, v) for k, v in pairs)
        return f"{base_url}?{query}"
    
    def fetch_user_videos(
        self,
        username: str,
        sec_uid: str,
        use_cached_session: bool = True,
        proxy_config: Optional[Dict] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Fetch videos from user profile.
        
        Preserves ALL parameters exactly as captured, only changes secUid.
        """
        
        # Load or capture session
        if use_cached_session and self._load_session():
            pass
        else:
            if not self.get_fresh_session_data(target_username=username, min_requests=5):
                print("✗ Failed to capture session data.")
                return None
        
        try:
            # Build URL - ONLY secUid changes, everything else exact
            url = self.build_api_url_exact(sec_uid=sec_uid)
            
            # Use captured headers exactly, only update referer
            headers = dict(self.headers)
            headers["referer"] = f"https://www.tiktok.com/@{username}"
            
            # Log what we're doing
            params_dict = dict(self.api_params_items)
            
            print(f"\n📡 Fetching @{username}")
            print(f"   Using captured cursor={params_dict.get('cursor', '?')}, count={params_dict.get('count', '?')}")
            
            # Debug: compare URLs
            print(f"\n   URL comparison:")
            print(f"   Captured: ...{self.captured_url[-100:]}")
            print(f"   Built:    ...{url[-100:]}")
            
            # Make request
            response = requests.get(
                url,
                headers=headers,
                cookies=self.cookies,
                impersonate="chrome131",
                proxies=proxy_config,
                timeout=30
            )
            
            print(f"\n   Status: {response.status_code}")
            print(f"   Content-Type: {response.headers.get('content-type', 'N/A')}")
            
            if response.status_code != 200:
                print(f"   ✗ HTTP Error")
                print(f"   Response: {response.text[:500]}")
                return None
            
            # Check content type
            content_type = response.headers.get('content-type', '')
            if 'json' not in content_type.lower():
                print(f"   ✗ Non-JSON response")
                print(f"   Response: {response.text[:500]}")
                return None
            
            data = response.json()
            
            if 'itemList' in data and data['itemList']:
                print(f"   ✓ Got {len(data['itemList'])} videos")
                return data
            else:
                print(f"   ⊗ No videos in response")
                print(f"   Response keys: {list(data.keys())}")
                if 'statusCode' in data:
                    print(f"   Status code: {data['statusCode']}")
                if 'statusMsg' in data:
                    print(f"   Status msg: {data['statusMsg']}")
                return data
                
        except json.JSONDecodeError as e:
            print(f"   ✗ JSON decode error: {e}")
            print(f"   Raw response: {response.text[:500]}")
            return None
        except Exception as e:
            print(f"   ✗ Error: {e}")
            import traceback
            traceback.print_exc()
            return None


def main():
    username = "nike"
    
    scraper = TikTokProfileScraper(
        output_dir="tiktok_videos",
        headless=False,
    )
    
    # Get secUid
    sec_uid = scraper.get_user_sec_uid(username)
    if not sec_uid:
        print("Failed to get secUid")
        return
    
    # Fetch videos - uses EXACT captured parameters, only changes secUid
    result = scraper.fetch_user_videos(
        username=username,
        sec_uid=sec_uid,
        use_cached_session=False,  # Force fresh capture
    )
    
    if result and 'itemList' in result:
        print(f"\n{'='*70}")
        print(f"SUCCESS! Got {len(result['itemList'])} videos")
        print(f"{'='*70}")
        
        for i, video in enumerate(result['itemList'][:5]):
            desc = video.get('desc', 'No description')[:50]
            print(f"  {i+1}. {desc}...")
        
        # Save results
        output_file = os.path.join(scraper.output_dir, f"{username}_videos.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"\n✓ Saved to {output_file}")


if __name__ == "__main__":
    main()