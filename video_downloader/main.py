#!/usr/bin/env python3
"""
Main entry point for TikTok Video Downloader
Starts Celery worker that ONLY handles video download tasks
"""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load .env from parent directory
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

def main():
    """Start Celery worker for video downloads only"""
    print("=" * 70)
    print("TikTok Video Downloader - Starting Celery Worker")
    print("=" * 70)
    print()
    
    # Check Redis connection
    try:
        import redis
        redis_client = redis.Redis(
            host=os.getenv("REDIS_HOST", "localhost"),
            port=int(os.getenv("REDIS_PORT", 6379)),
            db=0
        )
        redis_client.ping()
        print("✓ Connected to Redis")
        print()
    except Exception as e:
        print(f"✗ Failed to connect to Redis: {e}")
        return
    
    # Check if yt-dlp is installed
    try:
        import yt_dlp
        print("✓ yt-dlp is installed")
    except ImportError:
        print("✗ yt-dlp not found. Install with: pip install yt-dlp")
        return
    
    # Check if gallery-dl is installed (for slideshows)
    import subprocess
    try:
        result = subprocess.run(['gallery-dl', '--version'], capture_output=True, timeout=5)
        if result.returncode == 0:
            print("✓ gallery-dl is installed")
        else:
            print("⚠️  gallery-dl may not be working properly")
    except FileNotFoundError:
        print("⚠️  gallery-dl not found. Slideshow downloads may not work.")
        print("   Install with: pip install gallery-dl")
    except Exception as e:
        print(f"⚠️  Could not verify gallery-dl: {e}")
    
    print()
    print("=" * 70)
    print("Worker Configuration:")
    print("  Task: tasks.download_video")
    print("  Concurrency: 4 workers (gevent)")
    print("  Queue: celery (default)")
    print("=" * 70)
    print()
    
    # Start Celery worker - ONLY processes tasks.download_video
    os.execvp('celery', [
        'celery',
        '-A', 'video_downloader',
        'worker',
        '--pool=gevent',
        '--concurrency=1',
        '--loglevel=info',
        '--max-tasks-per-child=100',
        '--hostname=video_downloader@%h',
        '-Q', 'downloader'
    ])


if __name__ == "__main__":
    main()