# # # # import os
# # # # import json
# # # # import time
# # # # import redis
# # # # import sys
# # # # from typing import Optional, Dict, Any
# # # # from urllib.parse import quote
# # # # from collections import OrderedDict
# # # # from pathlib import Path
# # # # from curl_cffi import requests
# # # # from dotenv import load_dotenv
# # # # from celery_config import celery_app

# # # # env_path = Path(__file__).parent.parent / ".env"
# # # # load_dotenv(dotenv_path=env_path)

# # # # sys.path.append(str(Path(__file__).parent.parent / "shared"))
# # # # from storage import upload_file
# # # # from proxy import ProxyManager


# # # # class TikTokProfileScraper:
# # # #     """TikTok Profile scraper using the private API"""

# # # #     def __init__(self, output_dir="tiktok_videos", session_file="profile_session.json"):
# # # #         self.output_dir = output_dir
# # # #         self.session_file = session_file
# # # #         self.proxy_manager = ProxyManager()
        
# # # #         # Session data
# # # #         self.cookies = None
# # # #         self.headers = None
# # # #         self.api_params_items = None
        
# # # #         self._setup_output_directory()
# # # #         self.load_session()

# # # #     def _setup_output_directory(self):
# # # #         os.makedirs(self.output_dir, exist_ok=True)

# # # #     def load_session(self):
# # # #         """Load TikTok session from file"""
# # # #         session_path = Path(__file__).parent / self.session_file
        
# # # #         if not session_path.exists():
# # # #             raise FileNotFoundError(
# # # #                 f"Session file not found: {self.session_file}\n"
# # # #                 f"Please run: python capture_session.py"
# # # #             )
        
# # # #         with open(session_path, "r", encoding="utf-8") as f:
# # # #             data = json.load(f)
        
# # # #         self.cookies = data["cookies"]
# # # #         self.headers = data["headers"]
# # # #         self.api_params_items = data["params"]
        
# # # #         print(f"✓ Loaded session from {self.session_file}")

# # # #     def build_api_url(self, sec_uid: str, cursor: int = 0, count: int = 16) -> str:
# # # #         """
# # # #         Build profile API URL preserving captured parameter order
# # # #         Only updates: secUid, cursor, count
# # # #         """
# # # #         base_url = "https://www.tiktok.com/api/post/item_list/"

# # # #         if not self.api_params_items:
# # # #             raise Exception("API parameters not initialized.")

# # # #         pairs = list(self.api_params_items)

# # # #         # Update only the necessary parameters
# # # #         def set_or_replace(pairs_list, key, value):
# # # #             for i, (k, _) in enumerate(pairs_list):
# # # #                 if k == key:
# # # #                     pairs_list[i] = (key, str(value))
# # # #                     return
# # # #             pairs_list.append((key, str(value)))

# # # #         set_or_replace(pairs, "secUid", sec_uid)
# # # #         set_or_replace(pairs, "cursor", str(cursor))
# # # #         set_or_replace(pairs, "count", str(count))

# # # #         # Deduplicate signature tokens
# # # #         sig_keys = {"msToken", "X-Bogus", "X-Gnarly"}
# # # #         seen = {k: False for k in sig_keys}
# # # #         deduped = []
# # # #         for k, v in pairs:
# # # #             if k in sig_keys:
# # # #                 if not seen[k]:
# # # #                     deduped.append((k, v))
# # # #                     seen[k] = True
# # # #             else:
# # # #                 deduped.append((k, v))
# # # #         pairs = deduped

# # # #         # Encode parameters
# # # #         def encode_pair(k, v):
# # # #             if k in sig_keys:
# # # #                 return f"{quote(k, safe='')}={quote(v, safe='/=')}"
# # # #             return f"{quote(k, safe='')}={quote(v, safe='')}"

# # # #         query = "&".join(encode_pair(k, v) for k, v in pairs)
# # # #         return f"{base_url}?{query}"

# # # #     def get_user_sec_uid(self, username: str) -> Optional[str]:
# # # #         """Get secUid from user profile page"""
# # # #         try:
# # # #             import re
            
# # # #             profile_url = f"https://www.tiktok.com/@{username}"
            
# # # #             response = requests.get(
# # # #                 profile_url,
# # # #                 impersonate="chrome131",
# # # #                 timeout=30
# # # #             )
            
# # # #             if response.status_code != 200:
# # # #                 print(f"✗ Failed to fetch profile: {response.status_code}")
# # # #                 return None

# # # #             match = re.search(r'"secUid":"(MS4wLjABAAAA[^"]+)"', response.text)
# # # #             if match:
# # # #                 sec_uid = match.group(1)
# # # #                 print(f"✓ Found secUid for @{username}")
# # # #                 return sec_uid

# # # #             print(f"✗ Could not find secUid for @{username}")
# # # #             return None

# # # #         except Exception as e:
# # # #             print(f"✗ Error getting secUid: {e}")
# # # #             return None

# # # #     def fetch_user_videos(self, username: str, sec_uid: str, cursor: int = 0) -> Optional[Dict[str, Any]]:
# # # #         """Fetch videos from user profile"""
# # # #         try:
# # # #             url = self.build_api_url(sec_uid, cursor)
            
# # # #             # Update referer header for this specific user
# # # #             headers = self.headers.copy()
# # # #             headers["referer"] = f"https://www.tiktok.com/@{username}"

# # # #             print(f"📡 Fetching @{username} (cursor={cursor})...")

# # # #             # Get proxy
# # # #             proxy_config = self.proxy_manager.get_proxy_config(ProxyManager.PROXY_TYPE_ROTATING)

# # # #             response = requests.get(
# # # #                 url,
# # # #                 headers=headers,
# # # #                 cookies=self.cookies,
# # # #                 impersonate="chrome131",
# # # #                 proxies=proxy_config,
# # # #                 timeout=30
# # # #             )

# # # #             if response.status_code != 200:
# # # #                 print(f"   ✗ Status {response.status_code}")
# # # #                 return None

# # # #             data = response.json()
            
# # # #             if 'itemList' in data and data['itemList']:
# # # #                 print(f"   ✓ Got {len(data['itemList'])} videos")
# # # #                 return data
# # # #             else:
# # # #                 print(f"   ⊗ No videos in response")
# # # #                 return None

# # # #         except Exception as e:
# # # #             print(f"   ✗ Error: {e}")
# # # #             return None

# # # #     def save_video(self, video_item: Dict[str, Any], username: str):
# # # #         """Save video JSON to Digital Ocean Spaces"""
# # # #         try:
# # # #             video_id = video_item.get('id')
# # # #             if not video_id:
# # # #                 return

# # # #             # Create temp file
# # # #             temp_filename = f"{video_id}.json"
# # # #             temp_filepath = os.path.join(self.output_dir, temp_filename)

# # # #             with open(temp_filepath, 'w', encoding='utf-8') as f:
# # # #                 json.dump(video_item, f, indent=2, ensure_ascii=False)

# # # #             # Upload to Spaces
# # # #             object_name = f"tiktok_video_metadata/{username}/{video_id}.json"

# # # #             if upload_file(temp_filepath, object_name):
# # # #                 os.remove(temp_filepath)
# # # #                 print(f"      ✓ Uploaded {video_id}")
# # # #             else:
# # # #                 print(f"      ✗ Failed to upload {video_id}")

# # # #         except Exception as e:
# # # #             print(f"      ✗ Error saving: {e}")

# # # #     def scrape_user_profile(self, username: str) -> bool:
# # # #         """Scrape all videos from a user's profile"""
# # # #         print(f"\n{'='*70}")
# # # #         print(f"  Scraping @{username}")
# # # #         print(f"{'='*70}")

# # # #         # Get secUid
# # # #         sec_uid = self.get_user_sec_uid(username)
# # # #         if not sec_uid:
# # # #             return False

# # # #         cursor = 0
# # # #         total_videos = 0

# # # #         while True:
# # # #             # Fetch videos
# # # #             data = self.fetch_user_videos(username, sec_uid, cursor)
            
# # # #             if not data:
# # # #                 break

# # # #             item_list = data.get('itemList', [])
# # # #             if not item_list:
# # # #                 break

# # # #             # Save each video
# # # #             for item in item_list:
# # # #                 self.save_video(item, username)
# # # #                 total_videos += 1

# # # #             # Check if there are more
# # # #             has_more = data.get('hasMore', False)
            
# # # #             if has_more and item_list:
# # # #                 last_video = item_list[-1]
# # # #                 create_time = last_video.get('createTime')
# # # #                 if create_time:
# # # #                     cursor = int(create_time) * 1000
# # # #                 else:
# # # #                     break
# # # #             else:
# # # #                 break

# # # #             time.sleep(2)

# # # #         print(f"\n✓ Finished @{username} — {total_videos} videos")
# # # #         return True


# # # # @celery_app.task(bind=True, name="tasks.scrape_profile")
# # # # def scrape_profile_task(self, username: str):
# # # #     """Celery task to scrape a TikTok profile"""
# # # #     print(f"\nTask: Scrape @{username}")

# # # #     # Initialize scraper (loads session from file)
# # # #     scraper = TikTokProfileScraper()

# # # #     # Initialize Redis
# # # #     redis_client = redis.Redis(
# # # #         host=os.getenv("REDIS_HOST", "localhost"),
# # # #         port=int(os.getenv("REDIS_PORT", 6379)),
# # # #         db=0
# # # #     )

# # # #     try:
# # # #         # Check if already scraped
# # # #         if redis_client.sismember("scraped_usernames", username):
# # # #             print(f"⊗ Already scraped @{username}")
# # # #             return {"status": "skipped", "username": username}

# # # #         # Scrape the profile
# # # #         success = scraper.scrape_user_profile(username)

# # # #         if success:
# # # #             redis_client.sadd("scraped_usernames", username)
# # # #             return {"status": "success", "username": username}
# # # #         else:
# # # #             return {"status": "failed", "username": username}

# # # #     except Exception as e:
# # # #         print(f"✗ Error: {e}")
# # # #         import traceback
# # # #         traceback.print_exc()
# # # #         return {"status": "error", "username": username, "error": str(e)}




# # # import os
# # # import json
# # # import time
# # # import redis
# # # import sys
# # # from typing import Optional, Dict, Any
# # # from urllib.parse import quote
# # # from collections import OrderedDict
# # # from pathlib import Path
# # # from curl_cffi import requests
# # # from dotenv import load_dotenv
# # # from celery_config import celery_app

# # # env_path = Path(__file__).parent.parent / ".env"
# # # load_dotenv(dotenv_path=env_path)

# # # sys.path.append(str(Path(__file__).parent.parent / "shared"))
# # # from storage import upload_file
# # # from proxy import ProxyManager


# # # class TikTokProfileScraper:
# # #     """TikTok Profile scraper using the private API"""

# # #     def __init__(self, output_dir="tiktok_videos", session_file="profile_session.json"):
# # #         self.output_dir = output_dir
# # #         self.session_file = session_file
# # #         self.proxy_manager = ProxyManager()
        
# # #         # Session data
# # #         self.cookies = None
# # #         self.headers = None
# # #         self.api_params_items = None
        
# # #         self._setup_output_directory()
# # #         self.load_session()

# # #     def _setup_output_directory(self):
# # #         os.makedirs(self.output_dir, exist_ok=True)

# # #     def load_session(self):
# # #         """Load TikTok session from file"""
# # #         session_path = Path(__file__).parent / self.session_file
        
# # #         if not session_path.exists():
# # #             raise FileNotFoundError(
# # #                 f"Session file not found: {self.session_file}\n"
# # #                 f"Please run: python capture_session.py"
# # #             )
        
# # #         with open(session_path, "r", encoding="utf-8") as f:
# # #             data = json.load(f)
        
# # #         self.cookies = data["cookies"]
# # #         self.headers = data["headers"]
# # #         self.api_params_items = data["params"]
        
# # #         print(f"✓ Loaded session from {self.session_file}")

# # #     def build_api_url(self, sec_uid: str, cursor: int = 0, count: int = 16) -> str:
# # #         """
# # #         Build profile API URL preserving captured parameter order
# # #         Only updates: secUid, cursor, count
# # #         """
# # #         base_url = "https://www.tiktok.com/api/post/item_list/"

# # #         if not self.api_params_items:
# # #             raise Exception("API parameters not initialized.")

# # #         pairs = list(self.api_params_items)

# # #         # Update only the necessary parameters
# # #         def set_or_replace(pairs_list, key, value):
# # #             for i, (k, _) in enumerate(pairs_list):
# # #                 if k == key:
# # #                     pairs_list[i] = (key, str(value))
# # #                     return
# # #             pairs_list.append((key, str(value)))

# # #         set_or_replace(pairs, "secUid", sec_uid)
# # #         set_or_replace(pairs, "cursor", str(cursor))
# # #         set_or_replace(pairs, "count", str(count))

# # #         # Deduplicate signature tokens
# # #         sig_keys = {"msToken", "X-Bogus", "X-Gnarly"}
# # #         seen = {k: False for k in sig_keys}
# # #         deduped = []
# # #         for k, v in pairs:
# # #             if k in sig_keys:
# # #                 if not seen[k]:
# # #                     deduped.append((k, v))
# # #                     seen[k] = True
# # #             else:
# # #                 deduped.append((k, v))
# # #         pairs = deduped

# # #         # Encode parameters
# # #         def encode_pair(k, v):
# # #             if k in sig_keys:
# # #                 return f"{quote(k, safe='')}={quote(v, safe='/=')}"
# # #             return f"{quote(k, safe='')}={quote(v, safe='')}"

# # #         query = "&".join(encode_pair(k, v) for k, v in pairs)
# # #         return f"{base_url}?{query}"

# # #     def get_user_sec_uid(self, username: str) -> Optional[str]:
# # #         """Get secUid from user profile page"""
# # #         try:
# # #             import re
            
# # #             profile_url = f"https://www.tiktok.com/@{username}"
            
# # #             response = requests.get(
# # #                 profile_url,
# # #                 impersonate="chrome131",
# # #                 timeout=30
# # #             )
            
# # #             if response.status_code != 200:
# # #                 print(f"✗ Failed to fetch profile: {response.status_code}")
# # #                 return None

# # #             match = re.search(r'"secUid":"(MS4wLjABAAAA[^"]+)"', response.text)
# # #             if match:
# # #                 sec_uid = match.group(1)
# # #                 print(f"✓ Found secUid for @{username}")
# # #                 return sec_uid

# # #             print(f"✗ Could not find secUid for @{username}")
# # #             return None

# # #         except Exception as e:
# # #             print(f"✗ Error getting secUid: {e}")
# # #             return None

# # #     def fetch_user_videos(self, username: str, sec_uid: str, cursor: int = 0) -> Optional[Dict[str, Any]]:
# # #         """Fetch videos from user profile"""
# # #         try:
# # #             url = self.build_api_url(sec_uid, cursor)
            
# # #             # Update referer header for this specific user
# # #             headers = self.headers.copy()
# # #             headers["referer"] = f"https://www.tiktok.com/@{username}"

# # #             print(f"📡 Fetching @{username} (cursor={cursor})...")

# # #             # Get proxy
# # #             proxy_config = self.proxy_manager.get_proxy_config(ProxyManager.PROXY_TYPE_ROTATING)

# # #             response = requests.get(
# # #                 url,
# # #                 headers=headers,
# # #                 cookies=self.cookies,
# # #                 impersonate="chrome131",
# # #                 proxies=proxy_config,
# # #                 timeout=30
# # #             )

# # #             if response.status_code != 200:
# # #                 print(f"   ✗ Status {response.status_code}")
# # #                 return None

# # #             data = response.json()
            
# # #             if 'itemList' in data and data['itemList']:
# # #                 print(f"   ✓ Got {len(data['itemList'])} videos")
# # #                 return data
# # #             else:
# # #                 print(f"   ⊗ No videos in response")
# # #                 return None

# # #         except Exception as e:
# # #             print(f"   ✗ Error: {e}")
# # #             return None

# # #     def save_video_metadata(self, video_item: Dict[str, Any], username: str) -> bool:
# # #         """Save video metadata JSON to Digital Ocean Spaces"""
# # #         try:
# # #             video_id = video_item.get('id')
# # #             if not video_id:
# # #                 return False

# # #             # Create temp file
# # #             temp_filename = f"{video_id}.json"
# # #             temp_filepath = os.path.join(self.output_dir, temp_filename)

# # #             with open(temp_filepath, 'w', encoding='utf-8') as f:
# # #                 json.dump(video_item, f, indent=2, ensure_ascii=False)

# # #             # Upload to Spaces
# # #             object_name = f"tiktok_video_metadata/{username}/{video_id}.json"

# # #             if upload_file(temp_filepath, object_name):
# # #                 os.remove(temp_filepath)
# # #                 print(f"      ✓ Uploaded metadata {video_id}")
# # #                 return True
# # #             else:
# # #                 print(f"      ✗ Failed to upload metadata {video_id}")
# # #                 return False

# # #         except Exception as e:
# # #             print(f"      ✗ Error saving metadata: {e}")
# # #             return False

# # #     def queue_video_for_download(self, video_item: Dict[str, Any], username: str, redis_client: redis.Redis):
# # #         """Queue video ID for download by video downloader"""
# # #         try:
# # #             video_id = video_item.get('id')
# # #             if not video_id:
# # #                 return

# # #             # Check if already downloaded or queued
# # #             if redis_client.sismember("downloaded_videos", video_id):
# # #                 print(f"      ⊗ Video {video_id} already downloaded")
# # #                 return

# # #             if redis_client.sismember("download_queue", video_id):
# # #                 print(f"      ⊗ Video {video_id} already in queue")
# # #                 return

# # #             # Send Celery task for video download
# # #             celery_app.send_task(
# # #                 'tasks.download_video',
# # #                 args=[video_id, username, video_item]
# # #             )

# # #             # Add to download queue set
# # #             redis_client.sadd("download_queue", video_id)
            
# # #             print(f"      ✓ Queued video {video_id} for download")

# # #         except Exception as e:
# # #             print(f"      ✗ Error queuing video: {e}")

# # #     def scrape_user_profile(self, username: str, redis_client: redis.Redis) -> bool:
# # #         """Scrape all videos from a user's profile"""
# # #         print(f"\n{'='*70}")
# # #         print(f"  Scraping @{username}")
# # #         print(f"{'='*70}")

# # #         # Get secUid
# # #         sec_uid = self.get_user_sec_uid(username)
# # #         if not sec_uid:
# # #             return False

# # #         cursor = 0
# # #         total_videos = 0
# # #         total_queued = 0

# # #         while True:
# # #             # Fetch videos
# # #             data = self.fetch_user_videos(username, sec_uid, cursor)
            
# # #             if not data:
# # #                 break

# # #             item_list = data.get('itemList', [])
# # #             if not item_list:
# # #                 break

# # #             # Process each video
# # #             for item in item_list:
# # #                 # Save metadata to Spaces
# # #                 if self.save_video_metadata(item, username):
# # #                     total_videos += 1
                    
# # #                     # Queue for download
# # #                     self.queue_video_for_download(item, username, redis_client)
# # #                     total_queued += 1

# # #             # Check if there are more
# # #             has_more = data.get('hasMore', False)
            
# # #             if has_more and item_list:
# # #                 last_video = item_list[-1]
# # #                 create_time = last_video.get('createTime')
# # #                 if create_time:
# # #                     cursor = int(create_time) * 1000
# # #                 else:
# # #                     break
# # #             else:
# # #                 break

# # #             time.sleep(2)

# # #         print(f"\n✓ Finished @{username} — {total_videos} metadata saved, {total_queued} videos queued")
# # #         return True


# # # @celery_app.task(bind=True, name="tasks.scrape_profile")
# # # def scrape_profile_task(self, username: str):
# # #     """Celery task to scrape a TikTok profile"""
# # #     print(f"\nTask: Scrape @{username}")

# # #     # Initialize scraper (loads session from file)
# # #     scraper = TikTokProfileScraper()

# # #     # Initialize Redis
# # #     redis_client = redis.Redis(
# # #         host=os.getenv("REDIS_HOST", "localhost"),
# # #         port=int(os.getenv("REDIS_PORT", 6379)),
# # #         db=0
# # #     )

# # #     try:
# # #         # Check if already scraped
# # #         if redis_client.sismember("scraped_usernames", username):
# # #             print(f"⊗ Already scraped @{username}")
# # #             return {"status": "skipped", "username": username}

# # #         # Scrape the profile (now also queues videos for download)
# # #         success = scraper.scrape_user_profile(username, redis_client)

# # #         if success:
# # #             redis_client.sadd("scraped_usernames", username)
# # #             return {"status": "success", "username": username}
# # #         else:
# # #             return {"status": "failed", "username": username}

# # #     except Exception as e:
# # #         print(f"✗ Error: {e}")
# # #         import traceback
# # #         traceback.print_exc()
# # #         return {"status": "error", "username": username, "error": str(e)}




# # import os
# # import json
# # import time
# # import redis
# # import sys
# # from typing import Optional, Dict, Any
# # from urllib.parse import quote
# # from collections import OrderedDict
# # from pathlib import Path
# # from curl_cffi import requests
# # from dotenv import load_dotenv
# # from celery_config import celery_app

# # env_path = Path(__file__).parent.parent / ".env"
# # load_dotenv(dotenv_path=env_path)

# # sys.path.append(str(Path(__file__).parent.parent / "shared"))
# # from storage import upload_file
# # from proxy import ProxyManager


# # class TikTokProfileScraper:
# #     """TikTok Profile scraper using the private API"""

# #     def __init__(self, output_dir="tiktok_videos", session_file="profile_session.json"):
# #         self.output_dir = output_dir
# #         self.session_file = session_file
# #         self.proxy_manager = ProxyManager()
        
# #         # Session data
# #         self.cookies = None
# #         self.headers = None
# #         self.api_params_items = None
        
# #         self._setup_output_directory()
# #         self.load_session()

# #     def _setup_output_directory(self):
# #         os.makedirs(self.output_dir, exist_ok=True)

# #     def load_session(self):
# #         """Load TikTok session from file"""
# #         session_path = Path(__file__).parent / self.session_file
        
# #         if not session_path.exists():
# #             raise FileNotFoundError(
# #                 f"Session file not found: {self.session_file}\n"
# #                 f"Please run: python capture_session.py"
# #             )
        
# #         with open(session_path, "r", encoding="utf-8") as f:
# #             data = json.load(f)
        
# #         self.cookies = data["cookies"]
# #         self.headers = data["headers"]
# #         self.api_params_items = data["params"]
        
# #         print(f"✓ Loaded session from {self.session_file}")

# #     def build_api_url(self, sec_uid: str, cursor: int = 0, count: int = 16) -> str:
# #         """
# #         Build profile API URL preserving captured parameter order
# #         Only updates: secUid, cursor, count
# #         """
# #         base_url = "https://www.tiktok.com/api/post/item_list/"

# #         if not self.api_params_items:
# #             raise Exception("API parameters not initialized.")

# #         pairs = list(self.api_params_items)

# #         # Update only the necessary parameters
# #         def set_or_replace(pairs_list, key, value):
# #             for i, (k, _) in enumerate(pairs_list):
# #                 if k == key:
# #                     pairs_list[i] = (key, str(value))
# #                     return
# #             pairs_list.append((key, str(value)))

# #         set_or_replace(pairs, "secUid", sec_uid)
# #         set_or_replace(pairs, "cursor", str(cursor))
# #         set_or_replace(pairs, "count", str(count))

# #         # Deduplicate signature tokens
# #         sig_keys = {"msToken", "X-Bogus", "X-Gnarly"}
# #         seen = {k: False for k in sig_keys}
# #         deduped = []
# #         for k, v in pairs:
# #             if k in sig_keys:
# #                 if not seen[k]:
# #                     deduped.append((k, v))
# #                     seen[k] = True
# #             else:
# #                 deduped.append((k, v))
# #         pairs = deduped

# #         # Encode parameters
# #         def encode_pair(k, v):
# #             if k in sig_keys:
# #                 return f"{quote(k, safe='')}={quote(v, safe='/=')}"
# #             return f"{quote(k, safe='')}={quote(v, safe='')}"

# #         query = "&".join(encode_pair(k, v) for k, v in pairs)
# #         return f"{base_url}?{query}"

# #     def get_user_sec_uid(self, username: str) -> Optional[str]:
# #         """Get secUid from user profile page"""
# #         try:
# #             import re
            
# #             profile_url = f"https://www.tiktok.com/@{username}"
            
# #             response = requests.get(
# #                 profile_url,
# #                 impersonate="chrome131",
# #                 timeout=30
# #             )
            
# #             if response.status_code != 200:
# #                 print(f"✗ Failed to fetch profile: {response.status_code}")
# #                 return None

# #             match = re.search(r'"secUid":"(MS4wLjABAAAA[^"]+)"', response.text)
# #             if match:
# #                 sec_uid = match.group(1)
# #                 print(f"✓ Found secUid for @{username}")
# #                 return sec_uid

# #             print(f"✗ Could not find secUid for @{username}")
# #             return None

# #         except Exception as e:
# #             print(f"✗ Error getting secUid: {e}")
# #             return None

# #     def fetch_user_videos(self, username: str, sec_uid: str, cursor: int = 0) -> Optional[Dict[str, Any]]:
# #         """Fetch videos from user profile"""
# #         try:
# #             url = self.build_api_url(sec_uid, cursor)
            
# #             # Update referer header for this specific user
# #             headers = self.headers.copy()
# #             headers["referer"] = f"https://www.tiktok.com/@{username}"

# #             print(f"final url: ", url)
# #             print(f"headers: {headers}")
# #             print(f"cookies: ", self.cookies)

# #             print(f"📡 Fetching @{username} (cursor={cursor})...")

# #             # Get proxy
# #             proxy_config = self.proxy_manager.get_proxy_config(ProxyManager.PROXY_TYPE_DATACENTER)

# #             response = requests.get(
# #                 url,
# #                 headers=headers,
# #                 cookies=self.cookies,
# #                 impersonate="chrome131",
# #                 # proxies=proxy_config,
# #                 timeout=30
# #             )

# #             if response.status_code != 200:
# #                 print(f"   ✗ Status {response.status_code}")
# #                 return None

# #             data = response.json()
            
# #             if 'itemList' in data and data['itemList']:
# #                 print(f"   ✓ Got {len(data['itemList'])} videos")
# #                 return data
# #             else:
# #                 print(f"   ⊗ No videos in response")
# #                 return None

# #         except Exception as e:
# #             print(f"   ✗ Error: {e}")
# #             return None

# #     def save_video_metadata(self, video_item: Dict[str, Any], username: str) -> bool:
# #         """Save video metadata JSON to Digital Ocean Spaces"""
# #         try:
# #             video_id = video_item.get('id')
# #             if not video_id:
# #                 return False

# #             # Create temp file
# #             temp_filename = f"{video_id}.json"
# #             temp_filepath = os.path.join(self.output_dir, temp_filename)

# #             with open(temp_filepath, 'w', encoding='utf-8') as f:
# #                 json.dump(video_item, f, indent=2, ensure_ascii=False)

# #             # Upload to Spaces
# #             object_name = f"tiktok_video_metadata/{username}/{video_id}.json"

# #             if upload_file(temp_filepath, object_name):
# #                 os.remove(temp_filepath)
# #                 print(f"      ✓ Uploaded metadata {video_id}")
# #                 return True
# #             else:
# #                 print(f"      ✗ Failed to upload metadata {video_id}")
# #                 return False

# #         except Exception as e:
# #             print(f"      ✗ Error saving metadata: {e}")
# #             return False

# #     def queue_video_for_download(self, video_item: Dict[str, Any], username: str, redis_client: redis.Redis):
# #         """Queue video ID for download by video downloader"""
# #         try:
# #             video_id = video_item.get('id')
# #             if not video_id:
# #                 return

# #             # Check if already downloaded or queued
# #             if redis_client.sismember("downloaded_videos", video_id):
# #                 print(f"      ⊗ Video {video_id} already downloaded")
# #                 return

# #             if redis_client.sismember("download_queue", video_id):
# #                 print(f"      ⊗ Video {video_id} already in queue")
# #                 return

# #             # Check if it's a slideshow
# #             is_slideshow = bool(video_item.get('imagePost') or video_item.get('images'))

# #             # Send Celery task for video download
# #             celery_app.send_task(
# #                 'tasks.download_video',
# #                 args=[video_id, username, is_slideshow],
# #                 queue="downloader"
# #             )

# #             # Add to download queue set
# #             redis_client.sadd("download_queue", video_id)
            
# #             video_type = "slideshow" if is_slideshow else "video"
# #             print(f"      ✓ Queued {video_type} {video_id} for download")

# #         except Exception as e:
# #             print(f"      ✗ Error queuing video: {e}")

# #     def scrape_user_profile(self, username: str, redis_client: redis.Redis) -> bool:
# #         """Scrape all videos from a user's profile"""
# #         print(f"\n{'='*70}")
# #         print(f"  Scraping @{username}")
# #         print(f"{'='*70}")

# #         # Get secUid
# #         sec_uid = self.get_user_sec_uid(username)
# #         if not sec_uid:
# #             return False

# #         cursor = 0
# #         total_videos = 0
# #         total_queued = 0

# #         while True:
# #             # Fetch videos
# #             data = self.fetch_user_videos(username, sec_uid, cursor)
            
# #             if not data:
# #                 break

# #             item_list = data.get('itemList', [])
# #             if not item_list:
# #                 break

# #             # Process each video
# #             for item in item_list:
# #                 # Save metadata to Spaces
# #                 if self.save_video_metadata(item, username):
# #                     total_videos += 1
                    
# #                     # Queue for download
# #                     self.queue_video_for_download(item, username, redis_client)
# #                     total_queued += 1

# #             # Check if there are more
# #             has_more = data.get('hasMore', False)
            
# #             if has_more and item_list:
# #                 last_video = item_list[-1]
# #                 create_time = last_video.get('createTime')
# #                 if create_time:
# #                     cursor = int(create_time) * 1000
# #                 else:
# #                     break
# #             else:
# #                 break

# #             time.sleep(2)

# #         print(f"\n✓ Finished @{username} — {total_videos} metadata saved, {total_queued} videos queued")
# #         return True


# # @celery_app.task(bind=True, name="tasks.scrape_profile")
# # def scrape_profile_task(self, username: str):
# #     """Celery task to scrape a TikTok profile"""
# #     print(f"\n{'='*70}")
# #     print(f"  Task: Scrape @{username}")
# #     print(f"{'='*70}")

# #     # Initialize scraper (loads session from file)
# #     scraper = TikTokProfileScraper()

# #     # Initialize Redis
# #     redis_client = redis.Redis(
# #         host=os.getenv("REDIS_HOST", "localhost"),
# #         port=int(os.getenv("REDIS_PORT", 6379)),
# #         db=0
# #     )

# #     try:
# #         # Check if already scraped
# #         if redis_client.sismember("scraped_usernames", username):
# #             print(f"⊗ Already scraped @{username}")
# #             return {"status": "skipped", "username": username}

# #         # Scrape the profile (now also queues videos for download)
# #         success = scraper.scrape_user_profile(username, redis_client)

# #         if success:
# #             redis_client.sadd("scraped_usernames", username)
# #             return {"status": "success", "username": username}
# #         else:
# #             return {"status": "failed", "username": username}

# #     except Exception as e:
# #         print(f"✗ Error: {e}")
# #         import traceback
# #         traceback.print_exc()
# #         return {"status": "error", "username": username, "error": str(e)}





# import os
# import json
# import time
# import redis
# import sys
# from typing import Optional, Dict, Any
# from urllib.parse import quote
# from collections import OrderedDict
# from pathlib import Path
# from curl_cffi import requests
# from dotenv import load_dotenv
# from celery_config import celery_app

# env_path = Path(__file__).parent.parent / ".env"
# load_dotenv(dotenv_path=env_path)

# sys.path.append(str(Path(__file__).parent.parent / "shared"))
# from storage import upload_file
# from proxy import ProxyManager


# class TikTokProfileScraper:
#     """TikTok Profile scraper using the private API"""

#     def __init__(self, output_dir="tiktok_videos", session_file="profile_session.json"):
#         self.output_dir = output_dir
#         self.session_file = session_file
#         self.proxy_manager = ProxyManager()
        
#         # Session data
#         self.cookies = None
#         self.headers = None
#         self.api_params_items = None
        
#         self._setup_output_directory()
#         self.load_session()

#     def _setup_output_directory(self):
#         os.makedirs(self.output_dir, exist_ok=True)

#     def load_session(self):
#         """Load TikTok session from file"""
#         session_path = Path(__file__).parent / self.session_file
        
#         if not session_path.exists():
#             raise FileNotFoundError(
#                 f"Session file not found: {self.session_file}\n"
#                 f"Please run: python capture_session.py"
#             )
        
#         with open(session_path, "r", encoding="utf-8") as f:
#             data = json.load(f)
        
#         self.cookies = data["cookies"]
#         self.headers = data["headers"]
#         self.api_params_items = data["params"]
        
#         print(f"✓ Loaded session from {self.session_file}")

#     def build_api_url(self, sec_uid: str, cursor: int = 0, count: int = 16) -> str:
#         """
#         Build profile API URL preserving captured parameter order
#         Only updates: secUid, cursor, count
#         """
#         base_url = "https://www.tiktok.com/api/post/item_list/"

#         if not self.api_params_items:
#             raise Exception("API parameters not initialized.")

#         pairs = list(self.api_params_items)

#         # Update only the necessary parameters
#         def set_or_replace(pairs_list, key, value):
#             for i, (k, _) in enumerate(pairs_list):
#                 if k == key:
#                     pairs_list[i] = (key, str(value))
#                     return
#             pairs_list.append((key, str(value)))

#         set_or_replace(pairs, "secUid", sec_uid)
#         set_or_replace(pairs, "cursor", str(cursor))
#         set_or_replace(pairs, "count", str(count))

#         # Deduplicate signature tokens
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

#         # Encode parameters
#         def encode_pair(k, v):
#             if k in sig_keys:
#                 return f"{quote(k, safe='')}={quote(v, safe='/=')}"
#             return f"{quote(k, safe='')}={quote(v, safe='')}"

#         query = "&".join(encode_pair(k, v) for k, v in pairs)
#         return f"{base_url}?{query}"

#     def get_user_sec_uid(self, username: str) -> Optional[str]:
#         """Get secUid from user profile page"""
#         try:
#             import re
            
#             profile_url = f"https://www.tiktok.com/@{username}"
            
#             response = requests.get(
#                 profile_url,
#                 impersonate="chrome131",
#                 timeout=30
#             )
            
#             if response.status_code != 200:
#                 print(f"✗ Failed to fetch profile: {response.status_code}")
#                 return None

#             match = re.search(r'"secUid":"(MS4wLjABAAAA[^"]+)"', response.text)
#             if match:
#                 sec_uid = match.group(1)
#                 print(f"✓ Found secUid for @{username}")
#                 return sec_uid

#             print(f"✗ Could not find secUid for @{username}")
#             return None

#         except Exception as e:
#             print(f"✗ Error getting secUid: {e}")
#             return None

#     def fetch_user_videos(self, username: str, sec_uid: str, cursor: int = 0) -> Optional[Dict[str, Any]]:
#         """Fetch videos from user profile"""
#         try:
#             url = self.build_api_url(sec_uid, cursor)
            
#             # Update referer header for this specific user
#             headers = self.headers.copy()
#             headers["referer"] = f"https://www.tiktok.com/@{username}"

#             print(f"📡 Fetching @{username} (cursor={cursor})...")

#             # Get proxy
#             proxy_config = self.proxy_manager.get_proxy_config(ProxyManager.PROXY_TYPE_ROTATING)

#             print(url)
#             print(headers)
#             print(self.cookies)
#             response = requests.get(
#                 url,
#                 headers=headers,
#                 # cookies=self.cookies,
#                 impersonate="chrome131",
#                 # proxies=proxy_config,
#                 timeout=30
#             )

#             if response.status_code != 200:
#                 print(f"   ✗ Status {response.status_code}")
#                 return None

#             data = response.json()
            
#             if 'itemList' in data and data['itemList']:
#                 print(f"   ✓ Got {len(data['itemList'])} videos")
#                 return data
#             else:
#                 print(f"   ⊗ No videos in response")
#                 return None

#         except Exception as e:
#             print(f"   ✗ Error: {e}")
#             return None

#     def save_video(self, video_item: Dict[str, Any], username: str):
#         """Save video JSON to Digital Ocean Spaces"""
#         try:
#             video_id = video_item.get('id')
#             if not video_id:
#                 return

#             # Create temp file
#             temp_filename = f"{video_id}.json"
#             temp_filepath = os.path.join(self.output_dir, temp_filename)

#             with open(temp_filepath, 'w', encoding='utf-8') as f:
#                 json.dump(video_item, f, indent=2, ensure_ascii=False)

#             # Upload to Spaces
#             object_name = f"tiktok_video_metadata/{username}/{video_id}.json"

#             if upload_file(temp_filepath, object_name):
#                 os.remove(temp_filepath)
#                 print(f"      ✓ Uploaded {video_id}")
#             else:
#                 print(f"      ✗ Failed to upload {video_id}")

#         except Exception as e:
#             print(f"      ✗ Error saving: {e}")

#     def scrape_user_profile(self, username: str) -> bool:
#         """Scrape all videos from a user's profile"""
#         print(f"\n{'='*70}")
#         print(f"  Scraping @{username}")
#         print(f"{'='*70}")

#         # Get secUid
#         sec_uid = self.get_user_sec_uid(username)
#         if not sec_uid:
#             return False

#         cursor = 0
#         total_videos = 0

#         while True:
#             # Fetch videos
#             data = self.fetch_user_videos(username, sec_uid, cursor)
            
#             if not data:
#                 break

#             item_list = data.get('itemList', [])
#             if not item_list:
#                 break

#             # Save each video
#             for item in item_list:
#                 self.save_video(item, username)
#                 total_videos += 1

#             # Check if there are more
#             has_more = data.get('hasMore', False)
            
#             if has_more and item_list:
#                 last_video = item_list[-1]
#                 create_time = last_video.get('createTime')
#                 if create_time:
#                     cursor = int(create_time) * 1000
#                 else:
#                     break
#             else:
#                 break

#             time.sleep(2)

#         print(f"\n✓ Finished @{username} — {total_videos} videos")
#         return True


# @celery_app.task(bind=True, name="tasks.scrape_profile")
# def scrape_profile_task(self, username: str):
#     """Celery task to scrape a TikTok profile"""
#     print(f"\nTask: Scrape @{username}")

#     # Initialize scraper (loads session from file)
#     scraper = TikTokProfileScraper()

#     # Initialize Redis
#     redis_client = redis.Redis(
#         host=os.getenv("REDIS_HOST", "localhost"),
#         port=int(os.getenv("REDIS_PORT", 6379)),
#         db=0
#     )

#     try:
#         # Check if already scraped
#         if redis_client.sismember("scraped_usernames", username):
#             print(f"⊗ Already scraped @{username}")
#             return {"status": "skipped", "username": username}

#         # Scrape the profile
#         success = scraper.scrape_user_profile(username)

#         if success:
#             redis_client.sadd("scraped_usernames", username)
#             return {"status": "success", "username": username}
#         else:
#             return {"status": "failed", "username": username}

#     except Exception as e:
#         print(f"✗ Error: {e}")
#         import traceback
#         traceback.print_exc()
#         return {"status": "error", "username": username, "error": str(e)}




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