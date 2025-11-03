import redis
import json
import time
import os
import requests
from typing import Optional, Dict, Any
from urllib.parse import urlencode, quote
from pathlib import Path
from dotenv import load_dotenv
from celery_config import celery_app

# Load .env from parent directory
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)


class TikTokProfileScraper:
    """TikTok Profile scraper using the private API"""
    
    def __init__(self, output_dir: str = "tiktok_videos"):
        self.output_dir = output_dir
        self._setup_output_directory()
        
    def _setup_output_directory(self):
        """Create output directory if it doesn't exist"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def get_cookies(self) -> Dict[str, str]:
        """Get TikTok cookies for API requests"""
        cookies = {
            'cookie-consent': '{%22optional%22:true%2C%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22hubspot%22:true%2C%22version%22:%22v10%22}',
            'living_user_id': '149999902702',
            'tt_chain_token': 'g/awArl40iOADD0hHi9e/Q==',
            'd_ticket': '578cfb16f8d0da5d1f57811147ae32c1d1e4c',
            'uid_tt': '91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8',
            'uid_tt_ss': '91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8',
            'sid_tt': 'c6960424c3048f7c6e0978192e012638',
            'sessionid': 'c6960424c3048f7c6e0978192e012638',
            'sessionid_ss': 'c6960424c3048f7c6e0978192e012638',
            'store-idc': 'alisg',
            'store-country-code': 'kr',
            'store-country-code-src': 'uid',
            'tt-target-idc': 'alisg',
            'tt-target-idc-sign': 'jHcAJBth816HHWGYqpllY256Vw_XVnCFfgixI3_n23HZ8S9rc7uuJBy3lnZ69b6Lr-1s8Y2GP1RyOFAqPJOkmhJiSPC3w_-kvcpRCMG2_Lukc7i4fz-oh6V_QQvmQDqNCgP8UsHB_H-doJa_c73ADQM1cdxzfZ8ShMmIAi3TjpWjbwpU7fD1CNP8jPvqwEwMooHsXIGzhim5NP6iPydcpPFF03qitP0iPfpmRE2oCW4wYgBudTEQda95IYFPRBKVzbVLpQXhLZzzDPlqx894-oZZmhCgLc9CNoCyMaIVZlHvZ_fmW1v33PGRqPJxhxJP3At6jquz1qa_0_2CqNQ9qvwgRP5N79WQz5vidtT7so8o53vUVPt8I6qO0nvM7r8JHo66L4i9-q_ThXG3-2na1yz2Hyn8L54_o4Dn-ETt55-Cx__sgsWvYPgp8TF5jYdO9NouUQMSWJ8gUvq42P_SOnHRse8eksZCOPOkESCKl-O7c7RtKFAI8kP2ltJ9E6e5',
            'ttwid': '1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1752014034%7Cba59cb191a734d94f19af0f0136fe84f44d8797f1d8dcacf49a9ae2f8747e9db',
            '_ga': 'GA1.1.150342934.1752048579',
            '_fbp': 'fb.1.1752048580728.1446697223',
            '_ga_NBFTJ2P3P3': 'GS1.1.1752048579.1.1.1752048630.0.0.1773973896',
            'pre_country': 'KR',
            'lang_type': 'en',
            'tta_attr_id_mirror': '0.1755075598.7537992296453636097',
            '_tt_enable_cookie': '1',
            'ttcsid': '1755660196386::vRKZe4gsZbYCGZvSjeBW.1.1755660196386',
            'ttcsid_C97F14JC77U63IDI7U40': '1755660196385::1jScwBvAKvOay5Y3IDYq.1.1755660196625',
            '_ga_Y2RSHPPW88': 'GS2.1.s1755660196$o1$g1$t1755660202$j0$l0$h858435056',
            '_ga_HV1FL86553': 'GS2.1.s1755660196$o1$g0$t1755660202$j0$l0$h430147227',
            '_ttp': '31XBbVW8z3njdHMvhKmUgOZdYYp',
            '_ga_TEQXTT9FE4': 'GS1.1.1756345152.1.1.1756345319.0.0.46985635',
            'sid_guard': 'c6960424c3048f7c6e0978192e012638%7C1760468508%7C15552000%7CSun%2C+12-Apr-2026+19%3A01%3A48+GMT',
            'tt_session_tlb_tag': 'sttt%7C4%7CxpYEJMMEj3xuCXgZLgEmOP_________fzOi7a8IbznWsP6_DCsp0-A9Tmjey7VZ_aYnyddUwa54%3D',
            'sid_ucp_v1': '1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA',
            'ssid_ucp_v1': '1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA',
            'tiktok_webapp_theme_source': 'auto',
            'tiktok_webapp_theme': 'dark',
            'delay_guest_mode_vid': '5',
            'tt_csrf_token': 'xYWajjO9-89aI0fRrZo-yJnaslhIXLFs-kW8',
            'perf_feed_cache': '{%22expireTimestamp%22:1762351200000%2C%22itemIds%22:[%227568327995153190199%22%2C%227563637623449865528%22%2C%227560808146038508814%22]}',
            'passport_fe_beating_status': 'true',
            'ttwid': '1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1762191275%7C4f54d9d00bb07c9e0895413a36ad7cbcc3d69860ada9d8f33f1339433ad06d39',
            'store-country-sign': 'MEIEDFHb1dLdjFvdyFpD1AQgKXahhFoDptk3K-l3qFqNAoXi9avo7WbU6GrWds1vgJIEEA6Rm3DxSe6T8R03mWpIby4',
            'odin_tt': '0b9fde479be37f79c286f43cf6ed6d115dfc07aaab5b88e4ad689aeef9ed1b2fc6ddeefe1f6af12e93a0d444fc029f2b16012d5d151d30f938e9865f7e695d26',
            'msToken': 'mw2wrCFCYJNxQ-LjMcVEOWkMJPZvvgAzJFuwdc3Qq6Mpff6Ef5RGB4AlHSMK1j2HIijQWf5mbUBEVG70RpFwoXp3mFz7ROtvpppCO_aJYV1IdPBCbGiImVZZ1ah9le_lXSArRxauwwh277NEyvjWKL4R',
        }
        return cookies
    
    def get_headers(self, username: str) -> Dict[str, str]:
        """Get headers for API requests with username in referer"""
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'priority': 'u=1, i',
            'referer': f'https://www.tiktok.com/@{username}',
            'sec-ch-ua': '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',
        }
        return headers
    
    def build_api_url(self, sec_uid: str, cursor: int = 0, count: int = 16) -> str:
        """Build the profile API URL with proper parameters"""
        base_url = 'https://www.tiktok.com/api/post/item_list/'
        
        params = {
            'WebIdLastTime': '1736951461',
            'aid': '1988',
            'app_language': 'en',
            'app_name': 'tiktok_web',
            'browser_language': 'en-US',
            'browser_name': 'Mozilla',
            'browser_online': 'true',
            'browser_platform': 'Win32',
            'browser_version': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',
            'channel': 'tiktok_web',
            'clientABVersions': '74733388',
            'cookie_enabled': 'true',
            'count': str(count),
            'coverFormat': '2',
            'cursor': str(cursor),
            'data_collection_enabled': 'true',
            'device_id': '7460149314773288494',
            'device_platform': 'web_pc',
            'enable_cache': 'false',
            'focus_state': 'false',
            'from_page': 'user',
            'history_len': '3',
            'is_fullscreen': 'false',
            'is_page_visible': 'true',
            'language': 'en',
            'needPinnedItemIds': 'true',
            'odinId': '7478784916198065170',
            'os': 'windows',
            'post_item_list_request_type': '0',
            'priority_region': 'KR',
            'referer': '',
            'region': 'KR',
            'screen_height': '1080',
            'screen_width': '1920',
            'secUid': sec_uid,
            'tz_name': 'Asia/Seoul',
            'user_is_login': 'true',
            'video_encoding': 'mp4',
            'webcast_language': 'en',
        }
        
        # Tokens to append manually
        ms_token = 'mw2wrCFCYJNxQ-LjMcVEOWkMJPZvvgAzJFuwdc3Qq6Mpff6Ef5RGB4AlHSMK1j2HIijQWf5mbUBEVG70RpFwoXp3mFz7ROtvpppCO_aJYV1IdPBCbGiImVZZ1ah9le_lXSArRxauwwh277NEyvjWKL4R'
        x_bogus = 'DFSzsIVYOobANH/ACPjzUkmpF2l8'
        x_gnarly = 'McVjuq/NFgM4vFdZXNG2eamHnsMdmW7Uc/38SzL8/dl7eyGhvB7T7d9DqNeUxTd1TGyyrw6sAPEzYTPjSV-L5W/kW/nfm3I/JO9DcU7dIJvgwkrzMBmAkf90cNGCzR8f3fP5oLl5uvhKL6QE5iEK65UbvruH3F1I7xhEBRCXLOFDi6oFYgVf0m5PGiPlnNEqX59ZiQCniAmvz69t/pxVqTjhXtrOMe1WBCziSopGJ27kvy6ZSzGyppLlUQ/QSp/klifRW-w-yss5vx0NPkEVealvzx0UlLXQiolLTWXaFELyFovUF7pD-ZTdqVtK6yh3AUk='
        
        # Encode params
        query = urlencode(params, quote_via=quote)
        
        # Append tokens manually
        return f"{base_url}?{query}&msToken={ms_token}&X-Bogus={x_bogus}&X-Gnarly={x_gnarly}"
    
    def get_user_sec_uid(self, username: str) -> Optional[str]:
        """Get secUid for a username by visiting their profile page"""
        try:
            profile_url = f"https://www.tiktok.com/@{username}"
            response = requests.get(profile_url, cookies=self.get_cookies(), timeout=30)
            
            if 'secUid' in response.text:
                import re
                match = re.search(r'"secUid":"([^"]+)"', response.text)
                if match:
                    return match.group(1)
            
            print(f"Could not find secUid for {username}")
            return None
            
        except Exception as e:
            print(f"Error getting secUid for {username}: {e}")
            return None
    
    def save_video(self, video_item: Dict[str, Any], username: str):
        """Save individual video JSON to a file"""
        try:
            video_id = video_item.get('id')
            if not video_id:
                print("No video ID found, skipping save")
                return
            
            # Create username directory if it doesn't exist
            user_dir = f"{self.output_dir}/{username}"
            if not os.path.exists(user_dir):
                os.makedirs(user_dir)
            
            filename = f"{user_dir}/{video_id}.json"
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(video_item, f, indent=2, ensure_ascii=False)
            
            print(f"Saved video: {filename}")
            
        except Exception as e:
            print(f"Error saving video: {e}")
    
    def fetch_user_videos(
        self, 
        username: str, 
        sec_uid: str, 
        cursor: int = 0
    ) -> Optional[Dict[str, Any]]:
        """Fetch videos from a user's profile"""
        try:
            url = self.build_api_url(sec_uid=sec_uid, cursor=cursor)
            cookies = self.get_cookies()
            headers = self.get_headers(username)
            
            response = requests.get(url, cookies=cookies, headers=headers, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            return data
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching videos for {username}: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON for {username}: {e}")
            return None
    
    def scrape_user_profile(self, username: str) -> bool:
        """Scrape all videos from a user's profile"""
        print(f"Starting scrape for user: {username}")
        
        # Get secUid for the user
        sec_uid = self.get_user_sec_uid(username)
        if not sec_uid:
            print(f"Failed to get secUid for {username}")
            return False
        
        print(f"Got secUid for {username}: {sec_uid}")
        
        cursor = 0
        has_more = True
        total_videos = 0
        
        while has_more:
            print(f"Fetching videos for {username} with cursor: {cursor}")
            
            # Fetch videos
            data = self.fetch_user_videos(username, sec_uid, cursor)
            
            if not data:
                print(f"No data returned for {username}")
                break
            
            # Check if there are items
            item_list = data.get('itemList', [])
            if not item_list:
                print(f"No more videos for {username}")
                break
            
            # Save each video
            for item in item_list:
                self.save_video(item, username)
                total_videos += 1
            
            # Check if there are more videos
            has_more = data.get('hasMore', False)
            
            if has_more and item_list:
                # Get the createTime of the last video and multiply by 1000 for next cursor
                last_video = item_list[-1]
                create_time = last_video.get('createTime')
                if create_time:
                    cursor = int(create_time) * 1000
                else:
                    print(f"No createTime found in last video, stopping pagination")
                    break
            else:
                break
            
            # Small delay between requests
            time.sleep(2)
        
        print(f"Finished scraping {username}. Total videos: {total_videos}")
        return True


# Celery task
@celery_app.task(bind=True, name='tasks.scrape_profile')
def scrape_profile_task(self, username: str):
    """Celery task to scrape a TikTok profile"""
    print(f"Task started for username: {username}")
    
    # Initialize scraper
    scraper = TikTokProfileScraper()
    
    # Initialize Redis
    redis_client = redis.Redis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=int(os.getenv("REDIS_PORT", 6379)),
        username=os.getenv('REDIS_USERNAME', None) or None,
        password=os.getenv('REDIS_PASSWORD', None) or None,
        db=0
    )
    
    try:
        # Check if already scraped
        if redis_client.sismember("scraped_usernames", username):
            print(f"Username {username} already scraped, skipping")
            return {"status": "skipped", "username": username}
        
        # Scrape the profile
        success = scraper.scrape_user_profile(username)
        
        if success:
            # Add to scraped_usernames set
            redis_client.sadd("scraped_usernames", username)
            print(f"Successfully scraped {username}")
            return {"status": "success", "username": username}
        else:
            print(f"Failed to scrape {username}")
            return {"status": "failed", "username": username}
            
    except Exception as e:
        print(f"Error in task for {username}: {e}")
        return {"status": "error", "username": username, "error": str(e)}