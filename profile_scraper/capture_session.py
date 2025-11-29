#!/usr/bin/env python3
"""
Script to capture TikTok profile session data and save it to a file.
Run this manually whenever you need to refresh the session.
"""
import json
import time
from urllib.parse import urlparse, parse_qsl
from collections import OrderedDict
from playwright.sync_api import sync_playwright


def capture_profile_session(sample_username="nike", min_requests=3):
    """Capture session data from a TikTok profile"""
    print("=" * 70)
    print("Capturing TikTok Profile API request using Playwright...")
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
            if 'api/post/item_list/' in request.url:
                captured_requests.append({
                    'url': request.url, 
                    'headers': request.headers
                })
                print(f"   ✓ Captured post/item_list request #{len(captured_requests)}")

        page.on('request', handle_request)

        try:
            print(f"\n1. Navigating to @{sample_username} profile...")
            page.goto(f'https://www.tiktok.com/@{sample_username}', 
                     wait_until='domcontentloaded', timeout=60000)
            time.sleep(3)

            print(f"\n2. Scrolling to trigger more API requests...")
            scrolls = 0
            while len(captured_requests) < min_requests and scrolls < 10:
                page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                scrolls += 1
                print(f"   Scroll {scrolls}: {len(captured_requests)} requests so far...")
                time.sleep(2)

            print(f"\n3. Total requests captured: {len(captured_requests)}")

            if not captured_requests:
                print("\n✗ No API requests captured")
                return None

            # Use the LAST request
            selected = captured_requests[-1]
            captured_url = selected['url']
            captured_headers = selected['headers']

            # Get cookies
            browser_cookies = context.cookies()
            cookies = {c['name']: c['value'] for c in browser_cookies}

            # Parse URL to preserve parameter order
            parsed = urlparse(captured_url)
            pairs = parse_qsl(parsed.query, keep_blank_values=True)

            session_data = {
                "cookies": cookies,
                "headers": captured_headers,
                "params": pairs  # List of tuples to preserve order
            }

            print(f"\n4. Session data captured:")
            print(f"   ✓ Cookies: {len(cookies)}")
            print(f"   ✓ Headers: {len(captured_headers)}")
            print(f"   ✓ Parameters: {len(pairs)}")

            return session_data

        except Exception as e:
            print(f"\n✗ Error: {e}")
            import traceback
            traceback.print_exc()
            return None
        finally:
            browser.close()


def main():
    """Main function to capture and save session"""
    session_data = capture_profile_session(sample_username="nike", min_requests=3)
    
    if session_data:
        output_file = "profile_session.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(session_data, f, indent=2)
        
        print("\n" + "=" * 70)
        print(f"✓ Session saved to {output_file}")
        print("=" * 70)
        print("\nYou can now run the profile scraper!")
    else:
        print("\n✗ Failed to capture session")


if __name__ == "__main__":
    main()