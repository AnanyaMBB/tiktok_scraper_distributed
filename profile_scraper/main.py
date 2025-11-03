#!/usr/bin/env python3
"""
Main entry point for TikTok Profile Scraper
Starts Celery worker
"""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

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
            username=os.getenv('REDIS_USERNAME', None) or None,
            password=os.getenv('REDIS_PASSWORD', None) or None,
            db=0
        )
        redis_client.ping()
        print("✓ Connected to Redis")
        print()
    except Exception as e:
        print(f"✗ Failed to connect to Redis: {e}")
        print("Please ensure Redis is running and credentials are correct in .env")
        return
    
    print("Starting Celery worker with 4 concurrent tasks...")
    print("Monitor with Flower: celery -A profile_scraper flower")
    print("=" * 60)
    print()
    
    # Start Celery worker
    os.execvp('celery', ['celery', '-A', 'profile_scraper', 'worker', '--loglevel=info', '--concurrency=4'])

if __name__ == "__main__":
    main()