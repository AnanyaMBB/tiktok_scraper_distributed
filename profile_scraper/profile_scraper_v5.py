"""
TikTok Profile Scraper v5 - Scroll-Based Interception

Since X-Bogus/X-Gnarly signatures are tied to ALL parameters including cursor,
changing cursor invalidates the signature.

This version uses scroll-based interception:
1. Opens the browser and scrolls the profile page
2. Intercepts API RESPONSES (not requests) which contain valid data
3. Saves each video individually as it's collected
4. Continues scrolling until all videos are collected

This guarantees valid signatures since the browser generates them.
"""

import json
import time
import os
import sys
import asyncio
import random
import re
from typing import Optional, Dict, Any, List, Set
from pathlib import Path

# Fix for Windows asyncio subprocess issue with Playwright/Patchright
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

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
    TikTok Profile Scraper using scroll-based API response interception.
    
    This approach lets the browser handle all signature generation naturally.
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
        
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(self.user_data_dir, exist_ok=True)
    
    def _get_browser_args(self) -> List[str]:
        args = [
            "--disable-blink-features=AutomationControlled",
            "--disable-dev-shm-usage",
            "--no-first-run",
            "--no-default-browser-check",
            
            # Additional anti-detection for headless
            "--disable-background-timer-throttling",
            "--disable-backgrounding-occluded-windows",
            "--disable-renderer-backgrounding",
            "--disable-features=IsolateOrigins,site-per-process",
            "--disable-web-security",
            "--disable-features=TranslateUI",
            
            # Fake window/screen properties
            "--window-size=1920,1080",
            "--start-maximized",
            
            # GPU and rendering (helps with fingerprinting)
            "--enable-webgl",
            "--enable-features=NetworkService,NetworkServiceInProcess",
            "--ignore-certificate-errors",
        ]
        
        if self.headless:
            # Use new headless mode which is less detectable
            args.append("--headless=new")
            
            # Additional args to make headless look more like headed
            args.extend([
                "--disable-gpu",  # Sometimes helps in headless
                "--hide-scrollbars",
                "--mute-audio",
            ])
        
        return args
    
    def _get_user_video_dir(self, username: str) -> str:
        """Get directory for storing user's video metadata"""
        video_dir = os.path.join(self.output_dir, "tiktok_video_metadata", username)
        os.makedirs(video_dir, exist_ok=True)
        return video_dir
    
    def save_video_metadata(self, username: str, video: Dict[str, Any]) -> Optional[str]:
        """Save individual video metadata to its own file."""
        video_id = video.get('id')
        if not video_id:
            return None
        
        video_dir = self._get_user_video_dir(username)
        filepath = os.path.join(video_dir, f"{video_id}.json")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(video, f, indent=2, ensure_ascii=False)
        
        return filepath
    
    def is_video_already_saved(self, username: str, video_id: str) -> bool:
        """Check if a video has already been saved"""
        video_dir = self._get_user_video_dir(username)
        filepath = os.path.join(video_dir, f"{video_id}.json")
        return os.path.exists(filepath)
    
    def get_saved_video_ids(self, username: str) -> Set[str]:
        """Get set of already saved video IDs"""
        video_dir = self._get_user_video_dir(username)
        if not os.path.exists(video_dir):
            return set()
        
        video_ids = set()
        for filename in os.listdir(video_dir):
            if filename.endswith('.json'):
                video_ids.add(filename[:-5])  # Remove .json extension
        return video_ids
    
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
    
    def fetch_all_videos(
        self,
        username: str,
        max_videos: Optional[int] = None,
        skip_existing: bool = True,
        max_no_new_scrolls: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Fetch all videos by scrolling the profile and intercepting API responses.
        
        Args:
            username: TikTok username
            max_videos: Maximum videos to fetch (None = all)
            skip_existing: Skip videos already saved to disk
            max_no_new_scrolls: Stop after this many scrolls with no new videos
        
        Returns:
            List of all fetched video metadata
        """
        print(f"\n{'='*70}")
        print(f"Starting scroll-based scrape for @{username}")
        if max_videos:
            print(f"Max videos: {max_videos}")
        print(f"Skip existing: {skip_existing}")
        print(f"{'='*70}")
        
        # Get already saved video IDs
        existing_ids = self.get_saved_video_ids(username) if skip_existing else set()
        if existing_ids:
            print(f"Found {len(existing_ids)} existing videos on disk")
        
        all_videos = []
        seen_video_ids: Set[str] = set()
        saved_count = 0
        skipped_count = 0
        
        # API response buffer
        api_responses: List[Dict] = []
        
        with sync_playwright() as p:
            context_options = {
                "viewport": {"width": 1920, "height": 1080},
                "locale": "en-US",
                "timezone_id": "America/New_York",
            }
            
            # Handle proxy configuration
            proxy_to_use = None
            if self.proxy_config:
                proxy_to_use = self.proxy_config
                print(f"   Using proxy: {proxy_to_use.get('server', 'N/A')}")
            
            try:
                if USING_PATCHRIGHT:
                    # When using proxy, use a unique user_data_dir to avoid conflicts
                    # with cached proxy settings from previous sessions
                    import tempfile
                    if proxy_to_use:
                        # Create a temporary directory for this session
                        temp_user_data = tempfile.mkdtemp(prefix="tiktok_scraper_")
                        print(f"   Using temp profile: {temp_user_data}")
                    else:
                        temp_user_data = self.user_data_dir
                    
                    launch_kwargs = {
                        "user_data_dir": temp_user_data,
                        "channel": "chrome",
                        "headless": self.headless,
                        "args": self._get_browser_args(),
                        **context_options
                    }
                    
                    # Add proxy separately if configured
                    if proxy_to_use:
                        launch_kwargs["proxy"] = proxy_to_use
                    
                    context = p.chromium.launch_persistent_context(**launch_kwargs)
                else:
                    browser = p.chromium.launch(
                        headless=self.headless,
                        channel="chrome",
                        args=self._get_browser_args()
                    )
                    context = browser.new_context(**context_options)
                
                page = context.new_page()
                
                # Inject anti-detection scripts for headless mode
                if self.headless:
                    page.add_init_script("""
                        // Override webdriver property
                        Object.defineProperty(navigator, 'webdriver', {
                            get: () => undefined
                        });
                        
                        // Override plugins
                        Object.defineProperty(navigator, 'plugins', {
                            get: () => [
                                { name: 'Chrome PDF Plugin', filename: 'internal-pdf-viewer' },
                                { name: 'Chrome PDF Viewer', filename: 'mhjfbmdgcfjbbpaeojofohoefgiehjai' },
                                { name: 'Native Client', filename: 'internal-nacl-plugin' }
                            ]
                        });
                        
                        // Override languages
                        Object.defineProperty(navigator, 'languages', {
                            get: () => ['en-US', 'en']
                        });
                        
                        // Override permissions
                        const originalQuery = window.navigator.permissions.query;
                        window.navigator.permissions.query = (parameters) => (
                            parameters.name === 'notifications' ?
                                Promise.resolve({ state: Notification.permission }) :
                                originalQuery(parameters)
                        );
                        
                        // Override chrome property
                        window.chrome = {
                            runtime: {},
                            loadTimes: function() {},
                            csi: function() {},
                            app: {}
                        };
                        
                        // Fix for headless detection via window.outerWidth/outerHeight
                        Object.defineProperty(window, 'outerWidth', { get: () => window.innerWidth });
                        Object.defineProperty(window, 'outerHeight', { get: () => window.innerHeight });
                    """)
                
                # Set up RESPONSE interception (not request)
                def handle_response(response):
                    if 'api/post/item_list/' in response.url:
                        try:
                            data = response.json()
                            if data and 'itemList' in data:
                                api_responses.append(data)
                                print(f"   ✓ Intercepted response with {len(data.get('itemList', []))} videos")
                        except Exception:
                            pass
                
                page.on('response', handle_response)
                
                # Navigate to profile
                print(f"\nNavigating to @{username}...")
                
                # Sometimes visit homepage first
                if random.random() > 0.5:
                    print("   → Visiting homepage first...")
                    page.goto('https://www.tiktok.com/', wait_until='domcontentloaded', timeout=60000)
                    HumanBehavior.random_delay(2000, 4000)
                
                page.goto(
                    f'https://www.tiktok.com/@{username}',
                    wait_until='domcontentloaded',
                    timeout=60000
                )
                
                # Wait for initial load
                HumanBehavior.random_delay(3000, 5000)
                
                # Check for challenge
                if self._check_for_challenge(page):
                    print("⚠ Challenge detected - waiting 30s for manual resolution...")
                    time.sleep(30)
                
                # Scroll and collect videos
                scroll_count = 0
                no_new_videos_count = 0
                max_scrolls = 200  # Safety limit
                
                print(f"\nScrolling to collect videos...")
                
                while scroll_count < max_scrolls:
                    prev_total = len(all_videos)
                    
                    # Process any new API responses
                    while api_responses:
                        data = api_responses.pop(0)
                        for video in data.get('itemList', []):
                            video_id = video.get('id')
                            if not video_id:
                                continue
                            
                            # Skip if already seen in this session
                            if video_id in seen_video_ids:
                                continue
                            seen_video_ids.add(video_id)
                            
                            # Skip if already saved to disk
                            if skip_existing and video_id in existing_ids:
                                skipped_count += 1
                                continue
                            
                            # Save video
                            filepath = self.save_video_metadata(username, video)
                            if filepath:
                                saved_count += 1
                                all_videos.append(video)
                            
                            # Check max limit
                            if max_videos and len(all_videos) >= max_videos:
                                print(f"\n   Reached max_videos limit ({max_videos})")
                                break
                        
                        if max_videos and len(all_videos) >= max_videos:
                            break
                    
                    # Check if we've hit the limit
                    if max_videos and len(all_videos) >= max_videos:
                        break
                    
                    # Scroll
                    HumanBehavior.random_mouse_movement(page)
                    scroll_distance = random.randint(600, 1000)
                    HumanBehavior.smooth_scroll(page, scroll_distance)
                    scroll_count += 1
                    
                    # Wait for potential API response
                    HumanBehavior.random_delay(1500, 2500)
                    
                    # Check if we got new videos
                    new_videos = len(all_videos) - prev_total
                    
                    # Print progress every few scrolls
                    if scroll_count % 5 == 0 or new_videos > 0:
                        print(f"   Scroll {scroll_count}: Saved={saved_count}, Skipped={skipped_count}, "
                              f"Total collected={len(all_videos)}")
                    
                    if new_videos == 0:
                        no_new_videos_count += 1
                        if no_new_videos_count >= max_no_new_scrolls:
                            print(f"\n   No new videos after {max_no_new_scrolls} scrolls - reached end")
                            break
                    else:
                        no_new_videos_count = 0
                    
                    # Occasional longer pause
                    if random.random() > 0.85:
                        HumanBehavior.random_delay(2000, 4000)
                
                # Process any remaining responses
                while api_responses:
                    data = api_responses.pop(0)
                    for video in data.get('itemList', []):
                        video_id = video.get('id')
                        if not video_id or video_id in seen_video_ids:
                            continue
                        seen_video_ids.add(video_id)
                        
                        if skip_existing and video_id in existing_ids:
                            skipped_count += 1
                            continue
                        
                        if max_videos and len(all_videos) >= max_videos:
                            break
                        
                        filepath = self.save_video_metadata(username, video)
                        if filepath:
                            saved_count += 1
                            all_videos.append(video)
                
            except Exception as e:
                print(f"✗ Error: {e}")
                import traceback
                traceback.print_exc()
            
            finally:
                if USING_PATCHRIGHT:
                    context.close()
                else:
                    browser.close()
        
        print(f"\n{'='*70}")
        print(f"Scrape complete for @{username}")
        print(f"Total videos saved this session: {saved_count}")
        print(f"Videos skipped (already existed): {skipped_count}")
        print(f"Total unique videos seen: {len(seen_video_ids)}")
        print(f"Output directory: {self._get_user_video_dir(username)}")
        print(f"{'='*70}")
        
        return all_videos
    
    def _check_for_challenge(self, page: Page) -> bool:
        """Check if we're on a challenge/captcha page"""
        try:
            challenge_selectors = [
                '[class*="captcha"]',
                '[id*="captcha"]',
                '[class*="challenge"]',
                '.verify-wrap',
            ]
            for selector in challenge_selectors:
                if page.query_selector(selector):
                    return True
            return False
        except Exception:
            return False


def main():
    username = "nike"
    
    scraper = TikTokProfileScraper(
        output_dir="tiktok_videos",
        headless=False,
    )
    
    # Fetch ALL videos using scroll-based interception
    videos = scraper.fetch_all_videos(
        username=username,
        max_videos=None,  # Get ALL videos (set to a number to limit)
        skip_existing=True,  # Skip already saved videos
        max_no_new_scrolls=10,  # Stop after 10 scrolls with no new videos
    )
    
    if videos:
        print(f"\n{'='*70}")
        print(f"Sample videos collected this session:")
        print(f"{'='*70}")
        for i, video in enumerate(videos[:5]):
            desc = video.get('desc', 'No description')[:50]
            video_id = video.get('id', 'N/A')
            print(f"  {i+1}. [{video_id}] {desc}...")


if __name__ == "__main__":
    main()