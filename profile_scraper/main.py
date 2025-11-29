#!/usr/bin/env python3
"""
Main entry point for TikTok Profile Scraper
Starts Celery worker (Windows-compatible)
"""
import os
import sys
import asyncio
from pathlib import Path
from dotenv import load_dotenv

# Fix for Windows asyncio subprocess issue with Playwright
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

# Load .env from parent directory
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

def main():
    """Start Celery worker"""
    print("=" * 60)
    print("TikTok Profile Scraper - Starting Celery Worker")
    print("=" * 60)
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
    except Exception as e:
        print(f"✗ Failed to connect to Redis: {e}")
        print("Please ensure Redis is running and credentials are correct in .env")
        return
    
    # Check if Patchright/Playwright is available
    try:
        from patchright.sync_api import sync_playwright
        print("✓ Patchright available (undetected browser)")
    except ImportError:
        try:
            from playwright.sync_api import sync_playwright
            print("⚠ Using regular Playwright (Patchright not installed)")
        except ImportError:
            print("✗ Neither Patchright nor Playwright installed!")
            print("Run: pip install patchright && patchright install chrome")
            return
    
    # Import tasks to register them with Celery
    try:
        import tasks
        print("✓ Tasks module loaded")
    except ImportError as e:
        print(f"✗ Failed to import tasks: {e}")
        return
    
    print()
    print("Starting Celery worker (Windows-compatible solo pool)...")
    print("Listening for 'tasks.scrape_profile' from FYP scraper...")
    print("=" * 60)
    print()
    
    # Start Celery worker with solo pool for Windows
    # Using celery_config which includes=['tasks']
    from celery_config import celery_app
    
    # Update include to have tasks module
    celery_app.conf.update(include=['tasks'])
    
    # Start worker programmatically (works better on Windows than os.execvp)
    celery_app.worker_main([
        'worker',
        '--pool=solo',
        '--loglevel=info',
        '-E'
    ])

if __name__ == "__main__":
    main()