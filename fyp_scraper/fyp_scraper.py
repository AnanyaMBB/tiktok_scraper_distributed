import redis
import json
import time
import os
import sys
import requests
import argparse
from typing import Optional, Dict, Any, List
from urllib.parse import urlencode, quote 


class TikTokFYPScraper:
    """TikTok For You Page scraper using the private API"""
    
    def __init__(
        self,
        redis_client: redis.Redis,
        output_dir: str = "tiktok_video_metadata"
    ):
        self.redis_client = redis_client
        self.output_dir = output_dir
        self.last_new_account_time = time.time()
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
            'store-country-sign': 'MEIEDBKdqGvnG5UAo5FXbwQgAm15FzxCZRJzVE_IqmgWlnlT7svrenSYBbR9w-g-oRsEEF7CnPC1TU3oVf8kCi26MV4',
            'msToken': 'Xb5ISAL1qu4crHwjKKLRrctkVp1TEq5L-n_n90700NHS_cRZewdWtNn08cFvXpfj86NB79ISVgXL0ZJ4Ar5wbwp5QQsyafQl8i8Jocj24HK2v_F8llI3Jr3WmR1of_6wKdXt6rywsxWWStV_r-baiy_dnw==',
            'odin_tt': '55702be48b513482b777bcd6455e0453a917564e2ca5250690bf55a79a7e9972359024426402e79fb654913da3e1b60ab52fd8d6fbe071f3a91cafe0d0a83e3c',
            'passport_fe_beating_status': 'false',
            'perf_feed_cache': '{%22expireTimestamp%22:1762351200000%2C%22itemIds%22:[%227565222614025686285%22%2C%227553551072632147211%22%2C%227567781083329170701%22]}',
            'ttwid': '1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1762180132%7C03a7156af52f7028f1bd89d5799983d4e24445a7d55aec361f1c84fce271bbc0',
        }
        return cookies
    
    def get_headers(self) -> Dict[str, str]:
        """Get headers for API requests"""
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'priority': 'u=1, i',
            'referer': 'https://www.tiktok.com/',
            'sec-ch-ua': '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',
        }
        return headers

    def build_api_url(self, count: int = 6) -> str:
        base_url = 'https://www.tiktok.com/api/recommend/item_list/'

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
            'clientABVersions': '74800760,70508271,72437276,73720540,74250915,74393673,74446915,74465399,74465409,74536864,74609147,74627577,74632791,74674280,74676351,74679798,74686502,74700792,74703727,74711111,74733472,74746519,74746610,74757744,74767144,74767851,74782564,74792133,74793837,74798337,74798356,74808329,74810092,74811360,74819402,74824020,74872266,74882809,70138197,70156809,70405643,71057832,71200802,71381811,71516509,71803300,71962127,72360691,72408100,72854054,72892778,73004916,73171280,73208420,73989921,74276218,74844724',
            'cookie_enabled': 'true',
            'count': str(count),
            'coverFormat': '2',
            'cpu_core_number': '12',
            'dark_mode': 'false',
            'data_collection_enabled': 'true',
            'day_of_week': '1',
            'device_id': '7460149314773288494',
            'device_platform': 'web_pc',
            'device_score': '8.57',
            'device_type': 'web_h264',
            'enable_cache': 'false',
            'focus_state': 'true',
            'from_page': 'fyp',
            'history_len': '2',
            'isNonPersonalized': 'false',
            'is_fullscreen': 'false',
            'is_page_visible': 'true',
            'itemID': '',
            'language': 'en',
            'launch_mode': 'direct',
            'network': '10',
            'odinId': '7478784916198065170',
            'os': 'windows',
            'priority_region': 'KR',
            'pullType': '1',
            'referer': '',
            'region': 'KR',
            'screen_height': '1080',
            'screen_width': '1920',
            'showAboutThisAd': 'true',
            'showAds': 'true',
            'time_of_day': '23',
            'tz_name': 'Asia/Seoul',
            'video_encoding': '',
            'vv_count': '12529',
            'vv_count_fyp': '2637',
            'watchLiveLastTime': '1741102304984',
            'webcast_language': 'en',
            'window_height': '962',
            'window_width': '150',
        }

        # exclude msToken from urlencode to keep '=' unencoded
        ms_token = 'Xb5ISAL1qu4crHwjKKLRrctkVp1TEq5L-n_n90700NHS_cRZewdWtNn08cFvXpfj86NB79ISVgXL0ZJ4Ar5wbwp5QQsyafQl8i8Jocj24HK2v_F8llI3Jr3WmR1of_6wKdXt6rywsxWWStV_r-baiy_dnw=='
        x_bogus = 'DFSzsIVYt2tANH/ACPJVwimpF2W/'
        x_gnarly = (
            'Mw1bQHB/564boDbZQP6s-ShaK79iOfgOU57EoHgX55VO37v9-rSjMDEUveU9Nfm5dxJhESWUyRv4djcH4XUtOYukfRsLuySJRYRPMg37l9HL0XBOV0uTQJuCiwefkvLfYgShxDL-m543VJlr2-f2HHDjhsnNo6F10fQWHlSqptwrCQCKoyBctGFyOMd/cKJpCHGAvva4IxMPEQVXKqALpvG90JdQ4ERuMgAs11wKA97EXkbVCZigzSSJPsJFTwxkiF9SYENojM6LDiv2DEBH-1jU4pOll-gPUyLf0bY1IfEricLsZqdGwDDIhWCWS8EYYPz='
        )

        # Encode only safe params
        query = urlencode(params, quote_via=quote)

        # Append msToken and others manually (unencoded)
        return f"{base_url}?{query}&msToken={ms_token}&X-Bogus={x_bogus}&X-Gnarly={x_gnarly}"
    
    def save_video_item(self, item: Dict[str, Any]):
        """Save individual video item JSON to a file"""
        try:
            video_id = item.get('id')
            if not video_id:
                print("No video ID found, skipping save")
                return
            
            filename = f"{self.output_dir}/{video_id}.json"
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(item, f, indent=2, ensure_ascii=False)
            
            print(f"Saved video: {filename}")
            
        except Exception as e:
            print(f"Error saving video item: {e}")
    
    def process_accounts(self, items: List[Dict[str, Any]]):
        """Process accounts from video items and add to Redis queue"""
        for item in items:
            try:
                author = item.get('author', {})
                unique_id = author.get('uniqueId')
                
                if unique_id:
                    if not self.redis_client.sismember("scraped_usernames", unique_id):
                        self.redis_client.sadd("queued_usernames", unique_id)
                        print(f"Added {unique_id} to scraping queue")
                        self.last_new_account_time = time.time()
                        
            except Exception as e:
                print(f"Error processing account: {e}")
    
    def fetch_fyp_videos(self) -> Optional[List[Dict[str, Any]]]:
        """Fetch videos from the FYP API"""
        try:
            url = self.build_api_url(count=6)
            cookies = self.get_cookies()
            headers = self.get_headers()
            print(url)
            response = requests.get(url, cookies=cookies, headers=headers, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            
            if 'itemList' in data and data['itemList']:
                print(f"Fetched {len(data['itemList'])} videos from FYP")
                return data['itemList']
            else:
                print("No items found in FYP response")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Error fetching FYP videos: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
            return None
    
    def run(self, max_iterations: Optional[int] = None, delay: int = 5):
        """
        Run the FYP scraper continuously
        
        Args:
            max_iterations: Maximum number of iterations (None for infinite)
            delay: Delay in seconds between requests
        """
        print("Starting FYP scraper...")
        iteration = 0
        
        while True:
            # Check if we should stop
            if max_iterations and iteration >= max_iterations:
                print(f"Reached max iterations: {max_iterations}")
                break
            
            # Check for timeout (no new accounts in 5 minutes)
            if time.time() - self.last_new_account_time > 300:
                sys.exit("No new accounts found in the last 5 minutes. Exiting...")
            
            # Fetch videos
            items = self.fetch_fyp_videos()
            
            if items:
                # Save each video item as separate JSON file
                # for item in items:
                #     self.save_video_item(item)
                
                # Process accounts for queue
                self.process_accounts(items)
            
            iteration += 1
            print(f"Iteration {iteration} complete. Waiting {delay} seconds...")
            time.sleep(delay)