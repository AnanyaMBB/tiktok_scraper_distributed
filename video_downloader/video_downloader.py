import os
import sys
import redis
import time
import subprocess
import zipfile
import shutil
import yt_dlp
from pathlib import Path
from dotenv import load_dotenv
from celery import Celery

# Load .env from parent directory
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Add shared directory to path
sys.path.append(str(Path(__file__).parent.parent / 'shared'))
from storage import upload_file
from proxy import ProxyManager

# Initialize Celery
celery_app = Celery(
    'tiktok_scraper',
    broker=f"redis://{os.getenv('REDIS_HOST', 'localhost')}:{os.getenv('REDIS_PORT', 6379)}/0",
    backend=f"redis://{os.getenv('REDIS_HOST', 'localhost')}:{os.getenv('REDIS_PORT', 6379)}/0"
)

# Configure Celery
celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    task_track_started=True,
    task_time_limit=600,  # 10 minutes max per video
    task_soft_time_limit=540,  # 9 minutes soft limit
    worker_prefetch_multiplier=1,
    worker_max_tasks_per_child=100,
)


class TikTokVideoDownloader:
    """TikTok video downloader with proxy support"""
    
    def __init__(self, output_dir="downloads"):
        self.output_dir = output_dir
        self.proxy_manager = ProxyManager()
        self._setup_output_directory()
    
    def _setup_output_directory(self):
        """Create output directory if it doesn't exist"""
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "slideshows"), exist_ok=True)
    
    def download_video_with_ytdlp(self, url: str, video_id: str, max_retries: int = 3) -> str:
        """Download video using yt-dlp with proxy rotation"""
        output_path = os.path.join(self.output_dir, f"{video_id}.mp4")
        
        for attempt in range(max_retries):
            # Get proxy
            proxy_config = self.proxy_manager.get_proxy_config(ProxyManager.PROXY_TYPE_DATACENTER)
            proxy_url = proxy_config.get('http') if proxy_config else None
            
            options = {
                'outtmpl': output_path,
                'format': 'bestvideo+bestaudio/best',
                'merge_output_format': 'mp4',
                'quiet': False,
                'no_warnings': False,
                'socket_timeout': 30,
                'retries': 1,
            }
            
            if proxy_url:
                options['proxy'] = proxy_url
                print(f"   Attempt {attempt + 1}/{max_retries} with proxy")
            else:
                print(f"   Attempt {attempt + 1}/{max_retries} without proxy")
            
            try:
                with yt_dlp.YoutubeDL(options) as ydl:
                    ydl.download([url])
                
                if os.path.exists(output_path):
                    file_size = os.path.getsize(output_path)
                    print(f"   ✓ Downloaded: {video_id} ({file_size / 1024 / 1024:.2f} MB)")
                    return output_path
                    
            except Exception as e:
                print(f"   ✗ Download attempt {attempt + 1} failed: {e}")
                
                # Clean up partial download
                if os.path.exists(output_path):
                    try:
                        os.remove(output_path)
                    except:
                        pass
                
                if attempt == max_retries - 1:
                    raise e
                
                time.sleep(2)
        
        return None
    
    def download_slideshow_with_gallery_dl(self, url: str, video_id: str, max_retries: int = 3) -> str:
        """Download slideshow using gallery-dl with proxy rotation"""
        slideshow_folder = os.path.join(self.output_dir, "slideshows", video_id)
        os.makedirs(slideshow_folder, exist_ok=True)
        
        for attempt in range(max_retries):
            # Get proxy
            proxy_config = self.proxy_manager.get_proxy_config(ProxyManager.PROXY_TYPE_ROTATING)
            proxy_url = proxy_config.get('http') if proxy_config else None
            
            try:
                cmd = [
                    'gallery-dl',
                    '--dest', slideshow_folder,
                    '--filename', '{num:>02}.{extension}',
                    url
                ]
                
                if proxy_url:
                    cmd.extend(['--proxy', proxy_url])
                    print(f"   Slideshow attempt {attempt + 1}/{max_retries} with proxy")
                else:
                    print(f"   Slideshow attempt {attempt + 1}/{max_retries} without proxy")
                
                result = subprocess.run(
                    cmd, 
                    capture_output=True, 
                    text=True, 
                    check=True, 
                    timeout=120
                )
                
                # Check if files were downloaded
                files_downloaded = []
                for root, dirs, files in os.walk(slideshow_folder):
                    for file in files:
                        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp', '.mp3')):
                            files_downloaded.append(file)
                
                if not files_downloaded:
                    raise Exception("No files downloaded from slideshow")
                
                # Create zip file
                zip_filename = f"{video_id}.zip"
                zip_path = os.path.join(self.output_dir, zip_filename)
                
                with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    for root, dirs, files in os.walk(slideshow_folder):
                        for file in files:
                            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp', '.mp3')):
                                file_path = os.path.join(root, file)
                                zipf.write(file_path, file)
                
                # Clean up slideshow folder
                shutil.rmtree(slideshow_folder)
                
                zip_size = os.path.getsize(zip_path)
                print(f"   ✓ Downloaded slideshow: {video_id} ({len(files_downloaded)} files, {zip_size / 1024 / 1024:.2f} MB)")
                return zip_path
                
            except Exception as e:
                print(f"   ✗ Slideshow attempt {attempt + 1} failed: {e}")
                
                if attempt == max_retries - 1:
                    # Clean up on final failure
                    if os.path.exists(slideshow_folder):
                        shutil.rmtree(slideshow_folder)
                    raise e
                
                time.sleep(2)
        
        return None


@celery_app.task(bind=True, name='tasks.download_video', max_retries=3, default_retry_delay=60, queue="downloader")
def download_video_task(self, video_id: str, username: str, is_slideshow: bool):
    """
    Celery task to download a TikTok video
    
    Args:
        video_id: TikTok video ID
        username: TikTok username
        is_slideshow: True if slideshow/photo post, False if video
    """
    print(f"\n{'='*70}")
    print(f"  Downloading: {video_id} from @{username}")
    print(f"  Type: {'Slideshow' if is_slideshow else 'Video'}")
    print(f"{'='*70}")
    
    downloader = TikTokVideoDownloader()
    
    # Initialize Redis
    redis_client = redis.Redis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=int(os.getenv("REDIS_PORT", 6379)),
        db=0
    )
    
    try:
        # Check if already downloaded
        if redis_client.sismember("downloaded_videos", video_id):
            print(f"⊗ Video {video_id} already downloaded")
            # Remove from queue if still there
            redis_client.srem("download_queue", video_id)
            return {"status": "skipped", "video_id": video_id, "reason": "already_downloaded"}
        
        # Construct TikTok URL
        if is_slideshow:
            video_url = f"https://www.tiktok.com/@{username}/photo/{video_id}"
        else:
            video_url = f"https://www.tiktok.com/@{username}/video/{video_id}"
        
        print(f"URL: {video_url}")
        
        if is_slideshow:
            print("📸 Downloading slideshow...")
            
            # Download slideshow
            zip_path = downloader.download_slideshow_with_gallery_dl(video_url, video_id)
            
            if zip_path and os.path.exists(zip_path):
                # Upload to Spaces
                object_name = f"tiktok_video/{username}/{video_id}.zip"
                
                print(f"   Uploading to Spaces: {object_name}")
                
                if upload_file(zip_path, object_name):
                    # Clean up local file
                    try:
                        os.remove(zip_path)
                    except:
                        pass
                    
                    print(f"✓ Successfully uploaded slideshow: {object_name}")
                    
                    # Mark as downloaded
                    redis_client.sadd("downloaded_videos", video_id)
                    redis_client.srem("download_queue", video_id)
                    
                    return {
                        "status": "success",
                        "video_id": video_id,
                        "type": "slideshow",
                        "path": object_name
                    }
                else:
                    print(f"✗ Failed to upload slideshow")
                    # Retry the task
                    raise self.retry(exc=Exception("Upload failed"), countdown=60)
            else:
                print(f"✗ Failed to download slideshow")
                # Retry the task
                raise self.retry(exc=Exception("Download failed"), countdown=60)
        
        else:
            print("🎥 Downloading video...")
            
            # Download video
            video_path = downloader.download_video_with_ytdlp(video_url, video_id)
            
            if video_path and os.path.exists(video_path):
                # Upload to Spaces
                object_name = f"tiktok_video/{username}/{video_id}.mp4"
                
                print(f"   Uploading to Spaces: {object_name}")
                
                if upload_file(video_path, object_name):
                    # Clean up local file
                    try:
                        os.remove(video_path)
                    except:
                        pass
                    
                    print(f"✓ Successfully uploaded video: {object_name}")
                    
                    # Mark as downloaded
                    redis_client.sadd("downloaded_videos", video_id)
                    redis_client.srem("download_queue", video_id)
                    
                    return {
                        "status": "success",
                        "video_id": video_id,
                        "type": "video",
                        "path": object_name
                    }
                else:
                    print(f"✗ Failed to upload video")
                    # Retry the task
                    raise self.retry(exc=Exception("Upload failed"), countdown=60)
            else:
                print(f"✗ Failed to download video")
                # Retry the task
                raise self.retry(exc=Exception("Download failed"), countdown=60)
    
    except self.MaxRetriesExceededError:
        print(f"✗ Max retries exceeded for video {video_id}")
        # Remove from queue after max retries
        redis_client.srem("download_queue", video_id)
        return {
            "status": "failed",
            "video_id": video_id,
            "reason": "max_retries_exceeded"
        }
    
    except Exception as e:
        print(f"✗ Error downloading video: {e}")
        import traceback
        traceback.print_exc()
        
        # Retry the task
        try:
            raise self.retry(exc=e, countdown=60)
        except self.MaxRetriesExceededError:
            # Remove from queue after max retries
            redis_client.srem("download_queue", video_id)
            return {
                "status": "error",
                "video_id": video_id,
                "error": str(e)
            }