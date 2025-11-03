# import requests

# cookies = {
#     'cookie-consent': '{%22optional%22:true%2C%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22hubspot%22:true%2C%22version%22:%22v10%22}',
#     'living_user_id': '149999902702',
#     'tt_chain_token': 'g/awArl40iOADD0hHi9e/Q==',
#     'd_ticket': '578cfb16f8d0da5d1f57811147ae32c1d1e4c',
#     'uid_tt': '91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8',
#     'uid_tt_ss': '91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8',
#     'sid_tt': 'c6960424c3048f7c6e0978192e012638',
#     'sessionid': 'c6960424c3048f7c6e0978192e012638',
#     'sessionid_ss': 'c6960424c3048f7c6e0978192e012638',
#     'store-idc': 'alisg',
#     'store-country-code': 'kr',
#     'store-country-code-src': 'uid',
#     'tt-target-idc': 'alisg',
#     'tt-target-idc-sign': 'jHcAJBth816HHWGYqpllY256Vw_XVnCFfgixI3_n23HZ8S9rc7uuJBy3lnZ69b6Lr-1s8Y2GP1RyOFAqPJOkmhJiSPC3w_-kvcpRCMG2_Lukc7i4fz-oh6V_QQvmQDqNCgP8UsHB_H-doJa_c73ADQM1cdxzfZ8ShMmIAi3TjpWjbwpU7fD1CNP8jPvqwEwMooHsXIGzhim5NP6iPydcpPFF03qitP0iPfpmRE2oCW4wYgBudTEQda95IYFPRBKVzbVLpQXhLZzzDPlqx894-oZZmhCgLc9CNoCyMaIVZlHvZ_fmW1v33PGRqPJxhxJP3At6jquz1qa_0_2CqNQ9qvwgRP5N79WQz5vidtT7so8o53vUVPt8I6qO0nvM7r8JHo66L4i9-q_ThXG3-2na1yz2Hyn8L54_o4Dn-ETt55-Cx__sgsWvYPgp8TF5jYdO9NouUQMSWJ8gUvq42P_SOnHRse8eksZCOPOkESCKl-O7c7RtKFAI8kP2ltJ9E6e5',
#     'ttwid': '1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1752014034%7Cba59cb191a734d94f19af0f0136fe84f44d8797f1d8dcacf49a9ae2f8747e9db',
#     '_ga': 'GA1.1.150342934.1752048579',
#     '_fbp': 'fb.1.1752048580728.1446697223',
#     '_ga_NBFTJ2P3P3': 'GS1.1.1752048579.1.1.1752048630.0.0.1773973896',
#     'pre_country': 'KR',
#     'lang_type': 'en',
#     'tta_attr_id_mirror': '0.1755075598.7537992296453636097',
#     '_tt_enable_cookie': '1',
#     'ttcsid': '1755660196386::vRKZe4gsZbYCGZvSjeBW.1.1755660196386',
#     'ttcsid_C97F14JC77U63IDI7U40': '1755660196385::1jScwBvAKvOay5Y3IDYq.1.1755660196625',
#     '_ga_Y2RSHPPW88': 'GS2.1.s1755660196$o1$g1$t1755660202$j0$l0$h858435056',
#     '_ga_HV1FL86553': 'GS2.1.s1755660196$o1$g0$t1755660202$j0$l0$h430147227',
#     '_ttp': '31XBbVW8z3njdHMvhKmUgOZdYYp',
#     '_ga_TEQXTT9FE4': 'GS1.1.1756345152.1.1.1756345319.0.0.46985635',
#     'sid_guard': 'c6960424c3048f7c6e0978192e012638%7C1760468508%7C15552000%7CSun%2C+12-Apr-2026+19%3A01%3A48+GMT',
#     'tt_session_tlb_tag': 'sttt%7C4%7CxpYEJMMEj3xuCXgZLgEmOP_________fzOi7a8IbznWsP6_DCsp0-A9Tmjey7VZ_aYnyddUwa54%3D',
#     'sid_ucp_v1': '1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA',
#     'ssid_ucp_v1': '1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA',
#     'tiktok_webapp_theme_source': 'auto',
#     'tiktok_webapp_theme': 'dark',
#     'delay_guest_mode_vid': '5',
#     'tt_csrf_token': 'fC6X3ood-46AgqhdK-RE-KnY_vkvXjZPPdMY',
#     'perf_feed_cache': '{%22expireTimestamp%22:1762171200000%2C%22itemIds%22:[%227560011590322441502%22%2C%227565435256900209976%22%2C%227558870463225646348%22]}',
#     'store-country-sign': 'MEIEDNekO66OkaT4HZ9UaAQguHo4UC-k0yWjwtFWL_shAKDskxokVgRJPzOdsPjOnuMEEKvB2Pd0ULwLu80EKcusW1w',
#     'odin_tt': '4116507704e2237afd54221dada9494cab976af8df18049b36e7b0e4062e9b1151841138c0a2dfc8523da3167cefff11ff9452d6f74fb92f1b5f2789dd2b6066',
#     'msToken': 'se8Jrj22b-E5kSUNlPSNSgCo8c5uYEjGj3qOcIY7Ql4v_WPTYr2iy3vVt_YRt7E1jhJStsH1ReJYnNPiQnzKavqkBhdGR0XlOzmUv1NdgDB9bNZO6YX1ai7pesl_2UKVmIA-kFfMpsEHkeBb03QIoZwSXTk=',
#     'passport_fe_beating_status': 'false',
#     'msToken': 'AEGDQGTYjznUwuKAjjCPv-hNIGHWhdoQjnB5yJzpT7ZoAXaH9WYz0qLeBrDOoangFTku2O_2BsGnIDNP4k-Jd7eSov_P19ZIB0V-tPN5ZigSpyXRQzJxmWSW5lXF',
#     'ttwid': '1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1762001699%7C298db69a27f7c8414a09ba1fcc4eec483fe8a0bdd0b07858d6e05899fce3ac61',
# }

# headers = {
#     'accept': '*/*',
#     'accept-language': 'en-US,en;q=0.9',
#     'priority': 'u=1, i',
#     'referer': 'https://www.tiktok.com/',
#     'sec-ch-ua': '"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0',
#     'cookie': 'cookie-consent={%22optional%22:true%2C%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22hubspot%22:true%2C%22version%22:%22v10%22}; living_user_id=149999902702; tt_chain_token=g/awArl40iOADD0hHi9e/Q==; d_ticket=578cfb16f8d0da5d1f57811147ae32c1d1e4c; uid_tt=91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8; uid_tt_ss=91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8; sid_tt=c6960424c3048f7c6e0978192e012638; sessionid=c6960424c3048f7c6e0978192e012638; sessionid_ss=c6960424c3048f7c6e0978192e012638; store-idc=alisg; store-country-code=kr; store-country-code-src=uid; tt-target-idc=alisg; tt-target-idc-sign=jHcAJBth816HHWGYqpllY256Vw_XVnCFfgixI3_n23HZ8S9rc7uuJBy3lnZ69b6Lr-1s8Y2GP1RyOFAqPJOkmhJiSPC3w_-kvcpRCMG2_Lukc7i4fz-oh6V_QQvmQDqNCgP8UsHB_H-doJa_c73ADQM1cdxzfZ8ShMmIAi3TjpWjbwpU7fD1CNP8jPvqwEwMooHsXIGzhim5NP6iPydcpPFF03qitP0iPfpmRE2oCW4wYgBudTEQda95IYFPRBKVzbVLpQXhLZzzDPlqx894-oZZmhCgLc9CNoCyMaIVZlHvZ_fmW1v33PGRqPJxhxJP3At6jquz1qa_0_2CqNQ9qvwgRP5N79WQz5vidtT7so8o53vUVPt8I6qO0nvM7r8JHo66L4i9-q_ThXG3-2na1yz2Hyn8L54_o4Dn-ETt55-Cx__sgsWvYPgp8TF5jYdO9NouUQMSWJ8gUvq42P_SOnHRse8eksZCOPOkESCKl-O7c7RtKFAI8kP2ltJ9E6e5; ttwid=1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1752014034%7Cba59cb191a734d94f19af0f0136fe84f44d8797f1d8dcacf49a9ae2f8747e9db; _ga=GA1.1.150342934.1752048579; _fbp=fb.1.1752048580728.1446697223; _ga_NBFTJ2P3P3=GS1.1.1752048579.1.1.1752048630.0.0.1773973896; pre_country=KR; lang_type=en; tta_attr_id_mirror=0.1755075598.7537992296453636097; _tt_enable_cookie=1; ttcsid=1755660196386::vRKZe4gsZbYCGZvSjeBW.1.1755660196386; ttcsid_C97F14JC77U63IDI7U40=1755660196385::1jScwBvAKvOay5Y3IDYq.1.1755660196625; _ga_Y2RSHPPW88=GS2.1.s1755660196$o1$g1$t1755660202$j0$l0$h858435056; _ga_HV1FL86553=GS2.1.s1755660196$o1$g0$t1755660202$j0$l0$h430147227; _ttp=31XBbVW8z3njdHMvhKmUgOZdYYp; _ga_TEQXTT9FE4=GS1.1.1756345152.1.1.1756345319.0.0.46985635; sid_guard=c6960424c3048f7c6e0978192e012638%7C1760468508%7C15552000%7CSun%2C+12-Apr-2026+19%3A01%3A48+GMT; tt_session_tlb_tag=sttt%7C4%7CxpYEJMMEj3xuCXgZLgEmOP_________fzOi7a8IbznWsP6_DCsp0-A9Tmjey7VZ_aYnyddUwa54%3D; sid_ucp_v1=1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA; ssid_ucp_v1=1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA; tiktok_webapp_theme_source=auto; tiktok_webapp_theme=dark; delay_guest_mode_vid=5; tt_csrf_token=fC6X3ood-46AgqhdK-RE-KnY_vkvXjZPPdMY; perf_feed_cache={%22expireTimestamp%22:1762171200000%2C%22itemIds%22:[%227560011590322441502%22%2C%227565435256900209976%22%2C%227558870463225646348%22]}; store-country-sign=MEIEDNekO66OkaT4HZ9UaAQguHo4UC-k0yWjwtFWL_shAKDskxokVgRJPzOdsPjOnuMEEKvB2Pd0ULwLu80EKcusW1w; odin_tt=4116507704e2237afd54221dada9494cab976af8df18049b36e7b0e4062e9b1151841138c0a2dfc8523da3167cefff11ff9452d6f74fb92f1b5f2789dd2b6066; msToken=se8Jrj22b-E5kSUNlPSNSgCo8c5uYEjGj3qOcIY7Ql4v_WPTYr2iy3vVt_YRt7E1jhJStsH1ReJYnNPiQnzKavqkBhdGR0XlOzmUv1NdgDB9bNZO6YX1ai7pesl_2UKVmIA-kFfMpsEHkeBb03QIoZwSXTk=; passport_fe_beating_status=false; msToken=AEGDQGTYjznUwuKAjjCPv-hNIGHWhdoQjnB5yJzpT7ZoAXaH9WYz0qLeBrDOoangFTku2O_2BsGnIDNP4k-Jd7eSov_P19ZIB0V-tPN5ZigSpyXRQzJxmWSW5lXF; ttwid=1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1762001699%7C298db69a27f7c8414a09ba1fcc4eec483fe8a0bdd0b07858d6e05899fce3ac61',
# }

# response = requests.get(
#     'https://www.tiktok.com/api/recommend/item_list/?WebIdLastTime=1736951461&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F141.0.0.0%20Safari%2F537.36%20Edg%2F141.0.0.0&channel=tiktok_web&clientABVersions=74800760%2C70508271%2C72437276%2C73720540%2C74250915%2C74367308%2C74393673%2C74446915%2C74465399%2C74465409%2C74536864%2C74609147%2C74627577%2C74632791%2C74674280%2C74676351%2C74679798%2C74686502%2C74700792%2C74703727%2C74711111%2C74733472%2C74746519%2C74746610%2C74757744%2C74767144%2C74767851%2C74782564%2C74792133%2C74793837%2C74798337%2C74798356%2C74808329%2C74810092%2C74811360%2C74819402%2C74824020%2C74872266%2C74882809%2C70138197%2C70156809%2C70405643%2C71057832%2C71200802%2C71381811%2C71516509%2C71803300%2C71962127%2C72360691%2C72408100%2C72854054%2C72892778%2C73004916%2C73171280%2C73208420%2C73989921%2C74276218%2C74844724&cookie_enabled=true&count=6&coverFormat=2&cpu_core_number=12&dark_mode=false&data_collection_enabled=true&day_of_week=6&device_id=7460149314773288494&device_platform=web_pc&device_score=8.57&device_type=web_h264&enable_cache=false&focus_state=true&from_page=fyp&history_len=2&isNonPersonalized=false&is_fullscreen=false&is_page_visible=true&itemID=&language=en&launch_mode=direct&network=10&odinId=7478784916198065170&os=windows&priority_region=KR&pullType=1&referer=&region=KR&screen_height=1080&screen_width=1920&showAboutThisAd=true&showAds=true&time_of_day=21&tz_name=Asia%2FSeoul&video_encoding=&vv_count=12529&vv_count_fyp=2637&watchLiveLastTime=1741102304984&webcast_language=en&window_height=963&window_width=165&msToken=se8Jrj22b-E5kSUNlPSNSgCo8c5uYEjGj3qOcIY7Ql4v_WPTYr2iy3vVt_YRt7E1jhJStsH1ReJYnNPiQnzKavqkBhdGR0XlOzmUv1NdgDB9bNZO6YX1ai7pesl_2UKVmIA-kFfMpsEHkeBb03QIoZwSXTk=&X-Bogus=DFSzsIVOFbvANaQoCPBZ3Q-YnjPe&X-Gnarly=MRplt5vBUafcU6/ysUJmzy6qik43h4f34sH-NSqWbuIZ0XJ9abx/m8UJ4KWJus2fTvTAU4sEa1uoOym4tPgYepqyoXC-rHpjHETivv2oSwlXxNFxU0yjh-shRUvT8/gHSQMfemOJrs/k3pxmTCp3nN3PYyd6QPk9IUyF2RrBryy9WB1msl4iixJRRhUG1xqQJttjGe7Zb4eBmvE7jXjFpC957ujEU-v9G/0h0Kkg-Y-M2wUS5BxQmsVDH6Tksn4w7VxfdF7nEL-lOwxZK-jcXma9JTEzfTuDm1U49u65XePGhjrQ0OLZlBenK//9Rszp9wZ=',
#     cookies=cookies,
#     headers=headers,
# )


# print(response.content)

# with open("save.json", "wb") as file:
#     file.write(response.content)



import requests

cookies = {
    'cookie-consent': '{%22optional%22:true%2C%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22hubspot%22:true%2C%22version%22:%22v10%22}',
    'living_user_id': '149999902702',
    'tt_chain_token': 'g/awArl40iOADD0hHi9e/Q==',
    'd_ticket': '578cfb16f8d0da5d1f57811147ae32c1d1e4c',
    'uid_tt': '91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8',
    'uid_tt_ss': '91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8',
    'sid_tt': 'c6960424c3048f7c6e0978192e012638',
    'sessionid': 'c6960424c3048f7c6e0978192e012638',
    'sessionid_ss': 'c6960424c3048f7c6e0978192e012638',
    'store-idc': 'alisg',
    'store-country-code': 'kr',
    'store-country-code-src': 'uid',
    'tt-target-idc': 'alisg',
    'tt-target-idc-sign': 'jHcAJBth816HHWGYqpllY256Vw_XVnCFfgixI3_n23HZ8S9rc7uuJBy3lnZ69b6Lr-1s8Y2GP1RyOFAqPJOkmhJiSPC3w_-kvcpRCMG2_Lukc7i4fz-oh6V_QQvmQDqNCgP8UsHB_H-doJa_c73ADQM1cdxzfZ8ShMmIAi3TjpWjbwpU7fD1CNP8jPvqwEwMooHsXIGzhim5NP6iPydcpPFF03qitP0iPfpmRE2oCW4wYgBudTEQda95IYFPRBKVzbVLpQXhLZzzDPlqx894-oZZmhCgLc9CNoCyMaIVZlHvZ_fmW1v33PGRqPJxhxJP3At6jquz1qa_0_2CqNQ9qvwgRP5N79WQz5vidtT7so8o53vUVPt8I6qO0nvM7r8JHo66L4i9-q_ThXG3-2na1yz2Hyn8L54_o4Dn-ETt55-Cx__sgsWvYPgp8TF5jYdO9NouUQMSWJ8gUvq42P_SOnHRse8eksZCOPOkESCKl-O7c7RtKFAI8kP2ltJ9E6e5',
    'ttwid': '1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1752014034%7Cba59cb191a734d94f19af0f0136fe84f44d8797f1d8dcacf49a9ae2f8747e9db',
    '_ga': 'GA1.1.150342934.1752048579',
    '_fbp': 'fb.1.1752048580728.1446697223',
    '_ga_NBFTJ2P3P3': 'GS1.1.1752048579.1.1.1752048630.0.0.1773973896',
    'pre_country': 'KR',
    'lang_type': 'en',
    'tta_attr_id_mirror': '0.1755075598.7537992296453636097',
    '_tt_enable_cookie': '1',
    'ttcsid': '1755660196386::vRKZe4gsZbYCGZvSjeBW.1.1755660196386',
    'ttcsid_C97F14JC77U63IDI7U40': '1755660196385::1jScwBvAKvOay5Y3IDYq.1.1755660196625',
    '_ga_Y2RSHPPW88': 'GS2.1.s1755660196$o1$g1$t1755660202$j0$l0$h858435056',
    '_ga_HV1FL86553': 'GS2.1.s1755660196$o1$g0$t1755660202$j0$l0$h430147227',
    '_ttp': '31XBbVW8z3njdHMvhKmUgOZdYYp',
    '_ga_TEQXTT9FE4': 'GS1.1.1756345152.1.1.1756345319.0.0.46985635',
    'sid_guard': 'c6960424c3048f7c6e0978192e012638%7C1760468508%7C15552000%7CSun%2C+12-Apr-2026+19%3A01%3A48+GMT',
    'tt_session_tlb_tag': 'sttt%7C4%7CxpYEJMMEj3xuCXgZLgEmOP_________fzOi7a8IbznWsP6_DCsp0-A9Tmjey7VZ_aYnyddUwa54%3D',
    'sid_ucp_v1': '1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA',
    'ssid_ucp_v1': '1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA',
    'tiktok_webapp_theme_source': 'auto',
    'tiktok_webapp_theme': 'dark',
    'delay_guest_mode_vid': '5',
    'tt_csrf_token': 'xYWajjO9-89aI0fRrZo-yJnaslhIXLFs-kW8',
    'store-country-sign': 'MEIEDBKdqGvnG5UAo5FXbwQgAm15FzxCZRJzVE_IqmgWlnlT7svrenSYBbR9w-g-oRsEEF7CnPC1TU3oVf8kCi26MV4',
    'msToken': 'Xb5ISAL1qu4crHwjKKLRrctkVp1TEq5L-n_n90700NHS_cRZewdWtNn08cFvXpfj86NB79ISVgXL0ZJ4Ar5wbwp5QQsyafQl8i8Jocj24HK2v_F8llI3Jr3WmR1of_6wKdXt6rywsxWWStV_r-baiy_dnw==',
    'odin_tt': '55702be48b513482b777bcd6455e0453a917564e2ca5250690bf55a79a7e9972359024426402e79fb654913da3e1b60ab52fd8d6fbe071f3a91cafe0d0a83e3c',
    'passport_fe_beating_status': 'false',
    'msToken': '8ub9MWDYuXZFOp0RDsLUPEXhzk4vpC55-h_rTrpJWH3fqkbiDMXiFwWmlbEl6WDUxEwmB3lCdcdMU-x7jd2AZsVBLzmUHb8bD76wuSnxizDTDg1BCgELK3neEir7sjQHoOV2nD6T8jkpgqiU4z6_HGmOgA==',
    'perf_feed_cache': '{%22expireTimestamp%22:1762351200000%2C%22itemIds%22:[%227565222614025686285%22%2C%227553551072632147211%22%2C%227567781083329170701%22]}',
    'ttwid': '1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1762180132%7C03a7156af52f7028f1bd89d5799983d4e24445a7d55aec361f1c84fce271bbc0',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'priority': 'u=1, i',
    'referer': 'https://www.tiktok.com/',
    'sec-ch-ua': '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',
    # 'cookie': 'cookie-consent={%22optional%22:true%2C%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22hubspot%22:true%2C%22version%22:%22v10%22}; living_user_id=149999902702; tt_chain_token=g/awArl40iOADD0hHi9e/Q==; d_ticket=578cfb16f8d0da5d1f57811147ae32c1d1e4c; uid_tt=91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8; uid_tt_ss=91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8; sid_tt=c6960424c3048f7c6e0978192e012638; sessionid=c6960424c3048f7c6e0978192e012638; sessionid_ss=c6960424c3048f7c6e0978192e012638; store-idc=alisg; store-country-code=kr; store-country-code-src=uid; tt-target-idc=alisg; tt-target-idc-sign=jHcAJBth816HHWGYqpllY256Vw_XVnCFfgixI3_n23HZ8S9rc7uuJBy3lnZ69b6Lr-1s8Y2GP1RyOFAqPJOkmhJiSPC3w_-kvcpRCMG2_Lukc7i4fz-oh6V_QQvmQDqNCgP8UsHB_H-doJa_c73ADQM1cdxzfZ8ShMmIAi3TjpWjbwpU7fD1CNP8jPvqwEwMooHsXIGzhim5NP6iPydcpPFF03qitP0iPfpmRE2oCW4wYgBudTEQda95IYFPRBKVzbVLpQXhLZzzDPlqx894-oZZmhCgLc9CNoCyMaIVZlHvZ_fmW1v33PGRqPJxhxJP3At6jquz1qa_0_2CqNQ9qvwgRP5N79WQz5vidtT7so8o53vUVPt8I6qO0nvM7r8JHo66L4i9-q_ThXG3-2na1yz2Hyn8L54_o4Dn-ETt55-Cx__sgsWvYPgp8TF5jYdO9NouUQMSWJ8gUvq42P_SOnHRse8eksZCOPOkESCKl-O7c7RtKFAI8kP2ltJ9E6e5; ttwid=1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1752014034%7Cba59cb191a734d94f19af0f0136fe84f44d8797f1d8dcacf49a9ae2f8747e9db; _ga=GA1.1.150342934.1752048579; _fbp=fb.1.1752048580728.1446697223; _ga_NBFTJ2P3P3=GS1.1.1752048579.1.1.1752048630.0.0.1773973896; pre_country=KR; lang_type=en; tta_attr_id_mirror=0.1755075598.7537992296453636097; _tt_enable_cookie=1; ttcsid=1755660196386::vRKZe4gsZbYCGZvSjeBW.1.1755660196386; ttcsid_C97F14JC77U63IDI7U40=1755660196385::1jScwBvAKvOay5Y3IDYq.1.1755660196625; _ga_Y2RSHPPW88=GS2.1.s1755660196$o1$g1$t1755660202$j0$l0$h858435056; _ga_HV1FL86553=GS2.1.s1755660196$o1$g0$t1755660202$j0$l0$h430147227; _ttp=31XBbVW8z3njdHMvhKmUgOZdYYp; _ga_TEQXTT9FE4=GS1.1.1756345152.1.1.1756345319.0.0.46985635; sid_guard=c6960424c3048f7c6e0978192e012638%7C1760468508%7C15552000%7CSun%2C+12-Apr-2026+19%3A01%3A48+GMT; tt_session_tlb_tag=sttt%7C4%7CxpYEJMMEj3xuCXgZLgEmOP_________fzOi7a8IbznWsP6_DCsp0-A9Tmjey7VZ_aYnyddUwa54%3D; sid_ucp_v1=1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA; ssid_ucp_v1=1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA; tiktok_webapp_theme_source=auto; tiktok_webapp_theme=dark; delay_guest_mode_vid=5; tt_csrf_token=xYWajjO9-89aI0fRrZo-yJnaslhIXLFs-kW8; store-country-sign=MEIEDBKdqGvnG5UAo5FXbwQgAm15FzxCZRJzVE_IqmgWlnlT7svrenSYBbR9w-g-oRsEEF7CnPC1TU3oVf8kCi26MV4; msToken=Xb5ISAL1qu4crHwjKKLRrctkVp1TEq5L-n_n90700NHS_cRZewdWtNn08cFvXpfj86NB79ISVgXL0ZJ4Ar5wbwp5QQsyafQl8i8Jocj24HK2v_F8llI3Jr3WmR1of_6wKdXt6rywsxWWStV_r-baiy_dnw==; odin_tt=55702be48b513482b777bcd6455e0453a917564e2ca5250690bf55a79a7e9972359024426402e79fb654913da3e1b60ab52fd8d6fbe071f3a91cafe0d0a83e3c; passport_fe_beating_status=false; msToken=8ub9MWDYuXZFOp0RDsLUPEXhzk4vpC55-h_rTrpJWH3fqkbiDMXiFwWmlbEl6WDUxEwmB3lCdcdMU-x7jd2AZsVBLzmUHb8bD76wuSnxizDTDg1BCgELK3neEir7sjQHoOV2nD6T8jkpgqiU4z6_HGmOgA==; perf_feed_cache={%22expireTimestamp%22:1762351200000%2C%22itemIds%22:[%227565222614025686285%22%2C%227553551072632147211%22%2C%227567781083329170701%22]}; ttwid=1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1762180132%7C03a7156af52f7028f1bd89d5799983d4e24445a7d55aec361f1c84fce271bbc0',
}

response = requests.get(
    'https://www.tiktok.com/api/recommend/item_list/?WebIdLastTime=1736951461&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F142.0.0.0%20Safari%2F537.36%20Edg%2F142.0.0.0&channel=tiktok_web&clientABVersions=74800760%2C70508271%2C72437276%2C73720540%2C74250915%2C74393673%2C74446915%2C74465399%2C74465409%2C74536864%2C74609147%2C74627577%2C74632791%2C74674280%2C74676351%2C74679798%2C74686502%2C74700792%2C74703727%2C74711111%2C74733472%2C74746519%2C74746610%2C74757744%2C74767144%2C74767851%2C74782564%2C74792133%2C74793837%2C74798337%2C74798356%2C74808329%2C74810092%2C74811360%2C74819402%2C74824020%2C74872266%2C74882809%2C70138197%2C70156809%2C70405643%2C71057832%2C71200802%2C71381811%2C71516509%2C71803300%2C71962127%2C72360691%2C72408100%2C72854054%2C72892778%2C73004916%2C73171280%2C73208420%2C73989921%2C74276218%2C74844724&cookie_enabled=true&count=6&coverFormat=2&cpu_core_number=12&dark_mode=false&data_collection_enabled=true&day_of_week=1&device_id=7460149314773288494&device_platform=web_pc&device_score=8.57&device_type=web_h264&enable_cache=false&focus_state=true&from_page=fyp&history_len=2&isNonPersonalized=false&is_fullscreen=false&is_page_visible=true&itemID=&language=en&launch_mode=direct&network=10&odinId=7478784916198065170&os=windows&priority_region=KR&pullType=1&referer=&region=KR&screen_height=1080&screen_width=1920&showAboutThisAd=true&showAds=true&time_of_day=23&tz_name=Asia%2FSeoul&video_encoding=&vv_count=12529&vv_count_fyp=2637&watchLiveLastTime=1741102304984&webcast_language=en&window_height=962&window_width=150&msToken=Xb5ISAL1qu4crHwjKKLRrctkVp1TEq5L-n_n90700NHS_cRZewdWtNn08cFvXpfj86NB79ISVgXL0ZJ4Ar5wbwp5QQsyafQl8i8Jocj24HK2v_F8llI3Jr3WmR1of_6wKdXt6rywsxWWStV_r-baiy_dnw==&X-Bogus=DFSzsIVYt2tANH/ACPJVwimpF2W/&X-Gnarly=Mw1bQHB/564boDbZQP6s-ShaK79iOfgOU57EoHgX55VO37v9-rSjMDEUveU9Nfm5dxJhESWUyRv4djcH4XUtOYukfRsLuySJRYRPMg37l9HL0XBOV0uTQJuCiwefkvLfYgShxDL-m543VJlr2-f2HHDjhsnNo6F10fQWHlSqptwrCQCKoyBctGFyOMd/cKJpCHGAvva4IxMPEQVXKqALpvG90JdQ4ERuMgAs11wKA97EXkbVCZigzSSJPsJFTwxkiF9SYENojM6LDiv2DEBH-1jU4pOll-gPUyLf0bY1IfEricLsZqdGwDDIhWCWS8EYYPz=',
    cookies=cookies,
    headers=headers,
)


print(response.content)


'https://www.tiktok.com/api/recommend/item_list/?WebIdLastTime=1736951461&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F142.0.0.0%20Safari%2F537.36%20Edg%2F142.0.0.0&channel=tiktok_web&clientABVersions=74800760%2C70508271%2C72437276%2C73720540%2C74250915%2C74393673%2C74446915%2C74465399%2C74465409%2C74536864%2C74609147%2C74627577%2C74632791%2C74674280%2C74676351%2C74679798%2C74686502%2C74700792%2C74703727%2C74711111%2C74733472%2C74746519%2C74746610%2C74757744%2C74767144%2C74767851%2C74782564%2C74792133%2C74793837%2C74798337%2C74798356%2C74808329%2C74810092%2C74811360%2C74819402%2C74824020%2C74872266%2C74882809%2C70138197%2C70156809%2C70405643%2C71057832%2C71200802%2C71381811%2C71516509%2C71803300%2C71962127%2C72360691%2C72408100%2C72854054%2C72892778%2C73004916%2C73171280%2C73208420%2C73989921%2C74276218%2C74844724&cookie_enabled=true&count=6&coverFormat=2&cpu_core_number=12&dark_mode=false&data_collection_enabled=true&day_of_week=1&device_id=7460149314773288494&device_platform=web_pc&device_score=8.57&device_type=web_h264&enable_cache=false&focus_state=true&from_page=fyp&history_len=2&isNonPersonalized=false&is_fullscreen=false&is_page_visible=true&itemID=&language=en&launch_mode=direct&network=10&odinId=7478784916198065170&os=windows&priority_region=KR&pullType=1&referer=&region=KR&screen_height=1080&screen_width=1920&showAboutThisAd=true&showAds=true&time_of_day=23&tz_name=Asia%2FSeoul&video_encoding=&vv_count=12529&vv_count_fyp=2637&watchLiveLastTime=1741102304984&webcast_language=en&window_height=962&window_width=150&msToken=Xb5ISAL1qu4crHwjKKLRrctkVp1TEq5L-n_n90700NHS_cRZewdWtNn08cFvXpfj86NB79ISVgXL0ZJ4Ar5wbwp5QQsyafQl8i8Jocj24HK2v_F8llI3Jr3WmR1of_6wKdXt6rywsxWWStV_r-baiy_dnw%3D%3D&X-Bogus=DFSzsIVYt2tANH/ACPJVwimpF2W/&X-Gnarly=Mw1bQHB/564boDbZQP6s-ShaK79iOfgOU57EoHgX55VO37v9-rSjMDEUveU9Nfm5dxJhESWUyRv4djcH4XUtOYukfRsLuySJRYRPMg37l9HL0XBOV0uTQJuCiwefkvLfYgShxDL-m543VJlr2-f2HHDjhsnNo6F10fQWHlSqptwrCQCKoyBctGFyOMd/cKJpCHGAvva4IxMPEQVXKqALpvG90JdQ4ERuMgAs11wKA97EXkbVCZigzSSJPsJFTwxkiF9SYENojM6LDiv2DEBH-1jU4pOll-gPUyLf0bY1IfEricLsZqdGwDDIhWCWS8EYYPz='