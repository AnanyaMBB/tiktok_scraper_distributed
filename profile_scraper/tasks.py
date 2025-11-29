"""
Celery Tasks for TikTok Profile Scraping

This module wraps the TikTokProfileScraper (v5) as a Celery task
to process usernames queued by the FYP scraper.
"""

import os
import sys
import asyncio
import redis
from typing import Optional
from pathlib import Path
from datetime import datetime

# Fix for Windows asyncio subprocess issue with Playwright/Patchright
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

from dotenv import load_dotenv

# Load .env from parent directory
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Add shared directory to path
sys.path.append(str(Path(__file__).parent.parent / 'shared'))

# Import Celery app from your existing config
from celery_config import celery_app

# Import the profile scraper we built
from profile_scraper_v5 import TikTokProfileScraper

# Redis client for tracking
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=0,
    decode_responses=True
)


@celery_app.task(
    name='tasks.scrape_profile',
    bind=True,
    max_retries=3,
    default_retry_delay=60,
    autoretry_for=(Exception,),
    retry_backoff=True
)
def scrape_profile(self, username: str, max_videos: Optional[int] = None):
    """
    Celery task to scrape a TikTok user's profile.
    
    Args:
        username: TikTok username (without @)
        max_videos: Maximum videos to scrape (None = all)
    
    Returns:
        Dict with scrape results
    """
    print(f"\n[Task {self.request.id}] Starting scrape for @{username}")
    
    result = {
        'username': username,
        'task_id': self.request.id,
        'success': False,
        'videos_saved': 0,
        'skipped': False,
        'error': None,
        'started_at': datetime.utcnow().isoformat(),
        'completed_at': None
    }
    
    # Check if already scraped
    if redis_client.sismember("scraped_usernames", username):
        print(f"[Task {self.request.id}] @{username} already scraped, skipping")
        result['skipped'] = True
        result['success'] = True
        result['reason'] = 'Already scraped'
        return result
    
    # Set lock to prevent duplicate concurrent scrapes
    lock_key = f"scraping:{username}"
    if not redis_client.set(lock_key, self.request.id, nx=True, ex=3600):
        print(f"[Task {self.request.id}] @{username} already being scraped by another worker")
        result['skipped'] = True
        result['success'] = True
        result['reason'] = 'Already in progress'
        return result
    
    try:
        # Build proxy config from environment or use default
        proxy_config = None
        proxy_server = os.getenv("PROXY_SERVER")
        proxy_username = os.getenv("PROXY_USERNAME")
        proxy_password = os.getenv("PROXY_PASSWORD")
        
        if proxy_server:
            proxy_config = {
                "server": proxy_server,
            }
            if proxy_username:
                proxy_config["username"] = proxy_username
            if proxy_password:
                proxy_config["password"] = proxy_password
            print(f"[Task {self.request.id}] Using proxy: {proxy_server}")

        print("task proxy config: ", proxy_config)
        
        # Initialize the scraper
        scraper = TikTokProfileScraper(
            output_dir=os.getenv("OUTPUT_DIR", "tiktok_video_metadata"),
            headless=os.getenv("HEADLESS", "false").lower() == "true",
            proxy_config=proxy_config
        )
        
        # Run the scrape
        videos = scraper.fetch_all_videos(
            username=username,
            max_videos=max_videos,
            skip_existing=True,
            max_no_new_scrolls=10
        )
        
        result['success'] = True
        result['videos_saved'] = len(videos)
        
        # Mark username as scraped
        redis_client.sadd("scraped_usernames", username)
        
        print(f"[Task {self.request.id}] Completed @{username}: {len(videos)} videos saved")
        
    except Exception as e:
        print(f"[Task {self.request.id}] Error scraping @{username}: {e}")
        result['error'] = str(e)
        import traceback
        traceback.print_exc()
        raise  # Re-raise for Celery retry
    
    finally:
        # Remove lock
        redis_client.delete(lock_key)
        result['completed_at'] = datetime.utcnow().isoformat()
    
    return result


@celery_app.task(name='tasks.get_scrape_stats')
def get_scrape_stats():
    """Get statistics about scraping progress"""
    return {
        'total_usernames_scraped': redis_client.scard("scraped_usernames"),
        'currently_scraping': len(redis_client.keys("scraping:*")),
    }


@celery_app.task(name='tasks.clear_user_history')
def clear_user_history(username: str):
    """Clear scrape history for a specific user so they can be re-scraped"""
    redis_client.srem("scraped_usernames", username)
    return {'cleared': username}