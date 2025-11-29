# # import redis
# # import json
# # import time
# # import os
# # import requests
# # from typing import Optional, Dict, Any
# # from urllib.parse import urlencode, quote
# # from pathlib import Path
# # from dotenv import load_dotenv
# # from celery_config import celery_app
# # import sys

# # # Load .env from parent directory
# # env_path = Path(__file__).parent.parent / '.env'
# # load_dotenv(dotenv_path=env_path)

# # sys.path.append(str(Path(__file__).parent.parent / 'shared'))
# # from storage import upload_file
# # from proxy import get_datacenter_proxy


# # class TikTokProfileScraper:
# #     """TikTok Profile scraper using the private API"""
    
# #     def __init__(self, output_dir: str = "tiktok_videos"):
# #         self.output_dir = output_dir
# #         self._setup_output_directory()
        
# #     def _setup_output_directory(self):
# #         """Create output directory if it doesn't exist"""
# #         if not os.path.exists(self.output_dir):
# #             os.makedirs(self.output_dir)
    
# #     def get_cookies(self) -> Dict[str, str]:
# #         """Get TikTok cookies for API requests"""
# #         cookies = {
# #             'cookie-consent': '{%22optional%22:true%2C%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22hubspot%22:true%2C%22version%22:%22v10%22}',
# #             'living_user_id': '149999902702',
# #             'tt_chain_token': 'g/awArl40iOADD0hHi9e/Q==',
# #             'd_ticket': '578cfb16f8d0da5d1f57811147ae32c1d1e4c',
# #             'uid_tt': '91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8',
# #             'uid_tt_ss': '91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8',
# #             'sid_tt': 'c6960424c3048f7c6e0978192e012638',
# #             'sessionid': 'c6960424c3048f7c6e0978192e012638',
# #             'sessionid_ss': 'c6960424c3048f7c6e0978192e012638',
# #             'store-idc': 'alisg',
# #             'store-country-code': 'kr',
# #             'store-country-code-src': 'uid',
# #             'tt-target-idc': 'alisg',
# #             'tt-target-idc-sign': 'jHcAJBth816HHWGYqpllY256Vw_XVnCFfgixI3_n23HZ8S9rc7uuJBy3lnZ69b6Lr-1s8Y2GP1RyOFAqPJOkmhJiSPC3w_-kvcpRCMG2_Lukc7i4fz-oh6V_QQvmQDqNCgP8UsHB_H-doJa_c73ADQM1cdxzfZ8ShMmIAi3TjpWjbwpU7fD1CNP8jPvqwEwMooHsXIGzhim5NP6iPydcpPFF03qitP0iPfpmRE2oCW4wYgBudTEQda95IYFPRBKVzbVLpQXhLZzzDPlqx894-oZZmhCgLc9CNoCyMaIVZlHvZ_fmW1v33PGRqPJxhxJP3At6jquz1qa_0_2CqNQ9qvwgRP5N79WQz5vidtT7so8o53vUVPt8I6qO0nvM7r8JHo66L4i9-q_ThXG3-2na1yz2Hyn8L54_o4Dn-ETt55-Cx__sgsWvYPgp8TF5jYdO9NouUQMSWJ8gUvq42P_SOnHRse8eksZCOPOkESCKl-O7c7RtKFAI8kP2ltJ9E6e5',
# #             'ttwid': '1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1752014034%7Cba59cb191a734d94f19af0f0136fe84f44d8797f1d8dcacf49a9ae2f8747e9db',
# #             '_ga': 'GA1.1.150342934.1752048579',
# #             '_fbp': 'fb.1.1752048580728.1446697223',
# #             '_ga_NBFTJ2P3P3': 'GS1.1.1752048579.1.1.1752048630.0.0.1773973896',
# #             'pre_country': 'KR',
# #             'lang_type': 'en',
# #             'tta_attr_id_mirror': '0.1755075598.7537992296453636097',
# #             '_tt_enable_cookie': '1',
# #             'ttcsid': '1755660196386::vRKZe4gsZbYCGZvSjeBW.1.1755660196386',
# #             'ttcsid_C97F14JC77U63IDI7U40': '1755660196385::1jScwBvAKvOay5Y3IDYq.1.1755660196625',
# #             '_ga_Y2RSHPPW88': 'GS2.1.s1755660196$o1$g1$t1755660202$j0$l0$h858435056',
# #             '_ga_HV1FL86553': 'GS2.1.s1755660196$o1$g0$t1755660202$j0$l0$h430147227',
# #             '_ttp': '31XBbVW8z3njdHMvhKmUgOZdYYp',
# #             '_ga_TEQXTT9FE4': 'GS1.1.1756345152.1.1.1756345319.0.0.46985635',
# #             'sid_guard': 'c6960424c3048f7c6e0978192e012638%7C1760468508%7C15552000%7CSun%2C+12-Apr-2026+19%3A01%3A48+GMT',
# #             'tt_session_tlb_tag': 'sttt%7C4%7CxpYEJMMEj3xuCXgZLgEmOP_________fzOi7a8IbznWsP6_DCsp0-A9Tmjey7VZ_aYnyddUwa54%3D',
# #             'sid_ucp_v1': '1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA',
# #             'ssid_ucp_v1': '1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA',
# #             'tiktok_webapp_theme_source': 'auto',
# #             'tiktok_webapp_theme': 'dark',
# #             'delay_guest_mode_vid': '5',
# #             'tt_csrf_token': 'xYWajjO9-89aI0fRrZo-yJnaslhIXLFs-kW8',
# #             'perf_feed_cache': '{%22expireTimestamp%22:1762351200000%2C%22itemIds%22:[%227568327995153190199%22%2C%227563637623449865528%22%2C%227560808146038508814%22]}',
# #             'passport_fe_beating_status': 'true',
# #             'ttwid': '1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1762191275%7C4f54d9d00bb07c9e0895413a36ad7cbcc3d69860ada9d8f33f1339433ad06d39',
# #             'store-country-sign': 'MEIEDFHb1dLdjFvdyFpD1AQgKXahhFoDptk3K-l3qFqNAoXi9avo7WbU6GrWds1vgJIEEA6Rm3DxSe6T8R03mWpIby4',
# #             'odin_tt': '0b9fde479be37f79c286f43cf6ed6d115dfc07aaab5b88e4ad689aeef9ed1b2fc6ddeefe1f6af12e93a0d444fc029f2b16012d5d151d30f938e9865f7e695d26',
# #             'msToken': 'mw2wrCFCYJNxQ-LjMcVEOWkMJPZvvgAzJFuwdc3Qq6Mpff6Ef5RGB4AlHSMK1j2HIijQWf5mbUBEVG70RpFwoXp3mFz7ROtvpppCO_aJYV1IdPBCbGiImVZZ1ah9le_lXSArRxauwwh277NEyvjWKL4R',
# #         }
# #         return cookies
    
# #     def get_headers(self, username: str) -> Dict[str, str]:
# #         """Get headers for API requests with username in referer"""
# #         headers = {
# #             'accept': '*/*',
# #             'accept-language': 'en-US,en;q=0.9',
# #             'priority': 'u=1, i',
# #             'referer': f'https://www.tiktok.com/@{username}',
# #             'sec-ch-ua': '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
# #             'sec-ch-ua-mobile': '?0',
# #             'sec-ch-ua-platform': '"Windows"',
# #             'sec-fetch-dest': 'empty',
# #             'sec-fetch-mode': 'cors',
# #             'sec-fetch-site': 'same-origin',
# #             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',
# #         }
# #         return headers

# #     def build_api_url(self, sec_uid: str, cursor: int = 0, count: int = 16) -> str:
# #         """Build the profile API URL with proper encoding (TikTok compatible)"""
# #         base_url = 'https://www.tiktok.com/api/post/item_list/'

# #         params = {
# #             'WebIdLastTime': '1736951461',
# #             'aid': '1988',
# #             'app_language': 'en',
# #             'app_name': 'tiktok_web',
# #             'browser_language': 'en-US',
# #             'browser_name': 'Mozilla',
# #             'browser_online': 'true',
# #             'browser_platform': 'Win32',
# #             'browser_version': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',
# #             'channel': 'tiktok_web',
# #             'clientABVersions': '74733388',
# #             'cookie_enabled': 'true',
# #             'count': str(count),
# #             'coverFormat': '2',
# #             'cursor': str(cursor),
# #             'data_collection_enabled': 'true',
# #             'device_id': '7460149314773288494',
# #             'device_platform': 'web_pc',
# #             'enable_cache': 'false',
# #             'focus_state': 'false',
# #             'from_page': 'user',
# #             'history_len': '3',
# #             'is_fullscreen': 'false',
# #             'is_page_visible': 'true',
# #             'language': 'en',
# #             'needPinnedItemIds': 'true',
# #             'odinId': '7478784916198065170',
# #             'os': 'windows',
# #             'post_item_list_request_type': '0',
# #             'priority_region': 'KR',
# #             'referer': '',
# #             'region': 'KR',
# #             'screen_height': '1080',
# #             'screen_width': '1920',
# #             'secUid': sec_uid,
# #             'tz_name': 'Asia/Seoul',
# #             'user_is_login': 'true',
# #             'video_encoding': 'mp4',
# #             'webcast_language': 'en',
# #         }

# #         # Tokens appended unencoded (TikTok expects raw = / + characters)
# #         ms_token = 'mw2wrCFCYJNxQ-LjMcVEOWkMJPZvvgAzJFuwdc3Qq6Mpff6Ef5RGB4AlHSMK1j2HIijQWf5mbUBEVG70RpFwoXp3mFz7ROtvpppCO_aJYV1IdPBCbGiImVZZ1ah9le_lXSArRxauwwh277NEyvjWKL4R'
# #         x_bogus = 'DFSzsIVYOobANH/ACPjzUkmpF2l8'
# #         x_gnarly = (
# #             'McVjuq/NFgM4vFdZXNG2eamHnsMdmW7Uc/38SzL8/dl7eyGhvB7T7d9DqNeUxTd1TGyyrw6sAPEzYTPjSV-L5W/kW/nfm3I/JO9DcU7dIJvgwkrzMBmAkf90cNGCzR8f3fP5oLl5uvhKL6QE5iEK65UbvruH3F1I7xhEBRCXLOFDi6oFYgVf0m5PGiPlnNEqX59ZiQCniAmvz69t/pxVqTjhXtrOMe1WBCziSopGJ27kvy6ZSzGyppLlUQ/QSp/klifRW-w-yss5vx0NPkEVealvzx0UlLXQiolLTWXaFELyFovUF7pD-ZTdqVtK6yh3AUk='
# #         )

# #         # Encode params with %20 instead of +
# #         query = urlencode(params, quote_via=quote)

# #         # Append tokens manually to preserve raw characters
# #         return f"{base_url}?{query}&msToken={ms_token}&X-Bogus={x_bogus}&X-Gnarly={x_gnarly}"

# #     def get_user_sec_uid(self, username: str) -> Optional[str]:
# #         """Get secUid for a username by visiting their profile page"""
# #         try:
# #             profile_url = f"https://www.tiktok.com/@{username}"
# #             response = requests.get(profile_url, cookies=self.get_cookies(), timeout=30)
            
# #             if response.status_code != 200:
# #                 print(f"Failed to fetch profile for {username}: Status {response.status_code}")
# #                 return None
            
# #             # Try multiple extraction methods
# #             import re
            
# #             # Method 1: Extract from webapp.user-detail JSON structure
# #             pattern1 = r'"webapp\.user-detail":\s*\{[^}]*"userInfo":\s*\{[^}]*"user":\s*\{[^}]*"secUid":\s*"([^"]+)"'
# #             match = re.search(pattern1, response.text)
# #             if match:
# #                 sec_uid = match.group(1)
# #                 print(f"Found secUid for {username}: {sec_uid}")
# #                 return sec_uid
            
# #             # Method 2: Direct secUid search (simpler fallback)
# #             pattern2 = r'"secUid":\s*"(MS4wLjABAAAA[^"]+)"'
# #             match = re.search(pattern2, response.text)
# #             if match:
# #                 sec_uid = match.group(1)
# #                 print(f"Found secUid for {username}: {sec_uid}")
# #                 return sec_uid
            
# #             # Method 3: Try to find any secUid that starts with MS4wLjABAAAA
# #             pattern3 = r'(MS4wLjABAAAA[A-Za-z0-9_-]+)'
# #             matches = re.findall(pattern3, response.text)
# #             if matches:
# #                 # Get the first unique secUid
# #                 sec_uid = matches[0]
# #                 print(f"Found secUid for {username}: {sec_uid}")
# #                 return sec_uid
            
# #             print(f"Could not find secUid for {username}")
# #             return None
            
# #         except Exception as e:
# #             print(f"Error getting secUid for {username}: {e}")
# #             return None

# #     def save_video(self, video_item: Dict[str, Any], username: str):
# #         """Save video JSON to Digital Ocean Spaces"""
# #         try:
# #             video_id = video_item.get('id')
# #             if not video_id:
# #                 print("No video ID found, skipping save")
# #                 return
            
# #             # Create temporary file locally
# #             temp_filename = f"{video_id}.json"
# #             temp_filepath = os.path.join(self.output_dir, temp_filename)
            
# #             # Write JSON to temporary file
# #             with open(temp_filepath, 'w', encoding='utf-8') as f:
# #                 json.dump(video_item, f, indent=2, ensure_ascii=False)
            
# #             # Upload to Digital Ocean Spaces
# #             # Object name: tiktok_video_metadata/{username}/{video_id}.json
# #             object_name = f"tiktok_video_metadata/{username}/{video_id}.json"
            
# #             success = upload_file(temp_filepath, object_name)
            
# #             if success:
# #                 print(f"✓ Uploaded to Spaces: {object_name}")
# #                 # Delete temporary local file after successful upload
# #                 os.remove(temp_filepath)
# #             else:
# #                 print(f"✗ Failed to upload: {object_name}")
            
# #         except Exception as e:
# #             print(f"Error saving video: {e}")
# #             import traceback
# #             traceback.print_exc()
    
# #     def fetch_user_videos(
# #         self, 
# #         username: str, 
# #         sec_uid: str, 
# #         cursor: int = 0
# #     ) -> Optional[Dict[str, Any]]:
# #         """Fetch videos from a user's profile"""
# #         try:
# #             url = self.build_api_url(sec_uid=sec_uid, cursor=cursor)
# #             cookies = self.get_cookies()
# #             headers = self.get_headers(username)

# #             print(url)

# #             print(sec_uid)
            
# #             response = requests.get(url, cookies=cookies, headers=headers, timeout=30)
# #             # print(response.status_code)
# #             # print(response.content)
# #             response.raise_for_status()
            
# #             data = response.json()
# #             return data
            
# #         except requests.exceptions.RequestException as e:
# #             print(f"Error fetching videos for {username}: {e}")
# #             return None
# #         except json.JSONDecodeError as e:
# #             print(f"Error decoding JSON for {username}: {e}")
# #             return None
    
# #     def scrape_user_profile(self, username: str) -> bool:
# #         """Scrape all videos from a user's profile"""
# #         print(f"Starting scrape for user: {username}")
        
# #         # Get secUid for the user
# #         sec_uid = self.get_user_sec_uid(username)
# #         if not sec_uid:
# #             print(f"Failed to get secUid for {username}")
# #             return False
        
# #         print(f"Got secUid for {username}: {sec_uid}")
        
# #         cursor = 0
# #         has_more = True
# #         total_videos = 0
        
# #         while has_more:
# #             print(f"Fetching videos for {username} with cursor: {cursor}")
            
# #             # Fetch videos
# #             data = self.fetch_user_videos(username, sec_uid, cursor)
            
# #             if not data:
# #                 print(f"No data returned for {username}")
# #                 break
            
# #             # Check if there are items
# #             item_list = data.get('itemList', [])
# #             if not item_list:
# #                 print(f"No more videos for {username}")
# #                 break
            
# #             # Save each video
# #             for item in item_list:
# #                 self.save_video(item, username)
# #                 total_videos += 1
            
# #             # Check if there are more videos
# #             has_more = data.get('hasMore', False)
            
# #             if has_more and item_list:
# #                 # Get the createTime of the last video and multiply by 1000 for next cursor
# #                 last_video = item_list[-1]
# #                 create_time = last_video.get('createTime')
# #                 if create_time:
# #                     cursor = int(create_time) * 1000
# #                 else:
# #                     print(f"No createTime found in last video, stopping pagination")
# #                     break
# #             else:
# #                 break
            
# #             # Small delay between requests
# #             time.sleep(2)
        
# #         print(f"Finished scraping {username}. Total videos: {total_videos}")
# #         return True


# # # Celery task
# # @celery_app.task(bind=True, name='tasks.scrape_profile')
# # def scrape_profile_task(self, username: str):
# #     """Celery task to scrape a TikTok profile"""
# #     print(f"Task started for username: {username}")
    
# #     # Initialize scraper
# #     scraper = TikTokProfileScraper()
    
# #     # Initialize Redis
# #     redis_client = redis.Redis(
# #         host=os.getenv("REDIS_HOST", "localhost"),
# #         port=int(os.getenv("REDIS_PORT", 6379)),
# #         # username=os.getenv('REDIS_USERNAME', None) or None,
# #         # password=os.getenv('REDIS_PASSWORD', None) or None,
# #         db=0
# #     )
    
# #     try:
# #         # Check if already scraped
# #         if redis_client.sismember("scraped_usernames", username):
# #             print(f"Username {username} already scraped, skipping")
# #             return {"status": "skipped", "username": username}
        
# #         # Scrape the profile
# #         success = scraper.scrape_user_profile(username)
        
# #         if success:
# #             # Add to scraped_usernames set
# #             redis_client.sadd("scraped_usernames", username)
# #             print(f"Successfully scraped {username}")
# #             return {"status": "success", "username": username}
# #         else:
# #             print(f"Failed to scrape {username}")
# #             return {"status": "failed", "username": username}
            
# #     except Exception as e:
# #         print(f"Error in task for {username}: {e}")
# #         return {"status": "error", "username": username, "error": str(e)}


# import os
# import json
# import time
# import redis
# from urllib.parse import quote
# from collections import OrderedDict
# from pathlib import Path
# from curl_cffi import requests
# from dotenv import load_dotenv
# from celery_config import celery_app
# import sys

# env_path = Path(__file__).parent.parent / ".env"
# load_dotenv(dotenv_path=env_path)

# sys.path.append(str(Path(__file__).parent.parent / "shared"))
# from storage import upload_file


# class TikTokProfileScraper:
#     def __init__(self, output_dir="tiktok_videos"):
#         self.output_dir = output_dir
#         self.session_file = "tiktok_session.json"
#         self.cookies = None
#         self.headers = None
#         self.api_params_items = None
#         self._setup_output_directory()
#         self.load_session()

#     def _setup_output_directory(self):
#         os.makedirs(self.output_dir, exist_ok=True)

#     def load_session(self):
#         """Load single TikTok session for reuse across profiles"""
#         with open(self.session_file, "r", encoding="utf-8") as f:
#             data = json.load(f)
#         self.cookies = data["cookies"]
#         self.headers = data["headers"]
#         self.api_params_items = data["params"]
#         print("✓ Loaded global TikTok session from tiktok_session.json")

#     def build_api_url(self, sec_uid, cursor=0, count=16):
#         """Rebuild profile API URL with only secUid, cursor, and count changed"""
#         base_url = "https://www.tiktok.com/api/post/item_list/"
#         pairs = list(self.api_params_items)

#         def set_or_replace(k, v):
#             for i, (key, _) in enumerate(pairs):
#                 if key == k:
#                     pairs[i] = (k, str(v))
#                     return
#             pairs.append((k, str(v)))

#         set_or_replace("secUid", sec_uid)
#         set_or_replace("cursor", str(cursor))
#         set_or_replace("count", str(count))

#         sig_keys = {"msToken", "X-Bogus", "X-Gnarly"}
#         seen = {k: False for k in sig_keys}
#         deduped = []
#         for k, v in pairs:
#             if k in sig_keys:
#                 if not seen[k]:
#                     deduped.append((k, v))
#                     seen[k] = True
#             else:
#                 deduped.append((k, v))
#         pairs = deduped

#         def encode_pair(k, v):
#             if k in sig_keys:
#                 return f"{quote(k, safe='')}={quote(v, safe='/=')}"
#             return f"{quote(k, safe='')}={quote(v, safe='')}"

#         query = "&".join(encode_pair(k, v) for k, v in pairs)
#         return f"{base_url}?{query}"

#     def get_user_sec_uid(self, username):
#         """Fetch secUid from profile HTML"""
#         import re
#         r = requests.get(f"https://www.tiktok.com/@{username}", impersonate="chrome131")
#         if r.status_code != 200:
#             return None
#         m = re.search(r'"secUid":"(MS4wLjABAAAA[^"]+)"', r.text)
#         return m.group(1) if m else None

#     def fetch_user_videos(self, username, sec_uid, cursor=0):
#         """Request the user’s videos"""
#         url = self.build_api_url(sec_uid, cursor)
#         headers = self.headers.copy()
#         headers["referer"] = f"https://www.tiktok.com/@{username}"

#         print(f"📡 Requesting {username} cursor={cursor}")
#         r = requests.get(url, headers=headers, cookies=self.cookies, impersonate="chrome131", timeout=30)
#         if r.status_code != 200:
#             print(f"✗ {r.status_code} for {username}")
#             return None
#         data = r.json()
#         return data if data.get("itemList") else None

#     def save_video(self, video_item, username):
#         vid = video_item.get("id")
#         if not vid:
#             return
#         fn = os.path.join(self.output_dir, f"{vid}.json")
#         with open(fn, "w", encoding="utf-8") as f:
#             json.dump(video_item, f, indent=2, ensure_ascii=False)
#         obj = f"tiktok_video_metadata/{username}/{vid}.json"
#         if upload_file(fn, obj):
#             os.remove(fn)
#             print(f"✓ Uploaded {vid}")

#     def scrape_user_profile(self, username):
#         print(f"=== Scraping @{username} ===")
#         sec_uid = self.get_user_sec_uid(username)
#         if not sec_uid:
#             print("✗ Failed to get secUid")
#             return False

#         cursor, total = 0, 0
#         while True:
#             data = self.fetch_user_videos(username, sec_uid, cursor)
#             if not data:
#                 break
#             items = data.get("itemList", [])
#             for it in items:
#                 self.save_video(it, username)
#                 total += 1
#             if not data.get("hasMore"):
#                 break
#             last = items[-1].get("createTime")
#             if not last:
#                 break
#             cursor = int(last) * 1000
#             time.sleep(2)

#         print(f"✓ Done @{username} — {total} videos")
#         return True


# @celery_app.task(bind=True, name="tasks.scrape_profile")
# def scrape_profile_task(self, username):
#     scraper = TikTokProfileScraper()
#     redis_client = redis.Redis(
#         host=os.getenv("REDIS_HOST", "localhost"),
#         port=int(os.getenv("REDIS_PORT", 6379)),
#         db=0,
#     )

#     if redis_client.sismember("scraped_usernames", username):
#         return {"status": "skipped", "username": username}

#     ok = scraper.scrape_user_profile(username)
#     if ok:
#         redis_client.sadd("scraped_usernames", username)
#         return {"status": "success", "username": username}
#     return {"status": "failed", "username": username}



import os
import json
import time
import redis
import sys
from typing import Optional, Dict, Any
from urllib.parse import quote
from collections import OrderedDict
from pathlib import Path
from curl_cffi import requests
from dotenv import load_dotenv
from celery_config import celery_app

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

sys.path.append(str(Path(__file__).parent.parent / "shared"))
from storage import upload_file
from proxy import ProxyManager


class TikTokProfileScraper:
    """TikTok Profile scraper using the private API"""

    def __init__(self, output_dir="tiktok_videos", session_file="profile_session.json"):
        self.output_dir = output_dir
        self.session_file = session_file
        self.proxy_manager = ProxyManager()
        
        # Session data
        self.cookies = None
        self.headers = None
        self.api_params_items = None
        
        self._setup_output_directory()
        self.load_session()

    def _setup_output_directory(self):
        os.makedirs(self.output_dir, exist_ok=True)

    def load_session(self):
        """Load TikTok session from file"""
        session_path = Path(__file__).parent / self.session_file
        
        if not session_path.exists():
            raise FileNotFoundError(
                f"Session file not found: {self.session_file}\n"
                f"Please run: python capture_session.py"
            )
        
        with open(session_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        self.cookies = data["cookies"]
        self.headers = data["headers"]
        self.api_params_items = data["params"]
        
        print(f"✓ Loaded session from {self.session_file}")

    def build_api_url(self, sec_uid: str, cursor: int = 0, count: int = 16) -> str:
        """
        Build profile API URL preserving captured parameter order
        Only updates: secUid, cursor, count
        """
        base_url = "https://www.tiktok.com/api/post/item_list/"

        if not self.api_params_items:
            raise Exception("API parameters not initialized.")

        pairs = list(self.api_params_items)

        # Update only the necessary parameters
        def set_or_replace(pairs_list, key, value):
            for i, (k, _) in enumerate(pairs_list):
                if k == key:
                    pairs_list[i] = (key, str(value))
                    return
            pairs_list.append((key, str(value)))

        set_or_replace(pairs, "secUid", sec_uid)
        set_or_replace(pairs, "cursor", str(cursor))
        set_or_replace(pairs, "count", str(count))

        # Deduplicate signature tokens
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

        # Encode parameters
        def encode_pair(k, v):
            if k in sig_keys:
                return f"{quote(k, safe='')}={quote(v, safe='/=')}"
            return f"{quote(k, safe='')}={quote(v, safe='')}"

        query = "&".join(encode_pair(k, v) for k, v in pairs)
        return f"{base_url}?{query}"

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

    def fetch_user_videos(self, username: str, sec_uid: str, cursor: int = 0) -> Optional[Dict[str, Any]]:
        """Fetch videos from user profile"""
        try:
            url = self.build_api_url(sec_uid, cursor)
            
            # Update referer header for this specific user
            headers = self.headers.copy()
            headers["referer"] = f"https://www.tiktok.com/@{username}"

            print(f"📡 Fetching @{username} (cursor={cursor})...")

            # Get proxy
            proxy_config = self.proxy_manager.get_proxy_config(ProxyManager.PROXY_TYPE_ROTATING)

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

    def save_video(self, video_item: Dict[str, Any], username: str):
        """Save video JSON to Digital Ocean Spaces"""
        try:
            video_id = video_item.get('id')
            if not video_id:
                return

            # Create temp file
            temp_filename = f"{video_id}.json"
            temp_filepath = os.path.join(self.output_dir, temp_filename)

            with open(temp_filepath, 'w', encoding='utf-8') as f:
                json.dump(video_item, f, indent=2, ensure_ascii=False)

            # Upload to Spaces
            object_name = f"tiktok_video_metadata/{username}/{video_id}.json"

            if upload_file(temp_filepath, object_name):
                os.remove(temp_filepath)
                print(f"      ✓ Uploaded {video_id}")
            else:
                print(f"      ✗ Failed to upload {video_id}")

        except Exception as e:
            print(f"      ✗ Error saving: {e}")

    def scrape_user_profile(self, username: str) -> bool:
        """Scrape all videos from a user's profile"""
        print(f"\n{'='*70}")
        print(f"  Scraping @{username}")
        print(f"{'='*70}")

        # Get secUid
        sec_uid = self.get_user_sec_uid(username)
        if not sec_uid:
            return False

        cursor = 0
        total_videos = 0

        while True:
            # Fetch videos
            data = self.fetch_user_videos(username, sec_uid, cursor)
            
            if not data:
                break

            item_list = data.get('itemList', [])
            if not item_list:
                break

            # Save each video
            for item in item_list:
                self.save_video(item, username)
                total_videos += 1

            # Check if there are more
            has_more = data.get('hasMore', False)
            
            if has_more and item_list:
                last_video = item_list[-1]
                create_time = last_video.get('createTime')
                if create_time:
                    cursor = int(create_time) * 1000
                else:
                    break
            else:
                break

            time.sleep(2)

        print(f"\n✓ Finished @{username} — {total_videos} videos")
        return True


@celery_app.task(bind=True, name="tasks.scrape_profile")
def scrape_profile_task(self, username: str):
    """Celery task to scrape a TikTok profile"""
    print(f"\nTask: Scrape @{username}")

    # Initialize scraper (loads session from file)
    scraper = TikTokProfileScraper()

    # Initialize Redis
    redis_client = redis.Redis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=int(os.getenv("REDIS_PORT", 6379)),
        db=0
    )

    try:
        # Check if already scraped
        if redis_client.sismember("scraped_usernames", username):
            print(f"⊗ Already scraped @{username}")
            return {"status": "skipped", "username": username}

        # Scrape the profile
        success = scraper.scrape_user_profile(username)

        if success:
            redis_client.sadd("scraped_usernames", username)
            return {"status": "success", "username": username}
        else:
            return {"status": "failed", "username": username}

    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return {"status": "error", "username": username, "error": str(e)}