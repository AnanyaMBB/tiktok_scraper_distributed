"""
TikTok Profile Scraper v4 - Browser-Based API Fetching

The X-Bogus and X-Gnarly parameters are cryptographic signatures tied to 
the exact request parameters. Changing cursor/count invalidates them.

This version uses the browser to intercept API responses directly,
ensuring all signatures remain valid.
"""

import json
import time
import os
import sys
import random
import re
from typing import Optional, Dict, Any, List, Callable
from pathlib import Path

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
        """Smooth scroll like a human"""
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


class TikTokBrowserScraper:
    """
    TikTok Scraper that uses browser for all API calls.
    
    This ensures X-Bogus/X-Gnarly signatures are always valid since
    the browser generates them naturally.
    """
    
    DEFAULT_USER_DATA_DIR = os.path.join(os.path.expanduser("~"), ".tiktok_scraper_profile")
    
    def __init__(
        self,
        output_dir: str = "tiktok_videos",
        user_data_dir: Optional[str] = None,
        headless: bool = False,
        proxy_config: Optional[Dict] = None
    ):
        self.output_dir = output_dir
        self.user_data_dir = user_data_dir or self.DEFAULT_USER_DATA_DIR
        self.headless = headless
        self.proxy_config = proxy_config
        
        self._playwright = None
        self._context: Optional[BrowserContext] = None
        self._page: Optional[Page] = None
        
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
    
    def start_browser(self):
        """Start browser session"""
        if self._context is not None:
            return
        
        print("Starting browser...")
        self._playwright = sync_playwright().start()
        
        context_options = {
            "viewport": {"width": 1920, "height": 1080},
            "locale": "en-US",
            "timezone_id": "America/New_York",
        }
        
        if self.proxy_config:
            context_options["proxy"] = self.proxy_config
        
        if USING_PATCHRIGHT:
            self._context = self._playwright.chromium.launch_persistent_context(
                user_data_dir=self.user_data_dir,
                channel="chrome",
                headless=self.headless,
                args=self._get_browser_args(),
                **context_options
            )
        else:
            browser = self._playwright.chromium.launch(
                headless=self.headless,
                channel="chrome",
                args=self._get_browser_args()
            )
            self._context = browser.new_context(**context_options)
        
        self._page = self._context.new_page()
        print("✓ Browser started")
    
    def close_browser(self):
        """Close browser session"""
        if self._context:
            self._context.close()
            self._context = None
            self._page = None
        if self._playwright:
            self._playwright.stop()
            self._playwright = None
        print("Browser closed")
    
    def get_user_sec_uid(self, username: str) -> Optional[str]:
        """Get secUid from user profile page using curl_cffi"""
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
    
    def fetch_user_videos_via_browser(
        self,
        username: str,
        max_videos: int = 100,
        timeout_per_scroll: int = 5
    ) -> List[Dict[str, Any]]:
        """
        Fetch videos by scrolling the profile page and intercepting API responses.
        
        This method:
        1. Navigates to the user's profile
        2. Scrolls to trigger API calls
        3. Intercepts the API responses with valid signatures
        4. Collects all video data
        """
        self.start_browser()
        
        all_videos = []
        seen_video_ids = set()
        
        # Set up response interception
        api_responses = []
        
        def handle_response(response):
            if 'api/post/item_list/' in response.url:
                try:
                    data = response.json()
                    if 'itemList' in data and data['itemList']:
                        api_responses.append(data)
                        print(f"   ✓ Intercepted API response with {len(data['itemList'])} videos")
                except Exception as e:
                    pass
        
        self._page.on('response', handle_response)
        
        try:
            print(f"\n{'='*70}")
            print(f"Fetching videos for @{username}")
            print(f"{'='*70}")
            
            # Navigate to profile
            print(f"Navigating to @{username}...")
            self._page.goto(
                f'https://www.tiktok.com/@{username}',
                wait_until='domcontentloaded',
                timeout=60000
            )
            
            # Wait for initial load
            HumanBehavior.random_delay(3000, 5000)
            
            # Check for challenge
            if self._check_for_challenge():
                print("⚠ Challenge detected - waiting 30s for manual resolution...")
                time.sleep(30)
            
            # Scroll and collect videos
            scroll_count = 0
            max_scrolls = 50
            no_new_videos_count = 0
            
            while len(all_videos) < max_videos and scroll_count < max_scrolls:
                # Process any new API responses
                while api_responses:
                    data = api_responses.pop(0)
                    for video in data.get('itemList', []):
                        video_id = video.get('id')
                        if video_id and video_id not in seen_video_ids:
                            seen_video_ids.add(video_id)
                            all_videos.append(video)
                
                prev_count = len(all_videos)
                
                # Scroll down
                HumanBehavior.random_mouse_movement(self._page)
                scroll_distance = random.randint(400, 800)
                HumanBehavior.smooth_scroll(self._page, scroll_distance)
                
                # Wait for potential API response
                HumanBehavior.random_delay(1500, 3000)
                
                scroll_count += 1
                print(f"   Scroll {scroll_count}/{max_scrolls} - Total videos: {len(all_videos)}")
                
                # Check if we got new videos
                if len(all_videos) == prev_count:
                    no_new_videos_count += 1
                    if no_new_videos_count >= 5:
                        print("   No new videos after 5 scrolls - reached end or rate limited")
                        break
                else:
                    no_new_videos_count = 0
                
                # Occasional longer pause
                if random.random() > 0.8:
                    HumanBehavior.random_delay(2000, 4000)
            
            # Process any remaining responses
            while api_responses:
                data = api_responses.pop(0)
                for video in data.get('itemList', []):
                    video_id = video.get('id')
                    if video_id and video_id not in seen_video_ids:
                        seen_video_ids.add(video_id)
                        all_videos.append(video)
            
            print(f"\n✓ Collected {len(all_videos)} unique videos")
            return all_videos
            
        except Exception as e:
            print(f"✗ Error: {e}")
            import traceback
            traceback.print_exc()
            return all_videos
    
    def fetch_videos_with_cursor(
        self,
        username: str,
        sec_uid: str,
        cursor: int = 0,
        count: int = 30
    ) -> Optional[Dict[str, Any]]:
        """
        Fetch videos for a specific cursor by injecting JavaScript to make the API call.
        
        The browser will generate valid X-Bogus/X-Gnarly signatures.
        """
        self.start_browser()
        
        try:
            # First navigate to the profile to establish session
            current_url = self._page.url
            if username not in current_url:
                print(f"Navigating to @{username}...")
                self._page.goto(
                    f'https://www.tiktok.com/@{username}',
                    wait_until='domcontentloaded',
                    timeout=60000
                )
                HumanBehavior.random_delay(3000, 5000)
            
            print(f"📡 Fetching @{username} (cursor={cursor}, count={count})...")
            
            # Use the browser's fetch to make the API call
            # TikTok's JS will add the correct X-Bogus/X-Gnarly
            result = self._page.evaluate(f"""
                async () => {{
                    const params = new URLSearchParams({{
                        'secUid': '{sec_uid}',
                        'cursor': '{cursor}',
                        'count': '{count}',
                        'aid': '1988',
                        'app_language': 'en',
                        'app_name': 'tiktok_web',
                        'browser_language': navigator.language,
                        'browser_name': 'Mozilla',
                        'browser_online': navigator.onLine,
                        'browser_platform': navigator.platform,
                        'browser_version': navigator.userAgent.split(' ').pop(),
                        'channel': 'tiktok_web',
                        'cookie_enabled': navigator.cookieEnabled,
                        'device_platform': 'web_pc',
                        'focus_state': true,
                        'from_page': 'user',
                        'is_fullscreen': false,
                        'is_page_visible': true,
                        'os': 'windows',
                        'region': 'US',
                        'screen_height': screen.height,
                        'screen_width': screen.width,
                        'tz_name': Intl.DateTimeFormat().resolvedOptions().timeZone,
                        'webcast_language': 'en'
                    }});
                    
                    try {{
                        const response = await fetch(
                            '/api/post/item_list/?' + params.toString(),
                            {{
                                method: 'GET',
                                credentials: 'include',
                                headers: {{
                                    'Accept': 'application/json'
                                }}
                            }}
                        );
                        
                        if (!response.ok) {{
                            return {{ error: 'HTTP ' + response.status }};
                        }}
                        
                        return await response.json();
                    }} catch (e) {{
                        return {{ error: e.toString() }};
                    }}
                }}
            """)
            
            if result and 'error' in result:
                print(f"   ✗ {result['error']}")
                return None
            
            if result and 'itemList' in result:
                print(f"   ✓ Got {len(result['itemList'])} videos")
                return result
            else:
                print(f"   ⊗ No videos in response")
                # Print response for debugging
                print(f"   Response keys: {list(result.keys()) if result else 'None'}")
                return result
                
        except Exception as e:
            print(f"   ✗ Error: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def _check_for_challenge(self) -> bool:
        """Check if we're on a challenge/captcha page"""
        try:
            challenge_selectors = [
                '[class*="captcha"]',
                '[id*="captcha"]',
                '[class*="challenge"]',
                '.verify-wrap',
            ]
            for selector in challenge_selectors:
                if self._page.query_selector(selector):
                    return True
            return False
        except Exception:
            return False
    
    def save_videos(self, videos: List[Dict], filename: str = "videos.json"):
        """Save video data to JSON file"""
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(videos, f, indent=2, ensure_ascii=False)
        print(f"✓ Saved {len(videos)} videos to {filepath}")
    
    def __enter__(self):
        self.start_browser()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_browser()


def main():
    username = "nike"
    
    # Method 1: Scroll-based collection (most reliable)
    print("\n" + "="*70)
    print("METHOD 1: Scroll-based video collection")
    print("="*70)
    
    with TikTokBrowserScraper(headless=False) as scraper:
        videos = scraper.fetch_user_videos_via_browser(
            username=username,
            max_videos=50  # Collect up to 50 videos
        )
        
        if videos:
            scraper.save_videos(videos, f"{username}_videos.json")
            
            print(f"\n{'='*70}")
            print(f"Sample videos:")
            print(f"{'='*70}")
            for i, video in enumerate(videos[:5]):
                desc = video.get('desc', 'No description')[:60]
                plays = video.get('stats', {}).get('playCount', 0)
                print(f"  {i+1}. {desc}...")
                print(f"      Plays: {plays:,}")
    
    # Method 2: Cursor-based fetching (for specific pagination)
    print("\n" + "="*70)
    print("METHOD 2: Cursor-based API fetch")
    print("="*70)
    
    with TikTokBrowserScraper(headless=False) as scraper:
        sec_uid = scraper.get_user_sec_uid(username)
        
        if sec_uid:
            # Fetch first page
            result = scraper.fetch_videos_with_cursor(
                username=username,
                sec_uid=sec_uid,
                cursor=0,
                count=30
            )
            
            if result and 'itemList' in result:
                print(f"\nGot {len(result['itemList'])} videos")
                
                # Get next cursor for pagination
                has_more = result.get('hasMore', False)
                next_cursor = result.get('cursor', 0)
                print(f"Has more: {has_more}, Next cursor: {next_cursor}")


if __name__ == "__main__":
    main()