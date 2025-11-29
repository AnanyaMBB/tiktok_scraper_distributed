#!/usr/bin/env python3
"""
Script to capture TikTok profile session data and save it to a file.
This captures with real browser headers (not HeadlessChrome).
"""
import json
import time
from urllib.parse import urlparse, parse_qsl
from playwright.sync_api import sync_playwright
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "shared"))
from storage import upload_file
from proxy import get_datacenter_proxy



def capture_profile_session(sample_username="nike", min_requests=3):
    """Capture session data from a TikTok profile"""
    print("=" * 70)
    print("Capturing TikTok Profile API request using Playwright...")
    print("=" * 70)

    with sync_playwright() as p:
        print(get_datacenter_proxy())
        # Launch with specific args to avoid detection
        browser = p.chromium.launch(
            headless=False,  # Run visible browser
            proxy={
                "server": "http://gate.decodo.com:10001", 
                "username": "spe2t84yz6", 
                "password": "+jlyDjNahl1Rm868Fy", 
            },
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
                '--disable-web-security',
                '--no-sandbox'
            ]
        )
        
        # Use real Chrome user agent (not HeadlessChrome)
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
            locale='en-US',
            timezone_id='America/New_York',
            extra_http_headers={
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin'
            }
        )
        
        # Add script to remove webdriver flag
        context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => false
            });
        """)
        
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
            
            print(f"\n2. Waiting for page to fully load...")
            time.sleep(5)

            print(f"\n3. Scrolling to trigger more API requests...")
            scrolls = 0
            while len(captured_requests) < min_requests and scrolls < 15:
                page.evaluate("window.scrollBy(0, window.innerHeight)")
                scrolls += 1
                print(f"   Scroll {scrolls}: {len(captured_requests)} requests so far...")
                time.sleep(2)

            print(f"\n4. Total requests captured: {len(captured_requests)}")

            if not captured_requests:
                print("\n✗ No API requests captured")
                print("   Try running with headless=False and manually scroll")
                return None

            # Use the LAST request (most recent)
            selected = captured_requests[-1]
            captured_url = selected['url']
            captured_headers = selected['headers']

            print(f"\n5. Selected request #{len(captured_requests)} (the last one)")

            # Get cookies from browser
            browser_cookies = context.cookies()
            cookies = {c['name']: c['value'] for c in browser_cookies}

            print(f"\n6. Extracted {len(cookies)} cookies")

            # Show important cookies
            important = ['ttwid', 'msToken', 'sid_tt', 'sessionid', 'odin_tt']
            for name in important:
                if name in cookies:
                    val = cookies[name]
                    display = val[:40] + '...' if len(val) > 40 else val
                    print(f"   ✓ {name}: {display}")

            # Parse URL to preserve exact parameter order
            parsed = urlparse(captured_url)
            params = parse_qsl(parsed.query, keep_blank_values=True)

            print(f"\n7. Captured {len(params)} URL parameters in original order")

            # Build proper headers dict (add missing headers)
            final_headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'priority': 'u=1, i',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin'
            }
            
            # Add captured headers (overwrite defaults)
            for key, value in captured_headers.items():
                final_headers[key] = value

            # Make sure we don't have HeadlessChrome
            if 'sec-ch-ua' in final_headers and 'HeadlessChrome' in final_headers['sec-ch-ua']:
                final_headers['sec-ch-ua'] = '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"'
                print("\n   ⚠️  Fixed HeadlessChrome in sec-ch-ua header")

            print(f"\n8. Built {len(final_headers)} headers")
            print(f"   User-Agent: {final_headers.get('user-agent', 'N/A')[:60]}...")
            print(f"   sec-ch-ua: {final_headers.get('sec-ch-ua', 'N/A')[:60]}...")

            session_data = {
                "cookies": cookies,
                "headers": final_headers,
                "params": params
            }

            return session_data

        except Exception as e:
            print(f"\n✗ Error: {e}")
            import traceback
            traceback.print_exc()
            return None
        finally:
            print(f"\n9. Closing browser...")
            # time.sleep(120)
            browser.close()


def test_session(session_data):
    """Test if the captured session works"""
    from curl_cffi import requests
    from urllib.parse import quote
    
    cookies = session_data["cookies"]
    headers = session_data["headers"]
    params = session_data["params"]
    
    # Reconstruct URL exactly as captured
    def encode_pair(k, v):
        sig_keys = {"msToken", "X-Bogus", "X-Gnarly"}
        if k in sig_keys:
            return f"{quote(k, safe='')}={quote(v, safe='/=')}"
        return f"{quote(k, safe='')}={quote(v, safe='')}"
    
    query = "&".join(encode_pair(k, v) for k, v in params)
    url = f"https://www.tiktok.com/api/post/item_list/?{query}"
    
    print(f"\n{'='*70}")
  
    print("constructed cookies: ", cookies)
    
    try:
        response = requests.get(
            url,
            headers=headers,
            cookies=cookies,
            impersonate="chrome131",
            timeout=30
        )
        
        print(f"Status: {response.status_code}")
        print(f"Content-Length: {len(response.content)}")
        
        if response.status_code == 200 and len(response.content) > 0:
            try:
                data = response.json()
                if 'itemList' in data and data['itemList']:
                    print(f"✅ TEST PASSED! Got {len(data['itemList'])} videos")
                    return True
                else:
                    print(f"⚠️  Response has no itemList")
                    print(f"Keys: {list(data.keys())}")
                    return False
            except Exception as e:
                print(f"❌ Failed to parse JSON: {e}")
                return False
        elif len(response.content) == 0:
            print(f"❌ Empty response - session invalid or tokens expired")
            return False
        else:
            print(f"❌ Bad status code")
            return False
            
    except Exception as e:
        print(f"❌ TEST FAILED: {e}")
        return False


def main():
    """Main function to capture and save session"""
    print("\n" + "=" * 70)
    print("  TikTok Profile Session Capture Tool")
    print("=" * 70)
    print("\nThis will open a browser window and capture the session.")
    print("The browser will visit a TikTok profile and scroll automatically.\n")
    
    # Capture session
    session_data = capture_profile_session(sample_username="nike", min_requests=3)
    
    if session_data:
        # Test immediately
        if test_session(session_data):
            # Save if test passed
            output_file = "profile_session.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(session_data, f, indent=2)
            
            print("\n" + "=" * 70)
            print(f"✅ Session saved to {output_file}")
            print("=" * 70)
            print("\nYou can now run the profile scraper!")
        else:
            print("\n" + "=" * 70)
            print("❌ Session NOT saved - test failed")
            print("=" * 70)
            print("\nThe session was captured but doesn't work.")
            print("This usually means:")
            print("  1. TikTok detected automation (try again)")
            print("  2. Need to use a logged-in account")
            print("  3. Try manual curl capture instead")
    else:
        print("\n✗ Failed to capture session")


if __name__ == "__main__":
    main()