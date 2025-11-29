#!/usr/bin/env python3
import redis
import os
import argparse
from fyp_scraper import TikTokFYPScraper


def main():
    parser = argparse.ArgumentParser(description="TikTok FYP Scraper")
    parser.add_argument("--output-dir", type=str, default="tiktok_video_metadata", 
                        help="Directory to save video metadata")
    parser.add_argument("--max-iterations", type=int, default=None,
                        help="Maximum number of scraping iterations (None for infinite)")
    parser.add_argument("--delay", type=int, default=5,
                        help="Delay in seconds between API requests")
    args = parser.parse_args()

    # Initialize Redis client
    redis_client = redis.Redis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=os.getenv("REDIS_PORT", 6379),
        # username=os.getenv('REDIS_USERNAME', None),
        # password=os.getenv('REDIS_PASSWORD', None),
        db=0
    )

    # Test Redis connection
    try:
        redis_client.ping()
        print("✓ Connected to Redis")
    except redis.ConnectionError as e:
        print(f"✗ Failed to connect to Redis: {e}")
        return

    # Initialize and run scraper
    scraper = TikTokFYPScraper(
        redis_client=redis_client,
        output_dir=args.output_dir
    )

    print("Starting FYP scraper...")
    scraper.run(
        max_iterations=args.max_iterations,
        delay=args.delay
    )


if __name__ == "__main__":
    main()