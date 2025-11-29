# import redis
# import json
# import time
# import os
# import sys
# import requests
# import argparse
# from typing import Optional, Dict, Any, List
# from urllib.parse import urlencode, quote 
# from pathlib import Path
# from dotenv import load_dotenv
# from celery import Celery

# # Load .env from parent directory
# env_path = Path(__file__).parent.parent / '.env'
# load_dotenv(dotenv_path=env_path)

# sys.path.append(str(Path(__file__).parent.parent / 'shared'))
# from storage import upload_file
# from proxy import get_datacenter_proxy

# # Initialize Celery connection for sending tasks
# celery_app = Celery(
#     'tiktok_scraper',
#     broker=f"redis://{os.getenv('REDIS_HOST', 'localhost')}:{os.getenv('REDIS_PORT', 6379)}/0"
#     # broker=f"redis://{os.getenv('REDIS_USERNAME', '')}:{os.getenv('REDIS_PASSWORD', '')}@{os.getenv('REDIS_HOST', 'localhost')}:{os.getenv('REDIS_PORT', 6379)}/0"
# )


# class TikTokFYPScraper:
#     """TikTok For You Page scraper using the private API"""
    
#     def __init__(
#         self,
#         redis_client: redis.Redis,
#         output_dir: str = "tiktok_video_metadata"
#     ):
#         self.redis_client = redis_client
#         self.output_dir = output_dir
#         self.last_new_account_time = time.time()
#         self._setup_output_directory()
        
#     def _setup_output_directory(self):
#         """Create output directory if it doesn't exist"""
#         if not os.path.exists(self.output_dir):
#             os.makedirs(self.output_dir)
    
#     def get_cookies(self) -> Dict[str, str]:
#         """Get TikTok cookies for API requests"""
#         # cookies = {
#         #     'cookie-consent': '{%22optional%22:true%2C%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22hubspot%22:true%2C%22version%22:%22v10%22}',
#         #     'living_user_id': '149999902702',
#         #     'tt_chain_token': 'g/awArl40iOADD0hHi9e/Q==',
#         #     'd_ticket': '578cfb16f8d0da5d1f57811147ae32c1d1e4c',
#         #     'uid_tt': '91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8',
#         #     'uid_tt_ss': '91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8',
#         #     'sid_tt': 'c6960424c3048f7c6e0978192e012638',
#         #     'sessionid': 'c6960424c3048f7c6e0978192e012638',
#         #     'sessionid_ss': 'c6960424c3048f7c6e0978192e012638',
#         #     'store-idc': 'alisg',
#         #     'store-country-code': 'kr',
#         #     'store-country-code-src': 'uid',
#         #     'tt-target-idc': 'alisg',
#         #     'tt-target-idc-sign': 'jHcAJBth816HHWGYqpllY256Vw_XVnCFfgixI3_n23HZ8S9rc7uuJBy3lnZ69b6Lr-1s8Y2GP1RyOFAqPJOkmhJiSPC3w_-kvcpRCMG2_Lukc7i4fz-oh6V_QQvmQDqNCgP8UsHB_H-doJa_c73ADQM1cdxzfZ8ShMmIAi3TjpWjbwpU7fD1CNP8jPvqwEwMooHsXIGzhim5NP6iPydcpPFF03qitP0iPfpmRE2oCW4wYgBudTEQda95IYFPRBKVzbVLpQXhLZzzDPlqx894-oZZmhCgLc9CNoCyMaIVZlHvZ_fmW1v33PGRqPJxhxJP3At6jquz1qa_0_2CqNQ9qvwgRP5N79WQz5vidtT7so8o53vUVPt8I6qO0nvM7r8JHo66L4i9-q_ThXG3-2na1yz2Hyn8L54_o4Dn-ETt55-Cx__sgsWvYPgp8TF5jYdO9NouUQMSWJ8gUvq42P_SOnHRse8eksZCOPOkESCKl-O7c7RtKFAI8kP2ltJ9E6e5',
#         #     'ttwid': '1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1752014034%7Cba59cb191a734d94f19af0f0136fe84f44d8797f1d8dcacf49a9ae2f8747e9db',
#         #     '_ga': 'GA1.1.150342934.1752048579',
#         #     '_fbp': 'fb.1.1752048580728.1446697223',
#         #     '_ga_NBFTJ2P3P3': 'GS1.1.1752048579.1.1.1752048630.0.0.1773973896',
#         #     'pre_country': 'KR',
#         #     'lang_type': 'en',
#         #     'tta_attr_id_mirror': '0.1755075598.7537992296453636097',
#         #     '_tt_enable_cookie': '1',
#         #     'ttcsid': '1755660196386::vRKZe4gsZbYCGZvSjeBW.1.1755660196386',
#         #     'ttcsid_C97F14JC77U63IDI7U40': '1755660196385::1jScwBvAKvOay5Y3IDYq.1.1755660196625',
#         #     '_ga_Y2RSHPPW88': 'GS2.1.s1755660196$o1$g1$t1755660202$j0$l0$h858435056',
#         #     '_ga_HV1FL86553': 'GS2.1.s1755660196$o1$g0$t1755660202$j0$l0$h430147227',
#         #     '_ttp': '31XBbVW8z3njdHMvhKmUgOZdYYp',
#         #     '_ga_TEQXTT9FE4': 'GS1.1.1756345152.1.1.1756345319.0.0.46985635',
#         #     'sid_guard': 'c6960424c3048f7c6e0978192e012638%7C1760468508%7C15552000%7CSun%2C+12-Apr-2026+19%3A01%3A48+GMT',
#         #     'tt_session_tlb_tag': 'sttt%7C4%7CxpYEJMMEj3xuCXgZLgEmOP_________fzOi7a8IbznWsP6_DCsp0-A9Tmjey7VZ_aYnyddUwa54%3D',
#         #     'sid_ucp_v1': '1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA',
#         #     'ssid_ucp_v1': '1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA',
#         #     'tiktok_webapp_theme_source': 'auto',
#         #     'tiktok_webapp_theme': 'dark',
#         #     'delay_guest_mode_vid': '5',
#         #     'tt_csrf_token': 'xYWajjO9-89aI0fRrZo-yJnaslhIXLFs-kW8',
#         #     'store-country-sign': 'MEIEDBKdqGvnG5UAo5FXbwQgAm15FzxCZRJzVE_IqmgWlnlT7svrenSYBbR9w-g-oRsEEF7CnPC1TU3oVf8kCi26MV4',
#         #     'msToken': 'Xb5ISAL1qu4crHwjKKLRrctkVp1TEq5L-n_n90700NHS_cRZewdWtNn08cFvXpfj86NB79ISVgXL0ZJ4Ar5wbwp5QQsyafQl8i8Jocj24HK2v_F8llI3Jr3WmR1of_6wKdXt6rywsxWWStV_r-baiy_dnw==',
#         #     'odin_tt': '55702be48b513482b777bcd6455e0453a917564e2ca5250690bf55a79a7e9972359024426402e79fb654913da3e1b60ab52fd8d6fbe071f3a91cafe0d0a83e3c',
#         #     'passport_fe_beating_status': 'false',
#         #     'perf_feed_cache': '{%22expireTimestamp%22:1762351200000%2C%22itemIds%22:[%227565222614025686285%22%2C%227553551072632147211%22%2C%227567781083329170701%22]}',
#         #     'ttwid': '1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1762180132%7C03a7156af52f7028f1bd89d5799983d4e24445a7d55aec361f1c84fce271bbc0',
#         # }
        
#         r = requests.get("https://tiktok.com")
#         r_cookies = r.cookies.get_dict()

#         cookies = {
#             # 'cookie-consent': '{%22optional%22:true%2C%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22hubspot%22:true%2C%22version%22:%22v10%22}',
#             # 'living_user_id': '149999902702',
#             # 'tt_chain_token': '00iMvcDV9fK8UQnace7dmA%3D%3D',
#             'tt_chain_token': r_cookies['tt_chain_token']
#             # 'ttwid': '1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1752014034%7Cba59cb191a734d94f19af0f0136fe84f44d8797f1d8dcacf49a9ae2f8747e9db',
#             # 'tt_csrf_token': 'FkTc88CP-wo4Z31qGTjMSwYE4SkM3i2HipXA',
#             # 'msToken': '0JnvKq9p4Dt4D-d9I9jdcuJ9HuClM7-CsLr0UdFNfYbg3_AQCX94j3On0XVPZGB-vKVZzo_VetHzyVJXUW8kFB68SWQAppr_X5ITa6FL2KjGV6UWkTdVwNGWQnrPQNIntaadsG6iJvhl54CFe_wxj9IBnQ%3D%3D',
#             # 'ttwid': '1%7C5zjD0xS3YQr3dw_C8DY78ImpanF6Xpl_mHygDoVTwNY%7C1762235204%7Ca6416c5d6cd0391c3bfca0dd142ab1cbbb22ad4689454cbc7cb6b189ed169908',
#         }

#         return cookies
    
#     def get_headers(self) -> Dict[str, str]:
#         """Get headers for API requests"""
#         headers = {
#             'accept': '*/*',
#             'accept-language': 'en-US,en;q=0.9',
#             'priority': 'u=1, i',
#             'referer': 'https://www.tiktok.com/',
#             'sec-ch-ua': '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"Windows"',
#             'sec-fetch-dest': 'empty',
#             'sec-fetch-mode': 'cors',
#             'sec-fetch-site': 'same-origin',
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',
#         }
#         return headers

#     def build_api_url(self, count: int = 6) -> str:
#         base_url = 'https://www.tiktok.com/api/recommend/item_list/'

#         params = {
#             'WebIdLastTime': '1736951461',
#             'aid': '1988',
#             'app_language': 'en',
#             'app_name': 'tiktok_web',
#             'browser_language': 'en-US',
#             'browser_name': 'Mozilla',
#             'browser_online': 'true',
#             'browser_platform': 'Win32',
#             'browser_version': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',
#             'channel': 'tiktok_web',
#             'clientABVersions': '74800760,70508271,72437276,73720540,74250915,74393673,74446915,74465399,74465409,74536864,74609147,74627577,74632791,74674280,74676351,74679798,74686502,74700792,74703727,74711111,74733472,74746519,74746610,74757744,74767144,74767851,74782564,74792133,74793837,74798337,74798356,74808329,74810092,74811360,74819402,74824020,74872266,74882809,70138197,70156809,70405643,71057832,71200802,71381811,71516509,71803300,71962127,72360691,72408100,72854054,72892778,73004916,73171280,73208420,73989921,74276218,74844724',
#             'cookie_enabled': 'true',
#             'count': str(count),
#             'coverFormat': '2',
#             'cpu_core_number': '12',
#             'dark_mode': 'false',
#             'data_collection_enabled': 'true',
#             'day_of_week': '1',
#             'device_id': '7460149314773288494',
#             # 'device_id': '8498498349839438943',
#             'device_platform': 'web_pc',
#             'device_score': '8.57',
#             'device_type': 'web_h264',
#             'enable_cache': 'false',
#             'focus_state': 'true',
#             'from_page': 'fyp',
#             'history_len': '2',
#             'isNonPersonalized': 'false',
#             'is_fullscreen': 'false',
#             'is_page_visible': 'true',
#             'itemID': '',
#             'language': 'en',
#             'launch_mode': 'direct',
#             'network': '10',
#             'odinId': '7478784916198065170',
#             'os': 'windows',
#             'priority_region': 'KR',
#             'pullType': '1',
#             'referer': '',
#             'region': 'KR',
#             'screen_height': '1080',
#             'screen_width': '1920',
#             'showAboutThisAd': 'true',
#             'showAds': 'true',
#             'time_of_day': '23',
#             'tz_name': 'Asia/Seoul',
#             'video_encoding': '',
#             'vv_count': '12529',
#             'vv_count_fyp': '2637',
#             'watchLiveLastTime': '1741102304984',
#             'webcast_language': 'en',
#             'window_height': '962',
#             'window_width': '150',
#         }

#         # exclude msToken from urlencode to keep '=' unencoded
#         ms_token = 'Xb5ISAL1qu4crHwjKKLRrctkVp1TEq5L-n_n90700NHS_cRZewdWtNn08cFvXpfj86NB79ISVgXL0ZJ4Ar5wbwp5QQsyafQl8i8Jocj24HK2v_F8llI3Jr3WmR1of_6wKdXt6rywsxWWStV_r-baiy_dnw=='
        
#         x_bogus = 'DFSzsIVYt2tANH/ACPJVwimpF2W/'
#         x_gnarly = (
#             'Mw1bQHB/564boDbZQP6s-ShaK79iOfgOU57EoHgX55VO37v9-rSjMDEUveU9Nfm5dxJhESWUyRv4djcH4XUtOYukfRsLuySJRYRPMg37l9HL0XBOV0uTQJuCiwefkvLfYgShxDL-m543VJlr2-f2HHDjhsnNo6F10fQWHlSqptwrCQCKoyBctGFyOMd/cKJpCHGAvva4IxMPEQVXKqALpvG90JdQ4ERuMgAs11wKA97EXkbVCZigzSSJPsJFTwxkiF9SYENojM6LDiv2DEBH-1jU4pOll-gPUyLf0bY1IfEricLsZqdGwDDIhWCWS8EYYPz='
#         )

#         # Encode only safe params
#         query = urlencode(params, quote_via=quote)

#         # Append msToken and others manually (unencoded)
#         return f"{base_url}?{query}&msToken={ms_token}&X-Bogus={x_bogus}&X-Gnarly={x_gnarly}"
#         # return f"{base_url}?{query}"

    
#     def save_video_item(self, item: Dict[str, Any]):
#         """Save individual video item JSON to a file"""
#         try:
#             video_id = item.get('id')
#             if not video_id:
#                 print("No video ID found, skipping save")
#                 return
            
#             filename = f"{self.output_dir}/{video_id}.json"
            
#             with open(filename, 'w', encoding='utf-8') as f:
#                 json.dump(item, f, indent=2, ensure_ascii=False)
            
#             print(f"Saved video: {filename}")
            
#         except Exception as e:
#             print(f"Error saving video item: {e}")
    
#     def process_accounts(self, items: List[Dict[str, Any]]):
#         """Process accounts from video items and add to Redis queue"""
#         for item in items:
#             try:
#                 author = item.get('author', {})
#                 unique_id = author.get('uniqueId')
                
#                 if unique_id:
#                     # if not self.redis_client.sismember("scraped_usernames", unique_id):
#                     #     self.redis_client.sadd("queued_usernames", unique_id)
#                     #     print(f"Added {unique_id} to scraping queue")
#                     #     self.last_new_account_time = time.time()
#                     if not self.redis_client.sismember("scraped_usernames", unique_id):
#                         # Send task directly to Celery
#                         celery_app.send_task(
#                             'tasks.scrape_profile',
#                             args=[unique_id]
#                         )
#                         print(f"Queued Celery task for: {unique_id}")
#                         self.last_new_account_time = time.time()
#                     else:
#                         print(f"Skipping {unique_id} - already in scraped_usernames")
                        
#             except Exception as e:
#                 print(f"Error processing account: {e}")
    
#     def fetch_fyp_videos(self) -> Optional[List[Dict[str, Any]]]:
#         """Fetch videos from the FYP API"""
#         try:
#             url = self.build_api_url(count=6)
#             cookies = self.get_cookies()
#             headers = self.get_headers()
            
#             response = requests.get(url, cookies=cookies, headers=headers, timeout=30, proxies=get_datacenter_proxy())
#             response.raise_for_status()
            
#             data = response.json()
            
#             if 'itemList' in data and data['itemList']:
#                 print(f"Fetched {len(data['itemList'])} videos from FYP")
#                 return data['itemList']
#             else:
#                 print("No items found in FYP response")
#                 return None
                
#         except requests.exceptions.RequestException as e:
#             print(f"Error fetching FYP videos: {e}")
#             return None
#         except json.JSONDecodeError as e:
#             print(f"Error decoding JSON response: {e}")
#             return None
    
#     def run(self, max_iterations: Optional[int] = None, delay: int = 5):
#         """
#         Run the FYP scraper continuously
        
#         Args:
#             max_iterations: Maximum number of iterations (None for infinite)
#             delay: Delay in seconds between requests
#         """
#         print("Starting FYP scraper...")
#         iteration = 0
        
#         while True:
#             # Check if we should stop
#             if max_iterations and iteration >= max_iterations:
#                 print(f"Reached max iterations: {max_iterations}")
#                 break
            
#             # Check for timeout (no new accounts in 5 minutes)
#             if time.time() - self.last_new_account_time > 300:
#                 sys.exit("No new accounts found in the last 5 minutes. Exiting...")
            
#             # Fetch videos
#             items = self.fetch_fyp_videos()
            
#             if items:
#                 # Save each video item as separate JSON file
#                 # for item in items:
#                 #     self.save_video_item(item)
                
#                 # Process accounts for queue
#                 self.process_accounts(items)
            
#             iteration += 1
#             print(f"Iteration {iteration} complete. Waiting {delay} seconds...")
#             time.sleep(delay)




# import redis
# import json
# import time
# import os
# import sys
# import requests
# import argparse
# from typing import Optional, Dict, Any, List
# from urllib.parse import urlencode, quote, urlparse, parse_qs
# from pathlib import Path
# from dotenv import load_dotenv
# from celery import Celery
# from playwright.sync_api import sync_playwright

# # Load .env from parent directory
# env_path = Path(__file__).parent.parent / '.env'
# load_dotenv(dotenv_path=env_path)

# sys.path.append(str(Path(__file__).parent.parent / 'shared'))
# from storage import upload_file
# # from proxy import ProxyManager
# from proxy import get_datacenter_proxy 
# # Initialize Celery connection for sending tasks
# celery_app = Celery(
#     'tiktok_scraper',
#     broker=f"redis://{os.getenv('REDIS_HOST', 'localhost')}:{os.getenv('REDIS_PORT', 6379)}/0"
# )


# class TikTokFYPScraper:
#     """TikTok For You Page scraper using the private API"""
    
#     def __init__(
#         self,
#         redis_client: redis.Redis,
#         output_dir: str = "tiktok_video_metadata"
#     ):
#         self.redis_client = redis_client
#         self.output_dir = output_dir
#         self.last_new_account_time = time.time()
#         # self.proxy_manager = ProxyManager()
        
#         # Will be set by get_fresh_session_data()
#         self.cookies = None
#         self.headers = None
#         self.api_params = {}
        
#         self._setup_output_directory()
        
#     def _setup_output_directory(self):
#         """Create output directory if it doesn't exist"""
#         if not os.path.exists(self.output_dir):
#             os.makedirs(self.output_dir)
    
#     def get_fresh_session_data(self, min_requests: int = 5):
#         """
#         Use Playwright to capture a working API request to 
#         https://www.tiktok.com/api/recommend/item_list/
#         Waits for multiple requests and uses the last one
        
#         Args:
#             min_requests: Minimum number of API requests to wait for before capturing
#         """
#         print("=" * 70)
#         print("Capturing TikTok FYP API request using Playwright...")
#         print("=" * 70)
        
#         with sync_playwright() as p:
#             browser = p.chromium.launch(headless=False)
            
#             context = browser.new_context(
#                 viewport={'width': 1920, 'height': 1080},
#                 user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
#                 locale='en-US',
#                 timezone_id='America/New_York'
#             )
            
#             page = context.new_page()
            
#             # Track all requests to the recommend/item_list endpoint
#             captured_requests = []
            
#             def handle_request(request):
#                 # Only count requests to recommend/item_list
#                 if 'api/recommend/item_list/' in request.url:
#                     request_num = len(captured_requests) + 1
#                     captured_requests.append({
#                         'url': request.url,
#                         'headers': request.headers,
#                         'number': request_num
#                     })
#                     print(f"   ✓ Captured recommend/item_list request #{request_num}")
            
#             page.on('request', handle_request)
            
#             try:
#                 print("\n1. Navigating to TikTok For You Page...")
#                 page.goto('https://www.tiktok.com/foryou', wait_until='domcontentloaded', timeout=60000)
                
#                 print(f"\n2. Waiting for at least {min_requests} recommend/item_list requests...")
#                 time.sleep(3)
                
#                 print("\n3. Scrolling to trigger more API requests...")
#                 # Scroll until we have enough requests
#                 scroll_count = 0
#                 max_scrolls = 10
                
#                 while len(captured_requests) < min_requests and scroll_count < max_scrolls:
#                     # page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
#                     try: 
#                         button = page.query_selector('xpath=/html/body/div[1]/div[2]/main/aside/div/div[2]/button')
#                         if button and not page.get_by_role("button", name="Skip").is_visible():
#                             button.click() 
#                         time.sleep(3)

#                         if page.get_by_role("button", name="Refresh").is_visible():
#                             page.get_by_role("button", name="Refresh").click()

#                         if page.get_by_role("button", name="Skip").is_visible():
#                             page.get_by_role("button", name="Skip").click()
                        
#                     except Exception as e: 
#                         pass
#                     scroll_count += 1
#                     print(f"   Scroll {scroll_count}: {len(captured_requests)} recommend/item_list requests so far...")
#                     time.sleep(2)
                
#                 print(f"\n4. Total recommend/item_list requests captured: {len(captured_requests)}")
                
#                 if len(captured_requests) == 0:
#                     print("\n✗ No API requests were captured!")
#                     return False
                
#                 if len(captured_requests) < min_requests:
#                     print(f"\n⚠️  Warning: Only captured {len(captured_requests)} requests (wanted {min_requests})")
#                     print("   Using the last one anyway...")
                
#                 # Use the LAST request (most recent one)
#                 selected_request = captured_requests[-1]
#                 captured_url = selected_request['url']
#                 captured_headers = selected_request['headers']
#                 print("captured url: ", captured_url)
#                 print("captured headers: ", captured_headers)
                
#                 print(f"\n5. Selected request #{selected_request['number']} (the last one)")
                
#                 # Get cookies from browser
#                 browser_cookies = context.cookies()
#                 self.cookies = {cookie['name']: cookie['value'] for cookie in browser_cookies}
                
#                 print(f"\n6. Extracted {len(self.cookies)} cookies from browser:")
#                 print("   " + "-" * 66)
                
#                 # Print ALL cookies with FULL values
#                 for name, value in sorted(self.cookies.items()):
#                     print(f"   {name}: {value}")
                
#                 print("   " + "-" * 66)
                
#                 # Parse the captured URL to get all parameters
#                 print(f"\n7. Parsing API request URL...")
#                 parsed = urlparse(captured_url)
#                 self.api_params = parse_qs(parsed.query)


#                 print("="*10)
#                 print(self.api_params)
#                 print("="*10)

                
#                 # Convert single-item lists to strings
#                 for key, value in self.api_params.items():
#                     if isinstance(value, list) and len(value) == 1:
#                         self.api_params[key] = value[0]
                
#                 print(f"   ✓ Captured {len(self.api_params)} parameters from URL")
                
#                 # Display ALL captured parameters with FULL values
#                 print(f"\n8. All captured parameters (FULL VALUES):")
#                 print("   " + "-" * 66)
                
#                 param_index = 1
#                 for key in sorted(self.api_params.keys()):
#                     value = self.api_params[key]
#                     print(f"   {param_index:2}. {key}")
#                     print(f"       {value}")
#                     print()
#                     param_index += 1
                
#                 print("   " + "-" * 66)
                
#                 # Store headers
#                 self.headers = captured_headers
                
#                 print(f"\n9. Captured {len(self.headers)} request headers (FULL VALUES):")
#                 print("   " + "-" * 66)
                
#                 for name, value in sorted(self.headers.items()):
#                     print(f"   {name}: {value}")
                
#                 print("   " + "-" * 66)
                
#                 # Verify we have critical parameters
#                 print(f"\n10. Verifying critical parameters:")
#                 critical = ['device_id', 'msToken', 'X-Bogus', 'X-Gnarly', 'odinId', 'aid', 'region']
#                 all_found = True
                
#                 for param in critical:
#                     if param in self.api_params:
#                         val = self.api_params[param]
#                         print(f"   ✓ {param}:")
#                         print(f"     {val}")
#                     else:
#                         print(f"   ✗ {param}: NOT FOUND")
#                         all_found = False
                
#                 if not all_found:
#                     print("\n⚠️  Warning: Some critical parameters are missing!")
#                     print("   This might not work correctly.")
#                 else:
#                     print("\n✓ All critical parameters found!")
                
#                 print("\n" + "=" * 70)
#                 print(f"✓ Successfully captured request #{selected_request['number']}")
#                 print("=" * 70)
                
#                 return True
                
#             except Exception as e:
#                 print(f"\n✗ Error: {e}")
#                 import traceback
#                 traceback.print_exc()
#                 return False
#             finally:
#                 # time.sleep(1000)
#                 browser.close()
    
#     def get_cookies(self) -> Dict[str, str]:
#         """Get cookies from captured session"""
#         if self.cookies is None:
#             raise Exception("Cookies not initialized. Call get_fresh_session_data() first.")
#         return self.cookies
    
#     def get_headers(self) -> Dict[str, str]:
#         """Get headers from captured session"""
#         if self.headers is None:
#             raise Exception("Headers not initialized. Call get_fresh_session_data() first.")
#         return self.headers

#     def build_api_url(self, count: int = 6) -> str:
#         """Build API URL using captured parameters"""
#         base_url = 'https://www.tiktok.com/api/recommend/item_list/'

#         if not self.api_params:
#             raise Exception("API parameters not initialized. Call get_fresh_session_data() first.")

#         # Copy all parameters
#         params = self.api_params.copy()
        
#         # Update dynamic values
#         params['count'] = str(count)
#         params['focus_state'] = 'true'
#         params['is_page_visible'] = 'true'
#         params['WebIdLastTime'] = str(int(time.time()))
        
#         # Separate the tokens that go at the end
#         ms_token = params.pop('msToken', '')
#         x_bogus = params.pop('X-Bogus', '')
#         x_gnarly = params.pop('X-Gnarly', '')
        
#         # Build query string
#         query = urlencode(params, quote_via=quote)

#         print("final query: ", query)
        
#         # Construct full URL
#         url = f"{base_url}?{query}"
        
#         if ms_token:
#             url += f"&msToken={ms_token}"
#         if x_bogus:
#             url += f"&X-Bogus={x_bogus}"
#         if x_gnarly:
#             url += f"&X-Gnarly={x_gnarly}"


#         print("final url: ", url)
        
#         return url
    
#     def save_video_item(self, item: Dict[str, Any]):
#         """Save video item to file"""
#         try:
#             video_id = item.get('id')
#             if not video_id:
#                 return
            
#             filename = f"{self.output_dir}/{video_id}.json"
            
#             with open(filename, 'w', encoding='utf-8') as f:
#                 json.dump(item, f, indent=2, ensure_ascii=False)
            
#         except Exception as e:
#             print(f"Error saving video: {e}")
    
#     def process_accounts(self, items: List[Dict[str, Any]]):
#         """Process accounts and queue for scraping"""
#         for item in items:
#             try:
#                 author = item.get('author', {})
#                 unique_id = author.get('uniqueId')
                
#                 if unique_id:
#                     if not self.redis_client.sismember("scraped_usernames", unique_id):
#                         celery_app.send_task('tasks.scrape_profile', args=[unique_id])
#                         print(f"  ✓ Queued: {unique_id}")
#                         self.last_new_account_time = time.time()
#                     else:
#                         print(f"  ⊗ Skipped: {unique_id} (already scraped)")
                        
#             except Exception as e:
#                 print(f"  ✗ Error: {e}")
    
#     def fetch_fyp_videos(self) -> Optional[List[Dict[str, Any]]]:
#         """Fetch videos from FYP API"""
#         try:
#             url = self.build_api_url(count=6)
#             cookies = self.get_cookies()
#             headers = self.get_headers()
            
#             print(f"\n🌐 Making API request...")
#             print(f"   URL params: {len(self.api_params)}")
#             print(f"   Cookies: {len(cookies)}")
#             print(f"   Headers: {len(headers)}")
            
#             # Get proxy
#             # proxy_kwargs = self.proxy_manager.get_requests_kwargs(ProxyManager.PROXY_TYPE_RESIDENTIAL)
            
#             response = requests.get(url, cookies=cookies, headers=headers, timeout=30, proxies=get_datacenter_proxy())
            
#             print(f"   Response Status: {response.status_code}")
            
#             if response.status_code != 200:
#                 print(f"   ✗ Error response:")
#                 print(f"   {response.text[:500]}")
#                 return None
            
#             data = response.json()
            
#             if 'itemList' in data and data['itemList']:
#                 print(f"   ✓ Successfully got {len(data['itemList'])} videos!")
#                 return data['itemList']
#             else:
#                 print(f"   ⊗ No videos in response")
#                 print(f"   Response keys: {list(data.keys())}")
#                 if 'status_msg' in data:
#                     print(f"   Status message: {data['status_msg']}")
#                 if 'status_code' in data:
#                     print(f"   Status code: {data['status_code']}")
#                 return None
                
#         except Exception as e:
#             print(f"   ✗ Error: {e}")
#             import traceback
#             traceback.print_exc()
#             return None
    
#     def refresh_session_if_needed(self, iteration: int, refresh_interval: int = 50):
#         """Refresh session periodically"""
#         if iteration > 0 and iteration % refresh_interval == 0:
#             print(f"\n{'='*70}")
#             print(f"Refreshing session (iteration {iteration})...")
#             print(f"{'='*70}")
#             self.get_fresh_session_data()
    
#     def run(self, max_iterations: Optional[int] = None, delay: int = 5, refresh_interval: int = 50):
#         """Run the scraper"""
#         print(f"\n{'='*70}")
#         print(f"{'TikTok FYP Scraper':^70}")
#         print(f"{'='*70}")
        
#         # Get initial session data (wait for at least 5 requests)
#         if not self.get_fresh_session_data(min_requests=5):
#             print("\n✗ Failed to capture session data. Exiting...")
#             return
        
#         print(f"\n{'='*70}")
#         print(f"{'Starting Scraping Loop':^70}")
#         print(f"{'='*70}\n")
        
#         iteration = 0
        
#         while True:
#             if max_iterations and iteration >= max_iterations:
#                 print(f"\nReached max iterations: {max_iterations}")
#                 break
            
#             self.refresh_session_if_needed(iteration, refresh_interval)
            
#             if time.time() - self.last_new_account_time > 300:
#                 print("\n⏱️  Timeout: No new accounts in 5 minutes")
#                 sys.exit(0)
            
#             print(f"\n{'='*70}")
#             print(f"  Iteration {iteration + 1}")
#             print(f"{'='*70}")
            
#             items = self.fetch_fyp_videos()
            
#             if items:
#                 print(f"\n📝 Processing accounts:")
#                 self.process_accounts(items)
#             else:
#                 print(f"\n⚠️  No videos fetched - will retry next iteration")
            
#             iteration += 1
#             print(f"\n⏳ Waiting {delay} seconds before next iteration...\n")
#             time.sleep(delay)



# import redis
# import json
# import time
# import os
# import sys
# import argparse
# from typing import Optional, Dict, Any, List
# from urllib.parse import urlencode, quote, urlparse, parse_qs
# from pathlib import Path
# from dotenv import load_dotenv
# from celery import Celery
# from playwright.sync_api import sync_playwright
# from curl_cffi import requests  # NOT the same as pip requests!
# from collections import OrderedDict

# # Load .env from parent directory
# env_path = Path(__file__).parent.parent / '.env'
# load_dotenv(dotenv_path=env_path)

# sys.path.append(str(Path(__file__).parent.parent / 'shared'))
# from storage import upload_file
# from proxy import ProxyManager

# # Initialize Celery connection for sending tasks
# celery_app = Celery(
#     'tiktok_scraper',
#     broker=f"redis://{os.getenv('REDIS_HOST', 'localhost')}:{os.getenv('REDIS_PORT', 6379)}/0"
# )


# class TikTokFYPScraper:
#     """TikTok For You Page scraper using the private API"""
    
#     def __init__(
#         self,
#         redis_client: redis.Redis,
#         output_dir: str = "tiktok_video_metadata"
#     ):
#         self.redis_client = redis_client
#         self.output_dir = output_dir
#         self.last_new_account_time = time.time()
#         self.proxy_manager = ProxyManager()
        
#         # Will be set by get_fresh_session_data()
#         self.cookies = None
#         self.headers = None
#         self.api_params = {}
        
#         self._setup_output_directory()
        
#     def _setup_output_directory(self):
#         """Create output directory if it doesn't exist"""
#         if not os.path.exists(self.output_dir):
#             os.makedirs(self.output_dir)
    
#     def get_fresh_session_data(self, min_requests: int = 5):
#         """
#         Use Playwright to capture a working API request to 
#         https://www.tiktok.com/api/recommend/item_list/
#         Waits for multiple requests and uses the last one
        
#         Args:
#             min_requests: Minimum number of API requests to wait for before capturing
#         """
#         print("=" * 70)
#         print("Capturing TikTok FYP API request using Playwright...")
#         print("=" * 70)
        
#         with sync_playwright() as p:
#             browser = p.chromium.launch(headless=True)
            
#             context = browser.new_context(
#                 viewport={'width': 1920, 'height': 1080},
#                 user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
#                 locale='en-US',
#                 timezone_id='America/New_York'
#             )
            
#             page = context.new_page()
            
#             # Track all requests to the recommend/item_list endpoint
#             captured_requests = []
            
#             def handle_request(request):
#                 # Only count requests to recommend/item_list
#                 if 'api/recommend/item_list/' in request.url:
#                     request_num = len(captured_requests) + 1
#                     captured_requests.append({
#                         'url': request.url,
#                         'headers': request.headers,
#                         'number': request_num
#                     })
#                     print(f"   ✓ Captured recommend/item_list request #{request_num}")
            
#             page.on('request', handle_request)
            
#             try:
#                 print("\n1. Navigating to TikTok For You Page...")
#                 page.goto('https://www.tiktok.com/foryou', wait_until='domcontentloaded', timeout=60000)
                
#                 print(f"\n2. Waiting for at least {min_requests} recommend/item_list requests...")
#                 time.sleep(3)
                
#                 print("\n3. Scrolling to trigger more API requests...")
#                 # Scroll until we have enough requests
#                 scroll_count = 0
#                 max_scrolls = 10
                
#                 while len(captured_requests) < min_requests and scroll_count < max_scrolls:
#                     page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
#                     scroll_count += 1
#                     print(f"   Scroll {scroll_count}: {len(captured_requests)} recommend/item_list requests so far...")
#                     time.sleep(2)
                
#                 print(f"\n4. Total recommend/item_list requests captured: {len(captured_requests)}")
                
#                 if len(captured_requests) == 0:
#                     print("\n✗ No API requests were captured!")
#                     return False
                
#                 if len(captured_requests) < min_requests:
#                     print(f"\n⚠️  Warning: Only captured {len(captured_requests)} requests (wanted {min_requests})")
#                     print("   Using the last one anyway...")
                
#                 # Use the LAST request (most recent one)
#                 selected_request = captured_requests[-1]
#                 captured_url = selected_request['url']
#                 captured_headers = selected_request['headers']

#                 print("captured url: ", captured_url)
#                 print("captured headers: ", captured_headers)
                
#                 print(f"\n5. Selected request #{selected_request['number']} (the last one)")
                
#                 # Get cookies from browser
#                 browser_cookies = context.cookies()
#                 self.cookies = {cookie['name']: cookie['value'] for cookie in browser_cookies}
                
#                 print(f"\n6. Extracted {len(self.cookies)} cookies from browser:")
#                 print("   " + "-" * 66)
                
#                 # Print important cookies with FULL values
#                 important_cookies = ['ttwid', 'msToken', 'odin_tt', 'tt_chain_token', 
#                                    'sid_tt', 'sessionid', 'tt_csrf_token']
#                 for name in important_cookies:
#                     if name in self.cookies:
#                         print(f"   {name}: {self.cookies[name]}")
                
#                 print("   " + "-" * 66)
                
#                 # Parse the captured URL to get all parameters
#                 print(f"\n7. Parsing API request URL...")
#                 parsed = urlparse(captured_url)
#                 self.api_params = parse_qs(parsed.query)
                
#                 # Convert single-item lists to strings
#                 for key, value in self.api_params.items():
#                     if isinstance(value, list) and len(value) == 1:
#                         self.api_params[key] = value[0]
                
#                 print(f"   ✓ Captured {len(self.api_params)} parameters from URL")
                
#                 # Display critical parameters with FULL values
#                 print(f"\n8. Critical captured parameters (FULL VALUES):")
#                 print("   " + "-" * 66)
                
#                 critical_params = ['device_id', 'msToken', 'X-Bogus', 'X-Gnarly', 'odinId', 
#                                  'aid', 'region', 'WebIdLastTime']
                
#                 for param in critical_params:
#                     if param in self.api_params:
#                         value = self.api_params[param]
#                         print(f"   {param}:")
#                         print(f"   {value}")
#                         print()
                
#                 print("   " + "-" * 66)
                
#                 # Store headers
#                 self.headers = captured_headers
                
#                 print(f"\n9. Captured {len(self.headers)} request headers")
                
#                 # Show important headers
#                 important_headers = ['user-agent', 'referer', 'accept-language', 
#                                    'sec-ch-ua', 'sec-ch-ua-platform', 'sec-ch-ua-mobile']
#                 print("   Important headers:")
#                 for name in important_headers:
#                     if name in self.headers:
#                         print(f"   {name}: {self.headers[name]}")
                
#                 # Verify we have critical parameters
#                 print(f"\n10. Verification:")
#                 critical = ['device_id', 'msToken', 'X-Bogus', 'X-Gnarly', 'odinId', 'aid']
#                 missing = [p for p in critical if p not in self.api_params]
                
#                 if missing:
#                     print(f"   ✗ Missing parameters: {', '.join(missing)}")
#                     return False
#                 else:
#                     print(f"   ✓ All critical parameters present!")
                
#                 print("\n" + "=" * 70)
#                 print(f"✓ Successfully captured request #{selected_request['number']}")
#                 print("=" * 70)
                
#                 return True
                
#             except Exception as e:
#                 print(f"\n✗ Error: {e}")
#                 import traceback
#                 traceback.print_exc()
#                 return False
#             finally:
#                 # time.sleep(1000)
#                 browser.close()
    
#     def get_cookies(self) -> Dict[str, str]:
#         """Get cookies from captured session"""
#         if self.cookies is None:
#             raise Exception("Cookies not initialized. Call get_fresh_session_data() first.")
#         return self.cookies
    
#     def get_headers(self) -> Dict[str, str]:
#         """Get headers from captured session"""
#         if self.headers is None:
#             raise Exception("Headers not initialized. Call get_fresh_session_data() first.")
#         return self.headers

#     # def build_api_url(self, count: int = 6) -> str:
#     #     """Build API URL using captured parameters"""
#     #     base_url = 'https://www.tiktok.com/api/recommend/item_list/'

#     #     if not self.api_params:
#     #         raise Exception("API parameters not initialized. Call get_fresh_session_data() first.")

#     #     # Copy all parameters
#     #     params = self.api_params.copy()
        
#     #     # Update dynamic values
#     #     params['count'] = str(count)
#     #     params['focus_state'] = 'true'
#     #     params['is_page_visible'] = 'true'
#     #     params['WebIdLastTime'] = str(int(time.time()))
        
#     #     # Separate the tokens that go at the end
#     #     ms_token = params.pop('msToken', '')
#     #     x_bogus = params.pop('X-Bogus', '')
#     #     x_gnarly = params.pop('X-Gnarly', '')
        
#     #     # Build query string
#     #     query = urlencode(params, quote_via=quote)
        
#     #     # Construct full URL
#     #     url = f"{base_url}?{query}"
        
#     #     if ms_token:
#     #         url += f"&msToken={ms_token}"
#     #     if x_bogus:
#     #         url += f"&X-Bogus={x_bogus}"
#     #     if x_gnarly:
#     #         url += f"&X-Gnarly={x_gnarly}"
        
#     #     return url


#     def build_api_url(self, count: int = 6) -> str:
#         """Rebuild TikTok API URL without breaking param order/signature"""
#         base_url = "https://www.tiktok.com/api/recommend/item_list/"

#         if not self.api_params:
#             raise Exception("API parameters not initialized. Call get_fresh_session_data() first.")

#         # make a shallow copy preserving insertion order
#         params = OrderedDict(self.api_params)

#         # update lightweight dynamic fields only (don’t touch signature keys)
#         params["count"] = str(count)
#         params["focus_state"] = "true"
#         params["is_page_visible"] = "true"
#         params["WebIdLastTime"] = str(int(time.time()))

#         # ensure empty but required keys exist
#         if "priority_region" not in params:
#             params["priority_region"] = ""
#         if "referer" not in params:
#             params["referer"] = ""

#         # extract tokens but re-insert them in original order later
#         ms_token = params.get("msToken", "")
#         x_bogus = params.get("X-Bogus", "")
#         x_gnarly = params.get("X-Gnarly", "")

#         # build query preserving order — don’t sort alphabetically
#         ordered_query = "&".join(
#             f"{quote(str(k))}={quote(str(v))}" for k, v in params.items() if v != None
#         )

#         # append tokens exactly as browser does
#         if ms_token:
#             ordered_query += f"&msToken={ms_token}"
#         if x_bogus:
#             ordered_query += f"&X-Bogus={x_bogus}"
#         if x_gnarly:
#             ordered_query += f"&X-Gnarly={x_gnarly}"

#         full_url = f"{base_url}?{ordered_query}"
#         return full_url
    
#     def save_video_item(self, item: Dict[str, Any]):
#         """Save video item to file"""
#         try:
#             video_id = item.get('id')
#             if not video_id:
#                 return
            
#             filename = f"{self.output_dir}/{video_id}.json"
            
#             with open(filename, 'w', encoding='utf-8') as f:
#                 json.dump(item, f, indent=2, ensure_ascii=False)
            
#         except Exception as e:
#             print(f"Error saving video: {e}")
    
#     def process_accounts(self, items: List[Dict[str, Any]]):
#         """Process accounts and queue for scraping"""
#         for item in items:
#             try:
#                 author = item.get('author', {})
#                 unique_id = author.get('uniqueId')
                
#                 if unique_id:
#                     if not self.redis_client.sismember("scraped_usernames", unique_id):
#                         celery_app.send_task('tasks.scrape_profile', args=[unique_id])
#                         print(f"  ✓ Queued: {unique_id}")
#                         self.last_new_account_time = time.time()
#                     else:
#                         print(f"  ⊗ Skipped: {unique_id} (already scraped)")
                        
#             except Exception as e:
#                 print(f"  ✗ Error: {e}")
    
#     def fetch_fyp_videos(self) -> Optional[List[Dict[str, Any]]]:
#         """Fetch videos from FYP API using curl_cffi"""
#         try:
#             url = self.build_api_url(count=6)
#             cookies = self.get_cookies()
#             headers = self.get_headers()
            
#             print(f"\n🌐 Making API request with curl_cffi...")
#             print(f"   URL params: {len(self.api_params)}")
#             print(f"   Cookies: {len(cookies)}")
#             print(f"   Headers: {len(headers)}")
            
#             # Get proxy configuration
#             # proxy_config = self.proxy_manager.get_proxy_config(ProxyManager.PROXY_TYPE_DATACENTER)
            
#             # Make request using curl_cffi with Chrome impersonation
#             print("url to follow: ", url)
#             print("headers: ", headers)
#             response = requests.get(
#                 url,
#                 headers=headers,
#                 # cookies=cookies,
#                 impersonate="chrome131",  # Impersonate Chrome 131
#                 # proxies=proxy_config,
#                 timeout=30
#             )
            
#             print(f"   Response Status: {response.status_code}")
#             print(f"   Response Length: {len(response.content)} bytes")
            
#             if response.status_code != 200:
#                 print(f"   ✗ Error response:")
#                 print(f"   {response.text[:500]}")
#                 return None
            
#             data = response.json()
            
#             if 'itemList' in data and data['itemList']:
#                 print(f"   ✓ Successfully got {len(data['itemList'])} videos!")
#                 return data['itemList']
#             else:
#                 print(f"   ⊗ No videos in response")
#                 print(f"   Response keys: {list(data.keys())}")
#                 if 'status_msg' in data:
#                     print(f"   Status message: {data['status_msg']}")
#                 if 'status_code' in data:
#                     print(f"   Status code: {data['status_code']}")
#                 print(f"   Response preview: {response.text[:300]}")
#                 return None
                
#         except Exception as e:
#             print(f"   ✗ Error: {e}")
#             import traceback
#             traceback.print_exc()
#             return None
    
#     def refresh_session_if_needed(self, iteration: int, refresh_interval: int = 50):
#         """Refresh session periodically"""
#         if iteration > 0 and iteration % refresh_interval == 0:
#             print(f"\n{'='*70}")
#             print(f"Refreshing session (iteration {iteration})...")
#             print(f"{'='*70}")
#             self.get_fresh_session_data()
    
#     def run(self, max_iterations: Optional[int] = None, delay: int = 5, refresh_interval: int = 50):
#         """Run the scraper"""
#         print(f"\n{'='*70}")
#         print(f"{'TikTok FYP Scraper':^70}")
#         print(f"{'='*70}")
        
#         # Get initial session data (wait for at least 5 requests)
#         if not self.get_fresh_session_data(min_requests=5):
#             print("\n✗ Failed to capture session data. Exiting...")
#             return
        
#         print(f"\n{'='*70}")
#         print(f"{'Starting Scraping Loop':^70}")
#         print(f"{'='*70}\n")
        
#         iteration = 0
        
#         while True:
#             if max_iterations and iteration >= max_iterations:
#                 print(f"\nReached max iterations: {max_iterations}")
#                 break
            
#             self.refresh_session_if_needed(iteration, refresh_interval)
            
#             if time.time() - self.last_new_account_time > 300:
#                 print("\n⏱️  Timeout: No new accounts in 5 minutes")
#                 sys.exit(0)
            
#             print(f"\n{'='*70}")
#             print(f"  Iteration {iteration + 1}")
#             print(f"{'='*70}")
            
#             items = self.fetch_fyp_videos()
            
#             if items:
#                 print(f"\n📝 Processing accounts:")
#                 self.process_accounts(items)
#             else:
#                 print(f"\n⚠️  No videos fetched - will retry next iteration")
            
#             iteration += 1
#             print(f"\n⏳ Waiting {delay} seconds before next iteration...\n")
#             time.sleep(delay)




# import redis
# import json
# import time
# import os
# import sys
# import argparse
# from typing import Optional, Dict, Any, List
# from urllib.parse import urlencode, quote, urlparse, parse_qsl
# from pathlib import Path
# from dotenv import load_dotenv
# from celery import Celery
# from playwright.sync_api import sync_playwright
# from curl_cffi import requests  # NOT the same as pip requests!
# from collections import OrderedDict

# # Load .env from parent directory
# env_path = Path(__file__).parent.parent / '.env'
# load_dotenv(dotenv_path=env_path)

# sys.path.append(str(Path(__file__).parent.parent / 'shared'))
# from storage import upload_file
# from proxy import ProxyManager

# # Initialize Celery connection for sending tasks
# celery_app = Celery(
#     'tiktok_scraper',
#     broker=f"redis://{os.getenv('REDIS_HOST', 'localhost')}:{os.getenv('REDIS_PORT', 6379)}/0"
# )


# class TikTokFYPScraper:
#     """TikTok For You Page scraper using the private API"""

#     def __init__(
#         self,
#         redis_client: redis.Redis,
#         output_dir: str = "tiktok_video_metadata"
#     ):
#         self.redis_client = redis_client
#         self.output_dir = output_dir
#         self.last_new_account_time = time.time()
#         self.proxy_manager = ProxyManager()

#         self.cookies = None
#         self.headers = None
#         self.api_params = {}
#         self.api_params_items = None

#         self._setup_output_directory()

#     def _setup_output_directory(self):
#         if not os.path.exists(self.output_dir):
#             os.makedirs(self.output_dir)

#     def get_fresh_session_data(self, min_requests: int = 5):
#         print("=" * 70)
#         print("Capturing TikTok FYP API request using Playwright...")
#         print("=" * 70)

#         with sync_playwright() as p:
#             browser = p.chromium.launch(headless=True)

#             context = browser.new_context(
#                 viewport={'width': 1920, 'height': 1080},
#                 user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
#                 locale='en-US',
#                 timezone_id='America/New_York'
#             )

#             page = context.new_page()
#             captured_requests = []

#             def handle_request(request):
#                 if 'api/recommend/item_list/' in request.url:
#                     captured_requests.append({
#                         'url': request.url,
#                         'headers': request.headers
#                     })
#                     print(f"   ✓ Captured recommend/item_list request #{len(captured_requests)}")

#             page.on('request', handle_request)

#             try:
#                 page.goto('https://www.tiktok.com/foryou', wait_until='domcontentloaded', timeout=60000)
#                 time.sleep(3)

#                 scroll_count = 0
#                 while len(captured_requests) < min_requests and scroll_count < 10:
#                     page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
#                     scroll_count += 1
#                     print(f"   Scroll {scroll_count}: {len(captured_requests)} requests...")
#                     time.sleep(2)

#                 if not captured_requests:
#                     print("✗ No API requests captured")
#                     return False

#                 selected_request = captured_requests[-1]
#                 captured_url = selected_request['url']
#                 captured_headers = selected_request['headers']

#                 print("captured url: ", captured_url)
#                 print("captured headers: ", captured_headers)

#                 browser_cookies = context.cookies()
#                 self.cookies = {cookie['name']: cookie['value'] for cookie in browser_cookies}

#                 print("\nParsing API request URL (order-preserving)...")
#                 parsed = urlparse(captured_url)
#                 pairs = parse_qsl(parsed.query, keep_blank_values=True)

#                 self.api_params_items = list(pairs)
#                 self.api_params = OrderedDict()
#                 for k, v in pairs:
#                     if k not in self.api_params:
#                         self.api_params[k] = v

#                 print(f"✓ Captured {len(self.api_params)} unique parameters from URL (order preserved)")

#                 self.headers = captured_headers
#                 print(f"✓ Captured {len(self.headers)} headers")

#                 return True

#             except Exception as e:
#                 print(f"✗ Error: {e}")
#                 import traceback
#                 traceback.print_exc()
#                 return False
#             finally:
#                 browser.close()

#     def get_cookies(self) -> Dict[str, str]:
#         if self.cookies is None:
#             raise Exception("Cookies not initialized. Call get_fresh_session_data() first.")
#         return self.cookies

#     def get_headers(self) -> Dict[str, str]:
#         if self.headers is None:
#             raise Exception("Headers not initialized. Call get_fresh_session_data() first.")
#         return self.headers

#     def build_api_url(self, count: int = 6) -> str:
#         """
#         Rebuild TikTok API URL exactly like the browser:
#         - preserve original parameter ORDER
#         - do NOT duplicate signature params
#         - encode '/' as %2F
#         """
#         base_url = "https://www.tiktok.com/api/recommend/item_list/"

#         if not getattr(self, "api_params_items", None):
#             raise Exception("API parameters not initialized. Call get_fresh_session_data() first.")

#         pairs = list(self.api_params_items)

#         def set_or_replace(pairs_list, key, value):
#             for i, (k, _) in enumerate(pairs_list):
#                 if k == key:
#                     pairs_list[i] = (key, str(value))
#                     return
#             pairs_list.append((key, str(value)))

#         set_or_replace(pairs, "count", str(count))
#         set_or_replace(pairs, "focus_state", "true")
#         set_or_replace(pairs, "is_page_visible", "true")
#         set_or_replace(pairs, "WebIdLastTime", str(int(time.time())))

#         sig_keys = {"msToken", "X-Bogus", "X-Gnarly"}
#         found_sig = {k: False for k in sig_keys}
#         deduped = []

#         for k, v in pairs:
#             if k in sig_keys:
#                 if not found_sig[k]:
#                     deduped.append((k, v))
#                     found_sig[k] = True
#             else:
#                 deduped.append((k, v))

#         pairs = deduped

#         def enc(k: str, v: str) -> str:
#             # do not escape '/' in msToken, X-Bogus, X-Gnarly
#             if k in ("msToken", "X-Bogus", "X-Gnarly"):
#                 return f"{quote(k, safe='')}={quote(v, safe='/=')}"
#             return f"{quote(k, safe='')}={quote(v, safe='')}"

#         query = "&".join(enc(k, v) for k, v in pairs)
#         return f"{base_url}?{query}"

#     def save_video_item(self, item: Dict[str, Any]):
#         try:
#             video_id = item.get('id')
#             if not video_id:
#                 return

#             filename = f"{self.output_dir}/{video_id}.json"
#             with open(filename, 'w', encoding='utf-8') as f:
#                 json.dump(item, f, indent=2, ensure_ascii=False)
#         except Exception as e:
#             print(f"Error saving video: {e}")

#     def process_accounts(self, items: List[Dict[str, Any]]):
#         for item in items:
#             try:
#                 author = item.get('author', {})
#                 unique_id = author.get('uniqueId')

#                 if unique_id:
#                     if not self.redis_client.sismember("scraped_usernames", unique_id):
#                         celery_app.send_task('tasks.scrape_profile', args=[unique_id])
#                         print(f"  ✓ Queued: {unique_id}")
#                         self.last_new_account_time = time.time()
#                     else:
#                         print(f"  ⊗ Skipped: {unique_id} (already scraped)")

#             except Exception as e:
#                 print(f"  ✗ Error: {e}")

#     def fetch_fyp_videos(self) -> Optional[List[Dict[str, Any]]]:
#         try:
#             url = self.build_api_url(count=6)
#             cookies = self.get_cookies()
#             headers = self.get_headers()

#             print(f"\n🌐 Making API request with curl_cffi...")
#             print("url to follow: ", url)
#             print("headers: ", headers)

#             response = requests.get(
#                 url,
#                 headers=headers,
#                 impersonate="chrome131",
#                 timeout=30
#             )

#             print(f"Response Status: {response.status_code}")
#             if response.status_code != 200:
#                 print(f"✗ Error: {response.text[:500]}")
#                 return None

#             data = response.json()
#             if 'itemList' in data and data['itemList']:
#                 print(f"✓ Got {len(data['itemList'])} videos")
#                 return data['itemList']
#             else:
#                 print("⊗ No videos in response")
#                 print(f"Response keys: {list(data.keys())}")
#                 return None

#         except Exception as e:
#             print(f"✗ Error: {e}")
#             import traceback
#             traceback.print_exc()
#             return None

#     def refresh_session_if_needed(self, iteration: int, refresh_interval: int = 50):
#         if iteration > 0 and iteration % refresh_interval == 0:
#             print(f"\nRefreshing session (iteration {iteration})...")
#             self.get_fresh_session_data()

#     def run(self, max_iterations: Optional[int] = None, delay: int = 5, refresh_interval: int = 50):
#         if not self.get_fresh_session_data(min_requests=5):
#             print("✗ Failed to capture session data.")
#             return

#         iteration = 0
#         while True:
#             if max_iterations and iteration >= max_iterations:
#                 print(f"Reached max iterations: {max_iterations}")
#                 break

#             self.refresh_session_if_needed(iteration, refresh_interval)

#             if time.time() - self.last_new_account_time > 300:
#                 print("⏱️  Timeout: No new accounts in 5 minutes")
#                 sys.exit(0)

#             print(f"\nIteration {iteration + 1}")
#             items = self.fetch_fyp_videos()

#             if items:
#                 self.process_accounts(items)
#             else:
#                 print("⚠️  No videos fetched")

#             iteration += 1
#             time.sleep(delay)



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


class TikTokFYPScraper:
    """TikTok For You Page scraper using the private API"""

    def __init__(self, redis_client: redis.Redis, output_dir: str = "tiktok_video_metadata"):
        self.redis_client = redis_client
        self.output_dir = output_dir
        self.last_new_account_time = time.time()
        self.proxy_manager = ProxyManager()

        self.cookies = None
        self.headers = None
        self.api_params = {}
        self.api_params_items = None

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def get_fresh_session_data(self, min_requests: int = 5):
        print("=" * 70)
        print("Capturing TikTok FYP API request using Playwright...")
        print("=" * 70)

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                locale='en-US',
                timezone_id='America/New_York'
            )
            page = context.new_page()
            captured_requests = []

            def handle_request(request):
                if 'api/recommend/item_list/' in request.url:
                    captured_requests.append({'url': request.url, 'headers': request.headers})
                    print(f"   ✓ Captured recommend/item_list request #{len(captured_requests)}")

            page.on('request', handle_request)

            try:
                page.goto('https://www.tiktok.com/foryou', wait_until='domcontentloaded', timeout=60000)
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

    def get_cookies(self) -> Dict[str, str]:
        if self.cookies is None:
            raise Exception("Cookies not initialized. Call get_fresh_session_data() first.")
        return self.cookies

    def get_headers(self) -> Dict[str, str]:
        if self.headers is None:
            raise Exception("Headers not initialized. Call get_fresh_session_data() first.")
        return self.headers

    def build_api_url(self, count: int = 6) -> str:
        """
        Build TikTok API URL preserving byte identity:
        - Preserve captured WebIdLastTime
        - Preserve order
        - Do not re-encode or change signature params
        """
        base_url = "https://www.tiktok.com/api/recommend/item_list/"

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

    def fetch_fyp_videos(self) -> Optional[List[Dict[str, Any]]]:
        try:
            url = self.build_api_url(count=6)
            cookies = self.get_cookies()
            headers = self.get_headers()

            print(f"\n🌐 Fetching FYP API...")
            print("url to follow:", url)
            print("headers:", headers)

            response = requests.get(
                url,
                headers=headers,
                impersonate="chrome131",
                timeout=30
            )

            print(f"Response Status: {response.status_code}")
            if response.status_code != 200:
                print("✗ Error:", response.text[:300])
                return None

            data = response.json()
            if "itemList" in data and data["itemList"]:
                print(f"✓ Got {len(data['itemList'])} videos.")
                return data["itemList"]
            else:
                print("⊗ No videos in response")
                return None

        except Exception as e:
            print("✗ Error:", e)
            import traceback
            traceback.print_exc()
            return None

    def process_accounts(self, items: List[Dict[str, Any]]):
        for item in items:
            try:
                author = item.get("author", {})
                unique_id = author.get("uniqueId")
                if unique_id and not self.redis_client.sismember("scraped_usernames", unique_id):
                    celery_app.send_task("tasks.scrape_profile", args=[unique_id])
                    print(f"✓ Queued: {unique_id}")
                    self.last_new_account_time = time.time()
                else:
                    print(f"⊗ Skipped: {unique_id}")
            except Exception as e:
                print("Error processing:", e)

    def run(self, max_iterations: Optional[int] = None, delay: int = 5):
        if not self.get_fresh_session_data(min_requests=5):
            print("✗ Failed to capture session data.")
            return

        iteration = 0
        while True:
            if max_iterations and iteration >= max_iterations:
                break

            items = self.fetch_fyp_videos()
            if items:
                self.process_accounts(items)
            else:
                print("⚠️ No videos fetched")

            iteration += 1
            time.sleep(delay)
