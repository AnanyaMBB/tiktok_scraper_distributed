# # #!/usr/bin/env python3
# # """Test direct conversion of curl command"""
# # from curl_cffi import requests

# # url = "https://www.tiktok.com/api/post/item_list/?WebIdLastTime=1736951461&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F142.0.0.0%20Safari%2F537.36%20Edg%2F142.0.0.0&channel=tiktok_web&cookie_enabled=true&count=35&coverFormat=2&cursor=0&data_collection_enabled=true&device_id=7460149314773288494&device_platform=web_pc&focus_state=true&history_len=3&is_fullscreen=false&is_page_visible=true&language=en&odinId=7478784916198065170&os=windows&priority_region=US&referer=&region=US&screen_height=1080&screen_width=1920&secUid=MS4wLjABAAAAuYqWobyva4J42slRnXv8wgmO_0pv9NozRrmQ0vk1v33qPL5_qCpyoR-P_KpYBg4e&tz_name=Asia%2FSeoul&user_is_login=true&video_encoding=mp4&webcast_language=en&msToken=RyhisauVXdxKv0O64DCfY4KB4b9r4ss_hDOwPW3GGCmCSv0loXbaFhRNkObBNc3VFqRrS0ECObGorQptfHkSAY_EKroVB3MiseTpS0xyvDlBLMVub9L2V1LkG6RyZ-w_iGphoH5rApAI_7EX0dWGbKQIIw==&X-Bogus=DFSzsIVOmDJANnUoCOpfi9E-pInq&X-Gnarly=MJeMDy64wG1J3lr-dAa4/xhuKoSPFGTGLmo0KMvEmEj-Z2zYVv8CYc9EgooS0YoL8J0vqmya9ogjxmyjZ5v98bxTdtyV0ohjm7IG/1axe5cgwYujAscD6/h7Ds9PSIjug-nG0YmGU-MisFG3zc5BD7nork6hxCeYtDM7RXN69oNy2lGWwHf/NZ1YnHA4aVx8kP5H11B3Ky5lGuf0flfwJRE10PiPbVx8smPvNVxs1ImvRAg/BK-7U4n9DMh4PLL3wkhd5K3HSnSZFyAhqVRHRZj-hLbNQPuLo7Nkr98OKJMGRIBAKz1AnB9BktB-BJNF9Tv="

# # headers = {
# #     "accept": "*/*",
# #     "accept-language": "en-US,en;q=0.9",
# #     "priority": "u=1, i",
# #     "referer": "https://www.tiktok.com/@lisen.tech",
# #     "sec-ch-ua": '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
# #     "sec-ch-ua-mobile": "?0",
# #     "sec-ch-ua-platform": '"Windows"',
# #     "sec-fetch-dest": "empty",
# #     "sec-fetch-mode": "cors",
# #     "sec-fetch-site": "same-origin",
# #     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"
# # }

# # cookies = {
# #     "cookie-consent": '{"optional":true,"ga":true,"af":true,"fbp":true,"lip":true,"bing":true,"ttads":true,"reddit":true,"hubspot":true,"version":"v10"}',
# #     "living_user_id": "149999902702",
# #     "tt_chain_token": "g/awArl40iOADD0hHi9e/Q==",
# #     "d_ticket": "578cfb16f8d0da5d1f57811147ae32c1d1e4c",
# #     "uid_tt": "91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8",
# #     "uid_tt_ss": "91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8",
# #     "sid_tt": "c6960424c3048f7c6e0978192e012638",
# #     "sessionid": "c6960424c3048f7c6e0978192e012638",
# #     "sessionid_ss": "c6960424c3048f7c6e0978192e012638",
# #     "store-idc": "alisg",
# #     "store-country-code": "kr",
# #     "store-country-code-src": "uid",
# #     "tt-target-idc": "alisg",
# #     "tt-target-idc-sign": "jHcAJBth816HHWGYqpllY256Vw_XVnCFfgixI3_n23HZ8S9rc7uuJBy3lnZ69b6Lr-1s8Y2GP1RyOFAqPJOkmhJiSPC3w_-kvcpRCMG2_Lukc7i4fz-oh6V_QQvmQDqNCgP8UsHB_H-doJa_c73ADQM1cdxzfZ8ShMmIAi3TjpWjbwpU7fD1CNP8jPvqwEwMooHsXIGzhim5NP6iPydcpPFF03qitP0iPfpmRE2oCW4wYgBudTEQda95IYFPRBKVzbVLpQXhLZzzDPlqx894-oZZmhCgLc9CNoCyMaIVZlHvZ_fmW1v33PGRqPJxhxJP3At6jquz1qa_0_2CqNQ9qvwgRP5N79WQz5vidtT7so8o53vUVPt8I6qO0nvM7r8JHo66L4i9-q_ThXG3-2na1yz2Hyn8L54_o4Dn-ETt55-Cx__sgsWvYPgp8TF5jYdO9NouUQMSWJ8gUvq42P_SOnHRse8eksZCOPOkESCKl-O7c7RtKFAI8kP2ltJ9E6e5",
# #     "ttwid": "1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1752014034%7Cba59cb191a734d94f19af0f0136fe84f44d8797f1d8dcacf49a9ae2f8747e9db",
# #     "_ga": "GA1.1.150342934.1752048579",
# #     "_fbp": "fb.1.1752048580728.1446697223",
# #     "_ga_NBFTJ2P3P3": "GS1.1.1752048579.1.1.1752048630.0.0.1773973896",
# #     "pre_country": "KR",
# #     "lang_type": "en",
# #     "tta_attr_id_mirror": "0.1755075598.7537992296453636097",
# #     "_tt_enable_cookie": "1",
# #     "ttcsid": "1755660196386::vRKZe4gsZbYCGZvSjeBW.1.1755660196386",
# #     "ttcsid_C97F14JC77U63IDI7U40": "1755660196385::1jScwBvAKvOay5Y3IDYq.1.1755660196625",
# #     "_ga_Y2RSHPPW88": "GS2.1.s1755660196$o1$g1$t1755660202$j0$l0$h858435056",
# #     "_ga_HV1FL86553": "GS2.1.s1755660196$o1$g0$t1755660202$j0$l0$h430147227",
# #     "_ttp": "31XBbVW8z3njdHMvhKmUgOZdYYp",
# #     "_ga_TEQXTT9FE4": "GS1.1.1756345152.1.1.1756345319.0.0.46985635",
# #     "sid_guard": "c6960424c3048f7c6e0978192e012638%7C1760468508%7C15552000%7CSun%2C+12-Apr-2026+19%3A01%3A48+GMT",
# #     "tt_session_tlb_tag": "sttt%7C4%7CxpYEJMMEj3xuCXgZLgEmOP_________fzOi7a8IbznWsP6_DCsp0-A9Tmjey7VZ_aYnyddUwa54%3D",
# #     "sid_ucp_v1": "1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA",
# #     "ssid_ucp_v1": "1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA",
# #     "tiktok_webapp_theme_source": "auto",
# #     "tiktok_webapp_theme": "dark",
# #     "delay_guest_mode_vid": "5",
# #     "tt_csrf_token": "xYWajjO9-89aI0fRrZo-yJnaslhIXLFs-kW8",
# #     "perf_feed_cache": '{"expireTimestamp":1763096400000,"itemIds":["7571659024123317518","7571600769183452437","7571630534619729154"]}',
# #     "store-country-sign": "MEIEDHTam-nuJKKbIbSH7QQgiM2-9blpYoiGl5Naw92th_0qzSOUCKDlY709fUJwfFwEEI6hZi2-p7gVYC9aLt1A5zM",
# #     "odin_tt": "dcb093ff589a43fa427f3779b690ffc532deb0af3d87a656d18c0caff53a1e09bbd472c3a1ad8bd33e483932d275889e3b488a8e92f2b36e516c9acd21b6363febc2ae08903ee387c425feee42c462fd",
# #     "msToken": "RyhisauVXdxKv0O64DCfY4KB4b9r4ss_hDOwPW3GGCmCSv0loXbaFhRNkObBNc3VFqRrS0ECObGorQptfHkSAY_EKroVB3MiseTpS0xyvDlBLMVub9L2V1LkG6RyZ-w_iGphoH5rApAI_7EX0dWGbKQIIw==",
# #     "passport_fe_beating_status": "false",
# #     "ttwid": "1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1762923750%7C999013bdc8124b401cb2d236d9dd57d5b5fc7730d2932fb50e5778987eedbd40"
# # }

# # print("Testing direct curl conversion...")
# # print(f"URL contains secUid: {'secUid=' in url}")
# # print()

# # response = requests.get(
# #     url,
# #     headers=headers,
# #     cookies=cookies,
# #     impersonate="chrome131",
# #     timeout=30
# # )

# # print(f"Status: {response.status_code}")
# # print(f"Content-Type: {response.headers.get('content-type')}")
# # print(f"Content-Length: {len(response.content)}")
# # print()

# # if response.status_code == 200 and len(response.content) > 0:
# #     try:
# #         data = response.json()
# #         if 'itemList' in data and data['itemList']:
# #             print(f"✅ SUCCESS! Got {len(data['itemList'])} videos")
# #             print(f"First video ID: {data['itemList'][0]['id']}")
# #         else:
# #             print("⚠️  Response is JSON but no itemList")
# #             print(f"Keys: {list(data.keys())}")
# #             if 'status_msg' in data:
# #                 print(f"Status message: {data['status_msg']}")
# #     except Exception as e:
# #         print(f"❌ Failed to parse JSON: {e}")
# #         print(f"Response preview: {response.text[:200]}")
# # else:
# #     print(f"❌ Failed - Status: {response.status_code}, Length: {len(response.content)}")
# #     if len(response.content) > 0:
# #         print(f"Preview: {response.text[:200]}")



# #!/usr/bin/env python3
# """
# Build a working session file from your working curl command.
# This preserves the exact working configuration.
# """
# import json
# from urllib.parse import urlparse, parse_qsl

# # Your WORKING curl URL (paste the latest one)
# WORKING_URL = "https://www.tiktok.com/api/post/item_list/?WebIdLastTime=1736951461&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F142.0.0.0%20Safari%2F537.36%20Edg%2F142.0.0.0&channel=tiktok_web&cookie_enabled=true&count=35&coverFormat=2&cursor=0&data_collection_enabled=true&device_id=7460149314773288494&device_platform=web_pc&focus_state=true&history_len=3&is_fullscreen=false&is_page_visible=true&language=en&odinId=7478784916198065170&os=windows&priority_region=US&referer=&region=US&screen_height=1080&screen_width=1920&secUid=MS4wLjABAAAAuYqWobyva4J42slRnXv8wgmO_0pv9NozRrmQ0vk1v33qPL5_qCpyoR-P_KpYBg4e&tz_name=Asia%2FSeoul&user_is_login=true&video_encoding=mp4&webcast_language=en&msToken=RyhisauVXdxKv0O64DCfY4KB4b9r4ss_hDOwPW3GGCmCSv0loXbaFhRNkObBNc3VFqRrS0ECObGorQptfHkSAY_EKroVB3MiseTpS0xyvDlBLMVub9L2V1LkG6RyZ-w_iGphoH5rApAI_7EX0dWGbKQIIw==&X-Bogus=DFSzsIVOmDJANnUoCOpfi9E-pInq&X-Gnarly=MJeMDy64wG1J3lr-dAa4/xhuKoSPFGTGLmo0KMvEmEj-Z2zYVv8CYc9EgooS0YoL8J0vqmya9ogjxmyjZ5v98bxTdtyV0ohjm7IG/1axe5cgwYujAscD6/h7Ds9PSIjug-nG0YmGU-MisFG3zc5BD7nork6hxCeYtDM7RXN69oNy2lGWwHf/NZ1YnHA4aVx8kP5H11B3Ky5lGuf0flfwJRE10PiPbVx8smPvNVxs1ImvRAg/BK-7U4n9DMh4PLL3wkhd5K3HSnSZFyAhqVRHRZj-hLbNQPuLo7Nkr98OKJMGRIBAKz1AnB9BktB-BJNF9Tv="

# # Your WORKING headers (from curl)
# WORKING_HEADERS = {
#     "accept": "*/*",
#     "accept-language": "en-US,en;q=0.9",
#     "priority": "u=1, i",
#     "referer": "https://www.tiktok.com/@lisen.tech",
#     "sec-ch-ua": '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": '"Windows"',
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-origin",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"
# }

# # Your WORKING cookies (from curl)
# WORKING_COOKIES = {
#     "cookie-consent": '{"optional":true,"ga":true,"af":true,"fbp":true,"lip":true,"bing":true,"ttads":true,"reddit":true,"hubspot":true,"version":"v10"}',
#     "living_user_id": "149999902702",
#     "tt_chain_token": "g/awArl40iOADD0hHi9e/Q==",
#     "d_ticket": "578cfb16f8d0da5d1f57811147ae32c1d1e4c",
#     "uid_tt": "91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8",
#     "uid_tt_ss": "91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8",
#     "sid_tt": "c6960424c3048f7c6e0978192e012638",
#     "sessionid": "c6960424c3048f7c6e0978192e012638",
#     "sessionid_ss": "c6960424c3048f7c6e0978192e012638",
#     "store-idc": "alisg",
#     "store-country-code": "kr",
#     "store-country-code-src": "uid",
#     "tt-target-idc": "alisg",
#     "tt-target-idc-sign": "jHcAJBth816HHWGYqpllY256Vw_XVnCFfgixI3_n23HZ8S9rc7uuJBy3lnZ69b6Lr-1s8Y2GP1RyOFAqPJOkmhJiSPC3w_-kvcpRCMG2_Lukc7i4fz-oh6V_QQvmQDqNCgP8UsHB_H-doJa_c73ADQM1cdxzfZ8ShMmIAi3TjpWjbwpU7fD1CNP8jPvqwEwMooHsXIGzhim5NP6iPydcpPFF03qitP0iPfpmRE2oCW4wYgBudTEQda95IYFPRBKVzbVLpQXhLZzzDPlqx894-oZZmhCgLc9CNoCyMaIVZlHvZ_fmW1v33PGRqPJxhxJP3At6jquz1qa_0_2CqNQ9qvwgRP5N79WQz5vidtT7so8o53vUVPt8I6qO0nvM7r8JHo66L4i9-q_ThXG3-2na1yz2Hyn8L54_o4Dn-ETt55-Cx__sgsWvYPgp8TF5jYdO9NouUQMSWJ8gUvq42P_SOnHRse8eksZCOPOkESCKl-O7c7RtKFAI8kP2ltJ9E6e5",
#     "ttwid": "1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1752014034%7Cba59cb191a734d94f19af0f0136fe84f44d8797f1d8dcacf49a9ae2f8747e9db",
#     "_ga": "GA1.1.150342934.1752048579",
#     "_fbp": "fb.1.1752048580728.1446697223",
#     "_ga_NBFTJ2P3P3": "GS1.1.1752048579.1.1.1752048630.0.0.1773973896",
#     "pre_country": "KR",
#     "lang_type": "en",
#     "tta_attr_id_mirror": "0.1755075598.7537992296453636097",
#     "_tt_enable_cookie": "1",
#     "ttcsid": "1755660196386::vRKZe4gsZbYCGZvSjeBW.1.1755660196386",
#     "ttcsid_C97F14JC77U63IDI7U40": "1755660196385::1jScwBvAKvOay5Y3IDYq.1.1755660196625",
#     "_ga_Y2RSHPPW88": "GS2.1.s1755660196$o1$g1$t1755660202$j0$l0$h858435056",
#     "_ga_HV1FL86553": "GS2.1.s1755660196$o1$g0$t1755660202$j0$l0$h430147227",
#     "_ttp": "31XBbVW8z3njdHMvhKmUgOZdYYp",
#     "_ga_TEQXTT9FE4": "GS1.1.1756345152.1.1.1756345319.0.0.46985635",
#     "sid_guard": "c6960424c3048f7c6e0978192e012638%7C1760468508%7C15552000%7CSun%2C+12-Apr-2026+19%3A01%3A48+GMT",
#     "tt_session_tlb_tag": "sttt%7C4%7CxpYEJMMEj3xuCXgZLgEmOP_________fzOi7a8IbznWsP6_DCsp0-A9Tmjey7VZ_aYnyddUwa54%3D",
#     "sid_ucp_v1": "1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA",
#     "ssid_ucp_v1": "1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA",
#     "tiktok_webapp_theme_source": "auto",
#     "tiktok_webapp_theme": "dark",
#     "delay_guest_mode_vid": "5",
#     "tt_csrf_token": "xYWajjO9-89aI0fRrZo-yJnaslhIXLFs-kW8",
#     "perf_feed_cache": '{"expireTimestamp":1763096400000,"itemIds":["7571659024123317518","7571600769183452437","7571630534619729154"]}',
#     "store-country-sign": "MEIEDHTam-nuJKKbIbSH7QQgiM2-9blpYoiGl5Naw92th_0qzSOUCKDlY709fUJwfFwEEI6hZi2-p7gVYC9aLt1A5zM",
#     "odin_tt": "dcb093ff589a43fa427f3779b690ffc532deb0af3d87a656d18c0caff53a1e09bbd472c3a1ad8bd33e483932d275889e3b488a8e92f2b36e516c9acd21b6363febc2ae08903ee387c425feee42c462fd",
#     "msToken": "RyhisauVXdxKv0O64DCfY4KB4b9r4ss_hDOwPW3GGCmCSv0loXbaFhRNkObBNc3VFqRrS0ECObGorQptfHkSAY_EKroVB3MiseTpS0xyvDlBLMVub9L2V1LkG6RyZ-w_iGphoH5rApAI_7EX0dWGbKQIIw==",
#     "passport_fe_beating_status": "false",
#     "ttwid": "1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1762923750%7C999013bdc8124b401cb2d236d9dd57d5b5fc7730d2932fb50e5778987eedbd40"
# }

# def main():
#     print("=" * 70)
#     print("Building session from working curl command...")
#     print("=" * 70)
    
#     # Parse the URL to extract parameters
#     parsed = urlparse(WORKING_URL)
#     params = parse_qsl(parsed.query, keep_blank_values=True)
    
#     print(f"\n✓ Extracted {len(params)} parameters")
#     print(f"✓ Using {len(WORKING_HEADERS)} headers")
#     print(f"✓ Using {len(WORKING_COOKIES)} cookies")
    
#     # Build session data
#     session_data = {
#         "cookies": WORKING_COOKIES,
#         "headers": WORKING_HEADERS,
#         "params": params
#     }
    
#     # Test it immediately
#     print("\n" + "=" * 70)
#     print("Testing session...")
#     print("=" * 70)
    
#     from curl_cffi import requests
    
#     response = requests.get(
#         WORKING_URL,
#         headers=WORKING_HEADERS,
#         cookies=WORKING_COOKIES,
#         impersonate="chrome131",
#         timeout=30
#     )
    
#     print(f"\nStatus: {response.status_code}")
#     print(f"Content-Length: {len(response.content)}")
    
#     if response.status_code == 200 and len(response.content) > 0:
#         try:
#             data = response.json()
#             if 'itemList' in data and data['itemList']:
#                 print(f"✅ TEST PASSED! Got {len(data['itemList'])} videos")
                
#                 # Save the session
#                 output_file = "profile_session.json"
#                 with open(output_file, 'w', encoding='utf-8') as f:
#                     json.dump(session_data, f, indent=2)
                
#                 print("\n" + "=" * 70)
#                 print(f"✅ Session saved to {output_file}")
#                 print("=" * 70)
#                 print("\nYou can now run the profile scraper!")
#                 return True
#             else:
#                 print(f"⚠️  Response has no itemList")
#                 print(f"Keys: {list(data.keys())}")
#                 return False
#         except Exception as e:
#             print(f"❌ Failed to parse JSON: {e}")
#             return False
#     else:
#         print(f"❌ TEST FAILED")
#         if len(response.content) > 0:
#             print(f"Response: {response.text[:200]}")
#         return False

# if __name__ == "__main__":
#     main()


from patchright.sync_api import sync_playwright

with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        user_data_dir="/tmp/test_proxy",
        channel="chrome",
        headless=False,  # Watch what happens
        proxy={
            "server": "http://gate.decodo.com:10001",
            "username": "spe2t84yz6",
            "password": "+jlyDjNahl1Rm868Fy",
        },
    )
    page = context.new_page()
    page.goto("https://httpbin.org/ip")  # Test with simple site first
    print(page.content())
    input("Press Enter to close...")
    context.close()