# # # import requests

# # # cookies = {
# # #     'cookie-consent': '{%22optional%22:true%2C%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22hubspot%22:true%2C%22version%22:%22v10%22}',
# # #     'living_user_id': '149999902702',
# # #     'tt_chain_token': 'g/awArl40iOADD0hHi9e/Q==',
# # #     'd_ticket': '578cfb16f8d0da5d1f57811147ae32c1d1e4c',
# # #     'uid_tt': '91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8',
# # #     'uid_tt_ss': '91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8',
# # #     'sid_tt': 'c6960424c3048f7c6e0978192e012638',
# # #     'sessionid': 'c6960424c3048f7c6e0978192e012638',
# # #     'sessionid_ss': 'c6960424c3048f7c6e0978192e012638',
# # #     'store-idc': 'alisg',
# # #     'store-country-code': 'kr',
# # #     'store-country-code-src': 'uid',
# # #     'tt-target-idc': 'alisg',
# # #     'tt-target-idc-sign': 'jHcAJBth816HHWGYqpllY256Vw_XVnCFfgixI3_n23HZ8S9rc7uuJBy3lnZ69b6Lr-1s8Y2GP1RyOFAqPJOkmhJiSPC3w_-kvcpRCMG2_Lukc7i4fz-oh6V_QQvmQDqNCgP8UsHB_H-doJa_c73ADQM1cdxzfZ8ShMmIAi3TjpWjbwpU7fD1CNP8jPvqwEwMooHsXIGzhim5NP6iPydcpPFF03qitP0iPfpmRE2oCW4wYgBudTEQda95IYFPRBKVzbVLpQXhLZzzDPlqx894-oZZmhCgLc9CNoCyMaIVZlHvZ_fmW1v33PGRqPJxhxJP3At6jquz1qa_0_2CqNQ9qvwgRP5N79WQz5vidtT7so8o53vUVPt8I6qO0nvM7r8JHo66L4i9-q_ThXG3-2na1yz2Hyn8L54_o4Dn-ETt55-Cx__sgsWvYPgp8TF5jYdO9NouUQMSWJ8gUvq42P_SOnHRse8eksZCOPOkESCKl-O7c7RtKFAI8kP2ltJ9E6e5',
# # #     'ttwid': '1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1752014034%7Cba59cb191a734d94f19af0f0136fe84f44d8797f1d8dcacf49a9ae2f8747e9db',
# # #     '_ga': 'GA1.1.150342934.1752048579',
# # #     '_fbp': 'fb.1.1752048580728.1446697223',
# # #     '_ga_NBFTJ2P3P3': 'GS1.1.1752048579.1.1.1752048630.0.0.1773973896',
# # #     'pre_country': 'KR',
# # #     'lang_type': 'en',
# # #     'tta_attr_id_mirror': '0.1755075598.7537992296453636097',
# # #     '_tt_enable_cookie': '1',
# # #     'ttcsid': '1755660196386::vRKZe4gsZbYCGZvSjeBW.1.1755660196386',
# # #     'ttcsid_C97F14JC77U63IDI7U40': '1755660196385::1jScwBvAKvOay5Y3IDYq.1.1755660196625',
# # #     '_ga_Y2RSHPPW88': 'GS2.1.s1755660196$o1$g1$t1755660202$j0$l0$h858435056',
# # #     '_ga_HV1FL86553': 'GS2.1.s1755660196$o1$g0$t1755660202$j0$l0$h430147227',
# # #     '_ttp': '31XBbVW8z3njdHMvhKmUgOZdYYp',
# # #     '_ga_TEQXTT9FE4': 'GS1.1.1756345152.1.1.1756345319.0.0.46985635',
# # #     'sid_guard': 'c6960424c3048f7c6e0978192e012638%7C1760468508%7C15552000%7CSun%2C+12-Apr-2026+19%3A01%3A48+GMT',
# # #     'tt_session_tlb_tag': 'sttt%7C4%7CxpYEJMMEj3xuCXgZLgEmOP_________fzOi7a8IbznWsP6_DCsp0-A9Tmjey7VZ_aYnyddUwa54%3D',
# # #     'sid_ucp_v1': '1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA',
# # #     'ssid_ucp_v1': '1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA',
# # #     'tiktok_webapp_theme_source': 'auto',
# # #     'tiktok_webapp_theme': 'dark',
# # #     'delay_guest_mode_vid': '5',
# # #     'tt_csrf_token': 'fC6X3ood-46AgqhdK-RE-KnY_vkvXjZPPdMY',
# # #     'perf_feed_cache': '{%22expireTimestamp%22:1762171200000%2C%22itemIds%22:[%227560011590322441502%22%2C%227565435256900209976%22%2C%227558870463225646348%22]}',
# # #     'store-country-sign': 'MEIEDNekO66OkaT4HZ9UaAQguHo4UC-k0yWjwtFWL_shAKDskxokVgRJPzOdsPjOnuMEEKvB2Pd0ULwLu80EKcusW1w',
# # #     'odin_tt': '4116507704e2237afd54221dada9494cab976af8df18049b36e7b0e4062e9b1151841138c0a2dfc8523da3167cefff11ff9452d6f74fb92f1b5f2789dd2b6066',
# # #     'msToken': 'se8Jrj22b-E5kSUNlPSNSgCo8c5uYEjGj3qOcIY7Ql4v_WPTYr2iy3vVt_YRt7E1jhJStsH1ReJYnNPiQnzKavqkBhdGR0XlOzmUv1NdgDB9bNZO6YX1ai7pesl_2UKVmIA-kFfMpsEHkeBb03QIoZwSXTk=',
# # #     'passport_fe_beating_status': 'false',
# # #     'msToken': 'AEGDQGTYjznUwuKAjjCPv-hNIGHWhdoQjnB5yJzpT7ZoAXaH9WYz0qLeBrDOoangFTku2O_2BsGnIDNP4k-Jd7eSov_P19ZIB0V-tPN5ZigSpyXRQzJxmWSW5lXF',
# # #     'ttwid': '1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1762001699%7C298db69a27f7c8414a09ba1fcc4eec483fe8a0bdd0b07858d6e05899fce3ac61',
# # # }

# # # headers = {
# # #     'accept': '*/*',
# # #     'accept-language': 'en-US,en;q=0.9',
# # #     'priority': 'u=1, i',
# # #     'referer': 'https://www.tiktok.com/',
# # #     'sec-ch-ua': '"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
# # #     'sec-ch-ua-mobile': '?0',
# # #     'sec-ch-ua-platform': '"Windows"',
# # #     'sec-fetch-dest': 'empty',
# # #     'sec-fetch-mode': 'cors',
# # #     'sec-fetch-site': 'same-origin',
# # #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0',
# # #     'cookie': 'cookie-consent={%22optional%22:true%2C%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22hubspot%22:true%2C%22version%22:%22v10%22}; living_user_id=149999902702; tt_chain_token=g/awArl40iOADD0hHi9e/Q==; d_ticket=578cfb16f8d0da5d1f57811147ae32c1d1e4c; uid_tt=91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8; uid_tt_ss=91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8; sid_tt=c6960424c3048f7c6e0978192e012638; sessionid=c6960424c3048f7c6e0978192e012638; sessionid_ss=c6960424c3048f7c6e0978192e012638; store-idc=alisg; store-country-code=kr; store-country-code-src=uid; tt-target-idc=alisg; tt-target-idc-sign=jHcAJBth816HHWGYqpllY256Vw_XVnCFfgixI3_n23HZ8S9rc7uuJBy3lnZ69b6Lr-1s8Y2GP1RyOFAqPJOkmhJiSPC3w_-kvcpRCMG2_Lukc7i4fz-oh6V_QQvmQDqNCgP8UsHB_H-doJa_c73ADQM1cdxzfZ8ShMmIAi3TjpWjbwpU7fD1CNP8jPvqwEwMooHsXIGzhim5NP6iPydcpPFF03qitP0iPfpmRE2oCW4wYgBudTEQda95IYFPRBKVzbVLpQXhLZzzDPlqx894-oZZmhCgLc9CNoCyMaIVZlHvZ_fmW1v33PGRqPJxhxJP3At6jquz1qa_0_2CqNQ9qvwgRP5N79WQz5vidtT7so8o53vUVPt8I6qO0nvM7r8JHo66L4i9-q_ThXG3-2na1yz2Hyn8L54_o4Dn-ETt55-Cx__sgsWvYPgp8TF5jYdO9NouUQMSWJ8gUvq42P_SOnHRse8eksZCOPOkESCKl-O7c7RtKFAI8kP2ltJ9E6e5; ttwid=1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1752014034%7Cba59cb191a734d94f19af0f0136fe84f44d8797f1d8dcacf49a9ae2f8747e9db; _ga=GA1.1.150342934.1752048579; _fbp=fb.1.1752048580728.1446697223; _ga_NBFTJ2P3P3=GS1.1.1752048579.1.1.1752048630.0.0.1773973896; pre_country=KR; lang_type=en; tta_attr_id_mirror=0.1755075598.7537992296453636097; _tt_enable_cookie=1; ttcsid=1755660196386::vRKZe4gsZbYCGZvSjeBW.1.1755660196386; ttcsid_C97F14JC77U63IDI7U40=1755660196385::1jScwBvAKvOay5Y3IDYq.1.1755660196625; _ga_Y2RSHPPW88=GS2.1.s1755660196$o1$g1$t1755660202$j0$l0$h858435056; _ga_HV1FL86553=GS2.1.s1755660196$o1$g0$t1755660202$j0$l0$h430147227; _ttp=31XBbVW8z3njdHMvhKmUgOZdYYp; _ga_TEQXTT9FE4=GS1.1.1756345152.1.1.1756345319.0.0.46985635; sid_guard=c6960424c3048f7c6e0978192e012638%7C1760468508%7C15552000%7CSun%2C+12-Apr-2026+19%3A01%3A48+GMT; tt_session_tlb_tag=sttt%7C4%7CxpYEJMMEj3xuCXgZLgEmOP_________fzOi7a8IbznWsP6_DCsp0-A9Tmjey7VZ_aYnyddUwa54%3D; sid_ucp_v1=1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA; ssid_ucp_v1=1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA; tiktok_webapp_theme_source=auto; tiktok_webapp_theme=dark; delay_guest_mode_vid=5; tt_csrf_token=fC6X3ood-46AgqhdK-RE-KnY_vkvXjZPPdMY; perf_feed_cache={%22expireTimestamp%22:1762171200000%2C%22itemIds%22:[%227560011590322441502%22%2C%227565435256900209976%22%2C%227558870463225646348%22]}; store-country-sign=MEIEDNekO66OkaT4HZ9UaAQguHo4UC-k0yWjwtFWL_shAKDskxokVgRJPzOdsPjOnuMEEKvB2Pd0ULwLu80EKcusW1w; odin_tt=4116507704e2237afd54221dada9494cab976af8df18049b36e7b0e4062e9b1151841138c0a2dfc8523da3167cefff11ff9452d6f74fb92f1b5f2789dd2b6066; msToken=se8Jrj22b-E5kSUNlPSNSgCo8c5uYEjGj3qOcIY7Ql4v_WPTYr2iy3vVt_YRt7E1jhJStsH1ReJYnNPiQnzKavqkBhdGR0XlOzmUv1NdgDB9bNZO6YX1ai7pesl_2UKVmIA-kFfMpsEHkeBb03QIoZwSXTk=; passport_fe_beating_status=false; msToken=AEGDQGTYjznUwuKAjjCPv-hNIGHWhdoQjnB5yJzpT7ZoAXaH9WYz0qLeBrDOoangFTku2O_2BsGnIDNP4k-Jd7eSov_P19ZIB0V-tPN5ZigSpyXRQzJxmWSW5lXF; ttwid=1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1762001699%7C298db69a27f7c8414a09ba1fcc4eec483fe8a0bdd0b07858d6e05899fce3ac61',
# # # }

# # # response = requests.get(
# # #     'https://www.tiktok.com/api/recommend/item_list/?WebIdLastTime=1736951461&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F141.0.0.0%20Safari%2F537.36%20Edg%2F141.0.0.0&channel=tiktok_web&clientABVersions=74800760%2C70508271%2C72437276%2C73720540%2C74250915%2C74367308%2C74393673%2C74446915%2C74465399%2C74465409%2C74536864%2C74609147%2C74627577%2C74632791%2C74674280%2C74676351%2C74679798%2C74686502%2C74700792%2C74703727%2C74711111%2C74733472%2C74746519%2C74746610%2C74757744%2C74767144%2C74767851%2C74782564%2C74792133%2C74793837%2C74798337%2C74798356%2C74808329%2C74810092%2C74811360%2C74819402%2C74824020%2C74872266%2C74882809%2C70138197%2C70156809%2C70405643%2C71057832%2C71200802%2C71381811%2C71516509%2C71803300%2C71962127%2C72360691%2C72408100%2C72854054%2C72892778%2C73004916%2C73171280%2C73208420%2C73989921%2C74276218%2C74844724&cookie_enabled=true&count=6&coverFormat=2&cpu_core_number=12&dark_mode=false&data_collection_enabled=true&day_of_week=6&device_id=7460149314773288494&device_platform=web_pc&device_score=8.57&device_type=web_h264&enable_cache=false&focus_state=true&from_page=fyp&history_len=2&isNonPersonalized=false&is_fullscreen=false&is_page_visible=true&itemID=&language=en&launch_mode=direct&network=10&odinId=7478784916198065170&os=windows&priority_region=KR&pullType=1&referer=&region=KR&screen_height=1080&screen_width=1920&showAboutThisAd=true&showAds=true&time_of_day=21&tz_name=Asia%2FSeoul&video_encoding=&vv_count=12529&vv_count_fyp=2637&watchLiveLastTime=1741102304984&webcast_language=en&window_height=963&window_width=165&msToken=se8Jrj22b-E5kSUNlPSNSgCo8c5uYEjGj3qOcIY7Ql4v_WPTYr2iy3vVt_YRt7E1jhJStsH1ReJYnNPiQnzKavqkBhdGR0XlOzmUv1NdgDB9bNZO6YX1ai7pesl_2UKVmIA-kFfMpsEHkeBb03QIoZwSXTk=&X-Bogus=DFSzsIVOFbvANaQoCPBZ3Q-YnjPe&X-Gnarly=MRplt5vBUafcU6/ysUJmzy6qik43h4f34sH-NSqWbuIZ0XJ9abx/m8UJ4KWJus2fTvTAU4sEa1uoOym4tPgYepqyoXC-rHpjHETivv2oSwlXxNFxU0yjh-shRUvT8/gHSQMfemOJrs/k3pxmTCp3nN3PYyd6QPk9IUyF2RrBryy9WB1msl4iixJRRhUG1xqQJttjGe7Zb4eBmvE7jXjFpC957ujEU-v9G/0h0Kkg-Y-M2wUS5BxQmsVDH6Tksn4w7VxfdF7nEL-lOwxZK-jcXma9JTEzfTuDm1U49u65XePGhjrQ0OLZlBenK//9Rszp9wZ=',
# # #     cookies=cookies,
# # #     headers=headers,
# # # )


# # # print(response.content)

# # # with open("save.json", "wb") as file:
# # #     file.write(response.content)



# # import requests

# # cookies = {
# #     'cookie-consent': '{%22optional%22:true%2C%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22hubspot%22:true%2C%22version%22:%22v10%22}',
# #     'living_user_id': '149999902702',
# #     'tt_chain_token': 'g/awArl40iOADD0hHi9e/Q==',
# #     'd_ticket': '578cfb16f8d0da5d1f57811147ae32c1d1e4c',
# #     'uid_tt': '91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8',
# #     'uid_tt_ss': '91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8',
# #     'sid_tt': 'c6960424c3048f7c6e0978192e012638',
# #     'sessionid': 'c6960424c3048f7c6e0978192e012638',
# #     'sessionid_ss': 'c6960424c3048f7c6e0978192e012638',
# #     'store-idc': 'alisg',
# #     'store-country-code': 'kr',
# #     'store-country-code-src': 'uid',
# #     'tt-target-idc': 'alisg',
# #     'tt-target-idc-sign': 'jHcAJBth816HHWGYqpllY256Vw_XVnCFfgixI3_n23HZ8S9rc7uuJBy3lnZ69b6Lr-1s8Y2GP1RyOFAqPJOkmhJiSPC3w_-kvcpRCMG2_Lukc7i4fz-oh6V_QQvmQDqNCgP8UsHB_H-doJa_c73ADQM1cdxzfZ8ShMmIAi3TjpWjbwpU7fD1CNP8jPvqwEwMooHsXIGzhim5NP6iPydcpPFF03qitP0iPfpmRE2oCW4wYgBudTEQda95IYFPRBKVzbVLpQXhLZzzDPlqx894-oZZmhCgLc9CNoCyMaIVZlHvZ_fmW1v33PGRqPJxhxJP3At6jquz1qa_0_2CqNQ9qvwgRP5N79WQz5vidtT7so8o53vUVPt8I6qO0nvM7r8JHo66L4i9-q_ThXG3-2na1yz2Hyn8L54_o4Dn-ETt55-Cx__sgsWvYPgp8TF5jYdO9NouUQMSWJ8gUvq42P_SOnHRse8eksZCOPOkESCKl-O7c7RtKFAI8kP2ltJ9E6e5',
# #     'ttwid': '1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1752014034%7Cba59cb191a734d94f19af0f0136fe84f44d8797f1d8dcacf49a9ae2f8747e9db',
# #     '_ga': 'GA1.1.150342934.1752048579',
# #     '_fbp': 'fb.1.1752048580728.1446697223',
# #     '_ga_NBFTJ2P3P3': 'GS1.1.1752048579.1.1.1752048630.0.0.1773973896',
# #     'pre_country': 'KR',
# #     'lang_type': 'en',
# #     'tta_attr_id_mirror': '0.1755075598.7537992296453636097',
# #     '_tt_enable_cookie': '1',
# #     'ttcsid': '1755660196386::vRKZe4gsZbYCGZvSjeBW.1.1755660196386',
# #     'ttcsid_C97F14JC77U63IDI7U40': '1755660196385::1jScwBvAKvOay5Y3IDYq.1.1755660196625',
# #     '_ga_Y2RSHPPW88': 'GS2.1.s1755660196$o1$g1$t1755660202$j0$l0$h858435056',
# #     '_ga_HV1FL86553': 'GS2.1.s1755660196$o1$g0$t1755660202$j0$l0$h430147227',
# #     '_ttp': '31XBbVW8z3njdHMvhKmUgOZdYYp',
# #     '_ga_TEQXTT9FE4': 'GS1.1.1756345152.1.1.1756345319.0.0.46985635',
# #     'sid_guard': 'c6960424c3048f7c6e0978192e012638%7C1760468508%7C15552000%7CSun%2C+12-Apr-2026+19%3A01%3A48+GMT',
# #     'tt_session_tlb_tag': 'sttt%7C4%7CxpYEJMMEj3xuCXgZLgEmOP_________fzOi7a8IbznWsP6_DCsp0-A9Tmjey7VZ_aYnyddUwa54%3D',
# #     'sid_ucp_v1': '1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA',
# #     'ssid_ucp_v1': '1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA',
# #     'tiktok_webapp_theme_source': 'auto',
# #     'tiktok_webapp_theme': 'dark',
# #     'delay_guest_mode_vid': '5',
# #     'tt_csrf_token': 'xYWajjO9-89aI0fRrZo-yJnaslhIXLFs-kW8',
# #     'store-country-sign': 'MEIEDBKdqGvnG5UAo5FXbwQgAm15FzxCZRJzVE_IqmgWlnlT7svrenSYBbR9w-g-oRsEEF7CnPC1TU3oVf8kCi26MV4',
# #     'msToken': 'Xb5ISAL1qu4crHwjKKLRrctkVp1TEq5L-n_n90700NHS_cRZewdWtNn08cFvXpfj86NB79ISVgXL0ZJ4Ar5wbwp5QQsyafQl8i8Jocj24HK2v_F8llI3Jr3WmR1of_6wKdXt6rywsxWWStV_r-baiy_dnw==',
# #     'odin_tt': '55702be48b513482b777bcd6455e0453a917564e2ca5250690bf55a79a7e9972359024426402e79fb654913da3e1b60ab52fd8d6fbe071f3a91cafe0d0a83e3c',
# #     'passport_fe_beating_status': 'false',
# #     'msToken': '8ub9MWDYuXZFOp0RDsLUPEXhzk4vpC55-h_rTrpJWH3fqkbiDMXiFwWmlbEl6WDUxEwmB3lCdcdMU-x7jd2AZsVBLzmUHb8bD76wuSnxizDTDg1BCgELK3neEir7sjQHoOV2nD6T8jkpgqiU4z6_HGmOgA==',
# #     'perf_feed_cache': '{%22expireTimestamp%22:1762351200000%2C%22itemIds%22:[%227565222614025686285%22%2C%227553551072632147211%22%2C%227567781083329170701%22]}',
# #     'ttwid': '1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1762180132%7C03a7156af52f7028f1bd89d5799983d4e24445a7d55aec361f1c84fce271bbc0',
# # }

# # headers = {
# #     'accept': '*/*',
# #     'accept-language': 'en-US,en;q=0.9',
# #     'priority': 'u=1, i',
# #     'referer': 'https://www.tiktok.com/',
# #     'sec-ch-ua': '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
# #     'sec-ch-ua-mobile': '?0',
# #     'sec-ch-ua-platform': '"Windows"',
# #     'sec-fetch-dest': 'empty',
# #     'sec-fetch-mode': 'cors',
# #     'sec-fetch-site': 'same-origin',
# #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',
# #     # 'cookie': 'cookie-consent={%22optional%22:true%2C%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22hubspot%22:true%2C%22version%22:%22v10%22}; living_user_id=149999902702; tt_chain_token=g/awArl40iOADD0hHi9e/Q==; d_ticket=578cfb16f8d0da5d1f57811147ae32c1d1e4c; uid_tt=91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8; uid_tt_ss=91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8; sid_tt=c6960424c3048f7c6e0978192e012638; sessionid=c6960424c3048f7c6e0978192e012638; sessionid_ss=c6960424c3048f7c6e0978192e012638; store-idc=alisg; store-country-code=kr; store-country-code-src=uid; tt-target-idc=alisg; tt-target-idc-sign=jHcAJBth816HHWGYqpllY256Vw_XVnCFfgixI3_n23HZ8S9rc7uuJBy3lnZ69b6Lr-1s8Y2GP1RyOFAqPJOkmhJiSPC3w_-kvcpRCMG2_Lukc7i4fz-oh6V_QQvmQDqNCgP8UsHB_H-doJa_c73ADQM1cdxzfZ8ShMmIAi3TjpWjbwpU7fD1CNP8jPvqwEwMooHsXIGzhim5NP6iPydcpPFF03qitP0iPfpmRE2oCW4wYgBudTEQda95IYFPRBKVzbVLpQXhLZzzDPlqx894-oZZmhCgLc9CNoCyMaIVZlHvZ_fmW1v33PGRqPJxhxJP3At6jquz1qa_0_2CqNQ9qvwgRP5N79WQz5vidtT7so8o53vUVPt8I6qO0nvM7r8JHo66L4i9-q_ThXG3-2na1yz2Hyn8L54_o4Dn-ETt55-Cx__sgsWvYPgp8TF5jYdO9NouUQMSWJ8gUvq42P_SOnHRse8eksZCOPOkESCKl-O7c7RtKFAI8kP2ltJ9E6e5; ttwid=1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1752014034%7Cba59cb191a734d94f19af0f0136fe84f44d8797f1d8dcacf49a9ae2f8747e9db; _ga=GA1.1.150342934.1752048579; _fbp=fb.1.1752048580728.1446697223; _ga_NBFTJ2P3P3=GS1.1.1752048579.1.1.1752048630.0.0.1773973896; pre_country=KR; lang_type=en; tta_attr_id_mirror=0.1755075598.7537992296453636097; _tt_enable_cookie=1; ttcsid=1755660196386::vRKZe4gsZbYCGZvSjeBW.1.1755660196386; ttcsid_C97F14JC77U63IDI7U40=1755660196385::1jScwBvAKvOay5Y3IDYq.1.1755660196625; _ga_Y2RSHPPW88=GS2.1.s1755660196$o1$g1$t1755660202$j0$l0$h858435056; _ga_HV1FL86553=GS2.1.s1755660196$o1$g0$t1755660202$j0$l0$h430147227; _ttp=31XBbVW8z3njdHMvhKmUgOZdYYp; _ga_TEQXTT9FE4=GS1.1.1756345152.1.1.1756345319.0.0.46985635; sid_guard=c6960424c3048f7c6e0978192e012638%7C1760468508%7C15552000%7CSun%2C+12-Apr-2026+19%3A01%3A48+GMT; tt_session_tlb_tag=sttt%7C4%7CxpYEJMMEj3xuCXgZLgEmOP_________fzOi7a8IbznWsP6_DCsp0-A9Tmjey7VZ_aYnyddUwa54%3D; sid_ucp_v1=1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA; ssid_ucp_v1=1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA; tiktok_webapp_theme_source=auto; tiktok_webapp_theme=dark; delay_guest_mode_vid=5; tt_csrf_token=xYWajjO9-89aI0fRrZo-yJnaslhIXLFs-kW8; store-country-sign=MEIEDBKdqGvnG5UAo5FXbwQgAm15FzxCZRJzVE_IqmgWlnlT7svrenSYBbR9w-g-oRsEEF7CnPC1TU3oVf8kCi26MV4; msToken=Xb5ISAL1qu4crHwjKKLRrctkVp1TEq5L-n_n90700NHS_cRZewdWtNn08cFvXpfj86NB79ISVgXL0ZJ4Ar5wbwp5QQsyafQl8i8Jocj24HK2v_F8llI3Jr3WmR1of_6wKdXt6rywsxWWStV_r-baiy_dnw==; odin_tt=55702be48b513482b777bcd6455e0453a917564e2ca5250690bf55a79a7e9972359024426402e79fb654913da3e1b60ab52fd8d6fbe071f3a91cafe0d0a83e3c; passport_fe_beating_status=false; msToken=8ub9MWDYuXZFOp0RDsLUPEXhzk4vpC55-h_rTrpJWH3fqkbiDMXiFwWmlbEl6WDUxEwmB3lCdcdMU-x7jd2AZsVBLzmUHb8bD76wuSnxizDTDg1BCgELK3neEir7sjQHoOV2nD6T8jkpgqiU4z6_HGmOgA==; perf_feed_cache={%22expireTimestamp%22:1762351200000%2C%22itemIds%22:[%227565222614025686285%22%2C%227553551072632147211%22%2C%227567781083329170701%22]}; ttwid=1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1762180132%7C03a7156af52f7028f1bd89d5799983d4e24445a7d55aec361f1c84fce271bbc0',
# # }

# # response = requests.get(
# #     'https://www.tiktok.com/api/recommend/item_list/?WebIdLastTime=1736951461&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F142.0.0.0%20Safari%2F537.36%20Edg%2F142.0.0.0&channel=tiktok_web&clientABVersions=74800760%2C70508271%2C72437276%2C73720540%2C74250915%2C74393673%2C74446915%2C74465399%2C74465409%2C74536864%2C74609147%2C74627577%2C74632791%2C74674280%2C74676351%2C74679798%2C74686502%2C74700792%2C74703727%2C74711111%2C74733472%2C74746519%2C74746610%2C74757744%2C74767144%2C74767851%2C74782564%2C74792133%2C74793837%2C74798337%2C74798356%2C74808329%2C74810092%2C74811360%2C74819402%2C74824020%2C74872266%2C74882809%2C70138197%2C70156809%2C70405643%2C71057832%2C71200802%2C71381811%2C71516509%2C71803300%2C71962127%2C72360691%2C72408100%2C72854054%2C72892778%2C73004916%2C73171280%2C73208420%2C73989921%2C74276218%2C74844724&cookie_enabled=true&count=6&coverFormat=2&cpu_core_number=12&dark_mode=false&data_collection_enabled=true&day_of_week=1&device_id=7460149314773288494&device_platform=web_pc&device_score=8.57&device_type=web_h264&enable_cache=false&focus_state=true&from_page=fyp&history_len=2&isNonPersonalized=false&is_fullscreen=false&is_page_visible=true&itemID=&language=en&launch_mode=direct&network=10&odinId=7478784916198065170&os=windows&priority_region=KR&pullType=1&referer=&region=KR&screen_height=1080&screen_width=1920&showAboutThisAd=true&showAds=true&time_of_day=23&tz_name=Asia%2FSeoul&video_encoding=&vv_count=12529&vv_count_fyp=2637&watchLiveLastTime=1741102304984&webcast_language=en&window_height=962&window_width=150&msToken=Xb5ISAL1qu4crHwjKKLRrctkVp1TEq5L-n_n90700NHS_cRZewdWtNn08cFvXpfj86NB79ISVgXL0ZJ4Ar5wbwp5QQsyafQl8i8Jocj24HK2v_F8llI3Jr3WmR1of_6wKdXt6rywsxWWStV_r-baiy_dnw==&X-Bogus=DFSzsIVYt2tANH/ACPJVwimpF2W/&X-Gnarly=Mw1bQHB/564boDbZQP6s-ShaK79iOfgOU57EoHgX55VO37v9-rSjMDEUveU9Nfm5dxJhESWUyRv4djcH4XUtOYukfRsLuySJRYRPMg37l9HL0XBOV0uTQJuCiwefkvLfYgShxDL-m543VJlr2-f2HHDjhsnNo6F10fQWHlSqptwrCQCKoyBctGFyOMd/cKJpCHGAvva4IxMPEQVXKqALpvG90JdQ4ERuMgAs11wKA97EXkbVCZigzSSJPsJFTwxkiF9SYENojM6LDiv2DEBH-1jU4pOll-gPUyLf0bY1IfEricLsZqdGwDDIhWCWS8EYYPz=',
# #     cookies=cookies,
# #     headers=headers,
# # )


# # print(response.content)


# # 'https://www.tiktok.com/api/recommend/item_list/?WebIdLastTime=1736951461&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F142.0.0.0%20Safari%2F537.36%20Edg%2F142.0.0.0&channel=tiktok_web&clientABVersions=74800760%2C70508271%2C72437276%2C73720540%2C74250915%2C74393673%2C74446915%2C74465399%2C74465409%2C74536864%2C74609147%2C74627577%2C74632791%2C74674280%2C74676351%2C74679798%2C74686502%2C74700792%2C74703727%2C74711111%2C74733472%2C74746519%2C74746610%2C74757744%2C74767144%2C74767851%2C74782564%2C74792133%2C74793837%2C74798337%2C74798356%2C74808329%2C74810092%2C74811360%2C74819402%2C74824020%2C74872266%2C74882809%2C70138197%2C70156809%2C70405643%2C71057832%2C71200802%2C71381811%2C71516509%2C71803300%2C71962127%2C72360691%2C72408100%2C72854054%2C72892778%2C73004916%2C73171280%2C73208420%2C73989921%2C74276218%2C74844724&cookie_enabled=true&count=6&coverFormat=2&cpu_core_number=12&dark_mode=false&data_collection_enabled=true&day_of_week=1&device_id=7460149314773288494&device_platform=web_pc&device_score=8.57&device_type=web_h264&enable_cache=false&focus_state=true&from_page=fyp&history_len=2&isNonPersonalized=false&is_fullscreen=false&is_page_visible=true&itemID=&language=en&launch_mode=direct&network=10&odinId=7478784916198065170&os=windows&priority_region=KR&pullType=1&referer=&region=KR&screen_height=1080&screen_width=1920&showAboutThisAd=true&showAds=true&time_of_day=23&tz_name=Asia%2FSeoul&video_encoding=&vv_count=12529&vv_count_fyp=2637&watchLiveLastTime=1741102304984&webcast_language=en&window_height=962&window_width=150&msToken=Xb5ISAL1qu4crHwjKKLRrctkVp1TEq5L-n_n90700NHS_cRZewdWtNn08cFvXpfj86NB79ISVgXL0ZJ4Ar5wbwp5QQsyafQl8i8Jocj24HK2v_F8llI3Jr3WmR1of_6wKdXt6rywsxWWStV_r-baiy_dnw%3D%3D&X-Bogus=DFSzsIVYt2tANH/ACPJVwimpF2W/&X-Gnarly=Mw1bQHB/564boDbZQP6s-ShaK79iOfgOU57EoHgX55VO37v9-rSjMDEUveU9Nfm5dxJhESWUyRv4djcH4XUtOYukfRsLuySJRYRPMg37l9HL0XBOV0uTQJuCiwefkvLfYgShxDL-m543VJlr2-f2HHDjhsnNo6F10fQWHlSqptwrCQCKoyBctGFyOMd/cKJpCHGAvva4IxMPEQVXKqALpvG90JdQ4ERuMgAs11wKA97EXkbVCZigzSSJPsJFTwxkiF9SYENojM6LDiv2DEBH-1jU4pOll-gPUyLf0bY1IfEricLsZqdGwDDIhWCWS8EYYPz='




# import subprocess, json

# def get_ms_token():
#     js_code = """
#     const crypto = require('crypto');
#     // TikTok’s function is obfuscated but this produces a valid msToken-like signature
#     function makeToken() {
#       const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
#       let token = '';
#       for (let i = 0; i < 107; i++) token += chars[Math.floor(Math.random() * chars.length)];
#       return token + crypto.randomBytes(8).toString('hex');
#     }
#     console.log(JSON.stringify({msToken: makeToken()}));
#     """
#     out = subprocess.check_output(["node", "-e", js_code], text=True)
#     return json.loads(out)

# token = get_ms_token()
# print(token)


# from curl_cffi import requests   # this is not the same as pip requests

# url = "https://www.tiktok.com/api/recommend/item_list/?WebIdLastTime=1762523256&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F131.0.0.0%20Safari%2F537.36&channel=tiktok_web&clientABVersions=70508271%2C73547759%2C73720541%2C74536863%2C74609147%2C74627577%2C74632791%2C74674277%2C74700790%2C74703729%2C74711792%2C74746519%2C74767853%2C74772042%2C74780477%2C74792133%2C74793838%2C74798356%2C74803472%2C74810092%2C74811360%2C74819401%2C74824020%2C74860162%2C74872266%2C74879786%2C74891662%2C74927853%2C74931323%2C70405643%2C71057832%2C71200802%2C72361743%2C73171280%2C73208420%2C74276218%2C74844724&cookie_enabled=true&count=6&coverFormat=2&cpu_core_number=12&dark_mode=false&data_collection_enabled=false&day_of_week=5&device_id=7569979703613933069&device_platform=web_pc&enable_cache=false&focus_state=true&history_len=2&isNonPersonalized=false&is_fullscreen=false&is_new_user=true&is_page_visible=true&itemID=foryou&language=en&odinId=7569979722713646094&os=windows&priority_region=&pullType=1&referer=&region=US&screen_height=1080&screen_width=1920&showAboutThisAd=true&showAds=false&time_of_day=8&tz_name=America%2FNew_York&video_encoding=&vv_count=0&vv_count_fyp=0&watchLiveLastTime=&webcast_language=en&msToken=&X-Bogus=DFSzsIROgYtANrJaCPLSgL13rHlW&X-Gnarly=MxV7ycG9VvYw%2FHbNHexOaIlyOMmBjPaBH6chpV-i5-5yivXh2coA8h0kLOvG9hEzRmCkIqCxMTKMa41KgXmjiPharGW-pmEy6nQ%2FpuElpU79YtO1UZ4-f9zgQG0RuU1-5QQUPxkhMV9LvzN4Bvj4hct5MSZsOIVowMMba9hHqVAB0bG8zIgXUDSAg7X3sZUi4cvCdg604KpNOv2IgLVzH14Ym4JRYrrpCXnu8dsORUtpx8YGYP%2Fi0yMbH2bcDTe6BfEbFbSqx1911NrDf6S4s0TQ0LDMtE2H%2FCW9V%2FBBQRkuhQMsAO2RLsium3XHX7MamYz="

# headers = {
#     "sec-ch-ua-platform": '"Windows"',
#     "referer": "https://www.tiktok.com/foryou",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                   "AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/131.0.0.0 Safari/537.36",
#     "sec-ch-ua": '"Not=A?Brand";v="24", "Chromium";v="140"',
#     "accept-language": "en-US",
#     "sec-ch-ua-mobile": "?0",
#     "accept": "*/*",
#     "accept-encoding": "gzip, deflate, br"
# }

# # 'impersonate' makes curl_cffi use Chrome-like TLS + HTTP/2 fingerprint
# resp = requests.get(url, headers=headers, impersonate="chrome131")
# print("Status:", resp.status_code)
# print("Length:", len(resp.content))
# print("Preview:", resp.text[:600])



# import requests

# url = "https://www.tiktok.com/api/recommend/item_list/?WebIdLastTime=1762523256&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F131.0.0.0%20Safari%2F537.36&channel=tiktok_web&clientABVersions=70508271%2C73547759%2C73720541%2C74536863%2C74609147%2C74627577%2C74632791%2C74674277%2C74700790%2C74703729%2C74711792%2C74746519%2C74767853%2C74772042%2C74780477%2C74792133%2C74793838%2C74798356%2C74803472%2C74810092%2C74811360%2C74819401%2C74824020%2C74860162%2C74872266%2C74879786%2C74891662%2C74927853%2C74931323%2C70405643%2C71057832%2C71200802%2C72361743%2C73171280%2C73208420%2C74276218%2C74844724&cookie_enabled=true&count=6&coverFormat=2&cpu_core_number=12&dark_mode=false&data_collection_enabled=false&day_of_week=5&device_id=7569979703613933069&device_platform=web_pc&enable_cache=false&focus_state=true&history_len=2&isNonPersonalized=false&is_fullscreen=false&is_new_user=true&is_page_visible=true&itemID=foryou&language=en&odinId=7569979722713646094&os=windows&priority_region=&pullType=1&referer=&region=US&screen_height=1080&screen_width=1920&showAboutThisAd=true&showAds=false&time_of_day=8&tz_name=America%2FNew_York&video_encoding=&vv_count=0&vv_count_fyp=0&watchLiveLastTime=&webcast_language=en&msToken=&X-Bogus=DFSzsIROgYtANrJaCPLSgL13rHlW&X-Gnarly=MxV7ycG9VvYw%2FHbNHexOaIlyOMmBjPaBH6chpV-i5-5yivXh2coA8h0kLOvG9hEzRmCkIqCxMTKMa41KgXmjiPharGW-pmEy6nQ%2FpuElpU79YtO1UZ4-f9zgQG0RuU1-5QQUPxkhMV9LvzN4Bvj4hct5MSZsOIVowMMba9hHqVAB0bG8zIgXUDSAg7X3sZUi4cvCdg604KpNOv2IgLVzH14Ym4JRYrrpCXnu8dsORUtpx8YGYP%2Fi0yMbH2bcDTe6BfEbFbSqx1911NrDf6S4s0TQ0LDMtE2H%2FCW9V%2FBBQRkuhQMsAO2RLsium3XHX7MamYz="

# headers = {
#     "sec-ch-ua-platform": '"Windows"',
#     "referer": "https://www.tiktok.com/foryou",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                   "AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/131.0.0.0 Safari/537.36",
#     "sec-ch-ua": '"Not=A?Brand";v="24", "Chromium";v="140"',
#     "accept-language": "en-US",
#     "sec-ch-ua-mobile": "?0",
#     "accept": "*/*",
#     "accept-encoding": "gzip, deflate, br",
#     "origin": "https://www.tiktok.com",
#     "sec-fetch-site": "same-origin",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-dest": "empty"
# }

# r = requests.get(
#     url,
#     headers=headers,
#     allow_redirects=False,
#     timeout=30,
# )

# print("Status:", r.status_code)
# print("Length:", len(r.content))
# print("Preview:", r.text[:600])




# from curl_cffi import requests  # NOT the same as pip 'requests'

# url = "https://www.tiktok.com/api/recommend/item_list/?WebIdLastTime=1762570373&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F131.0.0.0%20Safari%2F537.36&channel=tiktok_web&clientABVersions=70508271%2C73547759%2C73720541%2C74536864%2C74609148%2C74627578%2C74632791%2C74674279%2C74700792%2C74703730%2C74711793%2C74746521%2C74746610%2C74767851%2C74772043%2C74780476%2C74792133%2C74793838%2C74798355%2C74803471%2C74810092%2C74811360%2C74819402%2C74824020%2C74837697%2C74851988%2C74872267%2C74879783%2C74891663%2C70405643%2C71057832%2C71200802%2C72361743%2C73171280%2C73208420%2C74276218%2C74844724&cookie_enabled=true&count=6&coverFormat=2&cpu_core_number=12&dark_mode=false&data_collection_enabled=false&day_of_week=5&device_id=7570182069923661326&device_platform=web_pc&device_score=7.95&device_type=web_h264&enable_cache=false&focus_state=true&from_page=fyp&history_len=2&isNonPersonalized=false&is_fullscreen=false&is_new_user=true&is_page_visible=true&itemID=&language=en&launch_mode=direct&network=10&odinId=7570182087548126263&os=windows&priority_region=&pullType=1&referer=&region=US&screen_height=1080&screen_width=1920&showAboutThisAd=true&showAds=false&time_of_day=21&tz_name=America%2FNew_York&video_encoding=&vv_count=0&vv_count_fyp=0&watchLiveLastTime=&webcast_language=en&window_height=1080&window_width=1920&msToken=qF1xn2sNFb9UgsRJ4MhBULHbsODsGv7Eldrrh18-gKzgSPqO6Gv8UalybNTvZtWSqj6NExQDwrDUQplmbc_Uz9st34egEXE7yPkYlFIOXHX4N11jj1Rw-Z6fE-vmbg==&X-Bogus=DFSzsIROUy2ANrJaCPTyG/9LFB5E&X-Gnarly=McPxGWzQtnacAmoPzzHpJ63q-AR1tMxdEsoTW9pGI4ChHYW9-9SKgwg3r1j/rHM07LuwH9kyCES8su350hIeN3CXUcOzRiRqZnEuuMxtxG9JNqzp4vetIOszm27BVv37G8H1sd70sRnzQkUeJwE/n8sIp9G0pkU5zwHH2olbkUPzHUkFEUkCscXyuYHbZzm-D8wvTZhttHR/VJ5kwEpvi0dAEFB8XWU3p4Lv4f/3RZTaCAf5gNGUaprhuc2gjyqMPNCx6/xaTIuVRkFZTcEIwCnNYPlH73MR5VBtCPxpja1JZ73/cJ83/XOpm1fkKuDk/DZ="
# # url = "https://www.tiktok.com/api/recommend/item_list/?WebIdLastTime=1762580191&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F131.0.0.0%20Safari%2F537.36&channel=tiktok_web&clientABVersions=70508271%2C73547759%2C73720541%2C74536863%2C74609149%2C74627577%2C74632788%2C74674277%2C74679799%2C74700792%2C74703727%2C74711792%2C74746521%2C74746610%2C74767853%2C74780476%2C74792133%2C74793838%2C74798355%2C74803470%2C74810092%2C74811360%2C74819401%2C74824021%2C74837697%2C74851988%2C74860161%2C74872266%2C74879783%2C74891664%2C74928115%2C70405643%2C71057832%2C71200802%2C72361743%2C73171280%2C73208420%2C74276218%2C74844724&cookie_enabled=true&count=6&coverFormat=2&cpu_core_number=12&dark_mode=false&data_collection_enabled=false&day_of_week=6&device_id=7570224036282664479&device_platform=web_pc&device_score=7.95&device_type=web_h264&enable_cache=false&focus_state=true&from_page=fyp&history_len=2&isNonPersonalized=false&is_fullscreen=false&is_new_user=true&is_page_visible=true&language=en&launch_mode=direct&network=10&odinId=7570224025344443423&os=windows&pullType=1&region=US&screen_height=1080&screen_width=1920&showAboutThisAd=true&showAds=false&time_of_day=0&tz_name=America%2FNew_York&vv_count=0&vv_count_fyp=0&webcast_language=en&window_height=1080&window_width=1920&msToken=BBbi2tK8upqX657cQS7qjS9Pe3eTKoZDRBvyf98EzelJFiI3tUHWHNlToo-nEefcd7tTVysTGQb6sYa_09lAof7xGjYteBqlPim054a1asiLmx3QdzF0TznZ4EEJ-A==&X-Bogus=DFSzsIROKIiANrJaCPYwj/9LFB55&X-Gnarly=MJS31m5UhJNeylPcqJLV93WQ0T47WTbNuEmD-xDd/FsxX5DJS1kSPSwdne3orkehymlimDoVxQH5ATcKbMP/DU-RlLz8hVY7BqFqk4Q/8Y21VL/7QVfA7e2C1N2/ovjtOuQ8HbC41krp8L9j/tb3Zd1Nawdp5k-srP548msE3aukJiAgbadae93zwZqWMWB1fDU3vUlJ0ynZPNHdHKRoCwN-m7l/ydvcAB/fWb-eDzVeR2w2THO1Z2T1IcwrKLkExzXah6znzGEykYPjzikxBK309V8m-z8H7ksVgcYWDoPLaw2xXtwIA96xocy4efWPBoe="
# headers = {
#     "sec-ch-ua-platform": '"Windows"',
#     "referer": "https://www.tiktok.com/foryou",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                   "AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/131.0.0.0 Safari/537.36",
#     "sec-ch-ua": '"Chromium";v="140", "Not=A?Brand";v="24", "HeadlessChrome";v="140"',
#     "accept-language": "en-US",
#     "sec-ch-ua-mobile": "?0",
#     "accept": "*/*",
#     "accept-encoding": "gzip, deflate, br"
# }

# # Use Chrome 131 fingerprint to mimic the browser TLS & HTTP/2 stack
# resp = requests.get(url, headers=headers, impersonate="chrome131")

# print("Status:", resp.status_code)
# print("Length:", len(resp.content))
# print("Preview:", resp.text[:600])




# from curl_cffi import requests  # NOT the same as pip 'requests'

# url = "https://www.tiktok.com/api/recommend/item_list/?WebIdLastTime=1762580136&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F131.0.0.0%20Safari%2F537.36&channel=tiktok_web&clientABVersions=70508271%2C73547759%2C73720541%2C74536863%2C74609149%2C74627577%2C74632788%2C74674277%2C74679799%2C74700792%2C74703727%2C74711792%2C74746521%2C74746610%2C74767853%2C74780476%2C74792133%2C74793838%2C74798355%2C74803470%2C74810092%2C74811360%2C74819401%2C74824021%2C74837697%2C74851988%2C74860161%2C74872266%2C74879783%2C74891664%2C74928115%2C70405643%2C71057832%2C71200802%2C72361743%2C73171280%2C73208420%2C74276218%2C74844724&cookie_enabled=true&count=6&coverFormat=2&cpu_core_number=12&dark_mode=false&data_collection_enabled=false&day_of_week=6&device_id=7570224036282664479&device_platform=web_pc&device_score=7.95&device_type=web_h264&enable_cache=false&focus_state=true&from_page=fyp&history_len=2&isNonPersonalized=false&is_fullscreen=false&is_new_user=true&is_page_visible=true&itemID=&language=en&launch_mode=direct&network=10&odinId=7570224025344443423&os=windows&priority_region=&pullType=1&referer=&region=US&screen_height=1080&screen_width=1920&showAboutThisAd=true&showAds=false&time_of_day=0&tz_name=America%2FNew_York&video_encoding=&vv_count=0&vv_count_fyp=0&watchLiveLastTime=&webcast_language=en&window_height=1080&window_width=1920&msToken=BBbi2tK8upqX657cQS7qjS9Pe3eTKoZDRBvyf98EzelJFiI3tUHWHNlToo-nEefcd7tTVysTGQb6sYa_09lAof7xGjYteBqlPim054a1asiLmx3QdzF0TznZ4EEJ-A==&X-Bogus=DFSzsIROKIiANrJaCPYwj/9LFB55&X-Gnarly=MJS31m5UhJNeylPcqJLV93WQ0T47WTbNuEmD-xDd/FsxX5DJS1kSPSwdne3orkehymlimDoVxQH5ATcKbMP/DU-RlLz8hVY7BqFqk4Q/8Y21VL/7QVfA7e2C1N2/ovjtOuQ8HbC41krp8L9j/tb3Zd1Nawdp5k-srP548msE3aukJiAgbadae93zwZqWMWB1fDU3vUlJ0ynZPNHdHKRoCwN-m7l/ydvcAB/fWb-eDzVeR2w2THO1Z2T1IcwrKLkExzXah6znzGEykYPjzikxBK309V8m-z8H7ksVgcYWDoPLaw2xXtwIA96xocy4efWPBoe="

# headers = {
#     "sec-ch-ua-platform": '"Windows"',
#     "referer": "https://www.tiktok.com/foryou",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                   "AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/131.0.0.0 Safari/537.36",
#     "sec-ch-ua": '"Chromium";v="140", "Not=A?Brand";v="24", "HeadlessChrome";v="140"',
#     "accept-language": "en-US",
#     "sec-ch-ua-mobile": "?0",
#     "accept": "*/*",
#     "accept-encoding": "gzip, deflate, br"
# }

# # Use Chrome fingerprint for correct TLS and HTTP/2 behavior
# resp = requests.get(url, headers=headers, impersonate="chrome131")

# print("Status:", resp.status_code)
# print("Length:", len(resp.content))
# print("Preview:", resp.text[:600])



# from curl_cffi import requests  # (not pip requests)

# url = "https://www.tiktok.com/api/recommend/item_list/?WebIdLastTime=1762580859&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/131.0.0.0%20Safari/537.36&channel=tiktok_web&clientABVersions=70508271,73547759,73720540,74536863,74609146,74627577,74632788,74674278,74700792,74703728,74711791,74746519,74767852,74772041,74780477,74792133,74793837,74798355,74803470,74810092,74811360,74819401,74824020,74837697,74851987,74863399,74872267,74879783,74891663,74931322,70405643,71057832,71200802,72361743,73171280,73208420,74276218,74844724&cookie_enabled=true&count=6&coverFormat=2&cpu_core_number=12&dark_mode=false&data_collection_enabled=false&day_of_week=6&device_id=7570227130547242526&device_platform=web_pc&device_score=7.95&device_type=web_h264&enable_cache=false&focus_state=true&from_page=fyp&history_len=2&isNonPersonalized=false&is_fullscreen=false&is_new_user=true&is_page_visible=true&itemID=&language=en&launch_mode=direct&network=9.4&odinId=7570227133109912606&os=windows&priority_region=&pullType=1&referer=&region=US&screen_height=1080&screen_width=1920&showAboutThisAd=true&showAds=false&time_of_day=0&tz_name=America%2FNew_York&video_encoding=&vv_count=0&vv_count_fyp=0&watchLiveLastTime=&webcast_language=en&window_height=1080&window_width=1920&msToken=NAwK-3nSLRaC2tiyNSDwCqSKRl5jrt0j4xz4IQkD8lHM2KZFpvG536A8juuCYN3pFUvCeawCKd71KlMTeleZz3tD3cfL0DQ8BLRzmN3Cu0mJvo1I7uE2uE01IeQbAQ==&X-Bogus=DFSzsIROrBvANrJaCPYUaA9LFB5s&X-Gnarly=M5eIyVtXZJxq8j4dfTa91/R5luzFtwp4QoOG0SDYAQmdXPjhT88-Rg-mrCK4CUi4Jt0sFHuq0zmFuNrhsjILkwomSvk/crEk5AQnRLcNDJqKF3uq1LLuhN1Hz-mJY8fY8WwzFElgjNKI0SMTcsqPVkMsK3kkpcH6cCAovIgvmCysOmOv1u2aIwaIUEuO/6yYEeHXjKne-LjxRArrJiu53Y1PHnujYyYnJt3g/OpNmnXF--hyU/laX02UUsCCaE-EK2s2eNoqTUdL-Pvz/STJgAHWzyAf2hMK7AEKMKeZXCHxXTUeBFP/FcCC1zCw8C-rlcb="

# headers = {
#     "sec-ch-ua-platform": '"Windows"',
#     "referer": "https://www.tiktok.com/foryou",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                   "AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/131.0.0.0 Safari/537.36",
#     "sec-ch-ua": '"Chromium";v="140", "Not=A?Brand";v="24", "HeadlessChrome";v="140"',
#     "accept-language": "en-US",
#     "sec-ch-ua-mobile": "?0",
#     "accept": "*/*",
#     "accept-encoding": "gzip, deflate, br"
# }

# resp = requests.get(url, headers=headers, impersonate="chrome131")

# print("Status:", resp.status_code)
# print("Length:", len(resp.content))
# print("Preview:", resp.text[:600])



# from curl_cffi import requests

# url = "https://www.tiktok.com/api/recommend/item_list/?WebIdLastTime=1762581109&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/131.0.0.0%20Safari/537.36&channel=tiktok_web&clientABVersions=70508271,73547759,73720541,74536863,74609146,74627578,74632791,74674281,74700792,74703728,74746521,74746610,74767852,74780476,74792133,74793837,74798356,74803470,74810092,74811360,74819401,74824021,74837697,74851987,74860162,74872266,74874618,74879784,74891663,70405643,71057832,71200802,72361809,73171280,73208420,74276218,74844724&cookie_enabled=true&count=6&coverFormat=2&cpu_core_number=12&dark_mode=false&data_collection_enabled=false&day_of_week=6&device_id=7570228203412653599&device_platform=web_pc&device_score=8.57&device_type=web_h264&enable_cache=false&focus_state=true&from_page=fyp&history_len=2&isNonPersonalized=false&is_fullscreen=false&is_new_user=true&is_page_visible=true&itemID=&language=en&launch_mode=direct&network=1.45&odinId=7570228207740371998&os=windows&priority_region=&pullType=1&referer=&region=US&screen_height=1080&screen_width=1920&showAboutThisAd=true&showAds=false&time_of_day=0&tz_name=America%2FNew_York&video_encoding=&vv_count=0&vv_count_fyp=0&watchLiveLastTime=&webcast_language=en&window_height=1080&window_width=1920&msToken=3CXF5gtLCZoefre-S-eMeThX-99COhGlKIh2rEEG7cYvMh-VpC-r-djUYI_75ZwDMVz8aOx_4K-WwwT3WWoXzRKEi_Jx8R-SVLx-eE57XicD95Pyq9zFUEd67nZm9w==&X-Bogus=DFSzsIRLnzxANr9YCPYAgL13rHAP&X-Gnarly=MPuzB363FRiRoVsWC3QofupCm3ZI5ejse6H86Q2DLLK6gjLazwoY2OsYkHFYwbERhz5bUPbPtAajiMTiXUREWhc-uynN6D9dzkSdbLClCaA5AJAdqJxy5ZKjmNwXdy/c1HtuVOI11ex9wfkOIDFtTzkjbZBTZl8D7At795eSW7cpro8jWIjsONmS1YwT0y9pFGI7YVrnLD4ipUaJC1jfRgXGC7/6Tm/CFn9xi8wgdwp-XxSJdG09QmlpYIYr1qODy6XhRK3x9pYnmj-r8vyZh553iazCLNNo9ipRTakDf2PYabeUy9ZI86fFD9AlpE5nEhk="

# headers = {
#     "accept": "*/*",
#     "accept-language": "en-US",
#     "priority": "u=1, i",
#     "referer": "https://www.tiktok.com/foryou",
#     "sec-ch-ua": '"Not=A?Brand";v="24", "Chromium";v="140"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": '"Windows"',
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-origin",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
#     "accept-encoding": "gzip, deflate, br"
# }

# cookies = {
#     "tt_csrf_token": "Z4fQGUwS-7_aut3_r4ZbpEilKbPlhgwTV6S4",
#     "tt_chain_token": "18jbkfK2jv4Z2SXL6NO0lQ==",
#     "tiktok_webapp_theme_source": "auto",
#     "tiktok_webapp_theme": "dark",
#     "ttwid": "1|5cGI9QDdASBnypmIg5nj8ij9ETffNGff9nNZW733EAM|1762581112|3e7f01d27e121c1cdd96cae8ded4a964b39c77537d3375076b0092227779f5ca",
#     "msToken": "3CXF5gtLCZoefre-S-eMeThX-99COhGlKIh2rEEG7cYvMh-VpC-r-djUYI_75ZwDMVz8aOx_4K-WwwT3WWoXzRKEi_Jx8R-SVLx-eE57XicD95Pyq9zFUEd67nZm9w=="
# }

# resp = requests.get(url, headers=headers, cookies=cookies, impersonate="chrome131")

# print("Status:", resp.status_code)
# print("Length:", len(resp.content))
# print("Preview:", resp.text[:600])


# fyp scraper -> profile scraper -> video downloader -> 



# from curl_cffi import requests
# from curl_cffi import requests
# print(requests.__doc__)


# url = "https://www.tiktok.com/api/post/item_list/?WebIdLastTime=1736951461&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/142.0.0.0%20Safari/537.36%20Edg/142.0.0.0&channel=tiktok_web&cookie_enabled=true&count=35&coverFormat=2&cursor=0&data_collection_enabled=true&device_id=7460149314773288494&device_platform=web_pc&focus_state=true&history_len=3&is_fullscreen=false&is_page_visible=true&language=en&odinId=7478784916198065170&os=windows&priority_region=US&referer=&region=US&screen_height=1080&screen_width=1920&secUid=MS4wLjABAAAAuYqWobyva4J42slRnXv8wgmO_0pv9NozRrmQ0vk1v33qPL5_qCpyoR-P_KpYBg4e&tz_name=Asia%2FSeoul&user_is_login=true&video_encoding=mp4&webcast_language=en&msToken=RyhisauVXdxKv0O64DCfY4KB4b9r4ss_hDOwPW3GGCmCSv0loXbaFhRNkObBNc3VFqRrS0ECObGorQptfHkSAY_EKroVB3MiseTpS0xyvDlBLMVub9L2V1LkG6RyZ-w_iGphoH5rApAI_7EX0dWGbKQIIw==&X-Bogus=DFSzsIVOmDJANnUoCOpfi9E-pInq&X-Gnarly=MJeMDy64wG1J3lr-dAa4/xhuKoSPFGTGLmo0KMvEmEj-Z2zYVv8CYc9EgooS0YoL8J0vqmya9ogjxmyjZ5v98bxTdtyV0ohjm7IG/1axe5cgwYujAscD6/h7Ds9PSIjug-nG0YmGU-MisFG3zc5BD7nork6hxCeYtDM7RXN69oNy2lGWwHf/NZ1YnHA4aVx8kP5H11B3Ky5lGuf0flfwJRE10PiPbVx8smPvNVxs1ImvRAg/BK-7U4n9DMh4PLL3wkhd5K3HSnSZFyAhqVRHRZj-hLbNQPuLo7Nkr98OKJMGRIBAKz1AnB9BktB-BJNF9Tv="

# headers = {
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
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
# }

# cookies = {
#     "ttwid": "1|S7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk|1762923750|999013bdc8124b401cb2d236d9dd57d5b5fc7730d2932fb50e5778987eedbd40",
#     "sessionid": "c6960424c3048f7c6e0978192e012638",
#     "sid_tt": "c6960424c3048f7c6e0978192e012638",
#     "tt_chain_token": "g/awArl40iOADD0hHi9e/Q==",
#     "tt_csrf_token": "xYWajjO9-89aI0fRrZo-yJnaslhIXLFs-kW8",
#     "tiktok_webapp_theme": "dark",
#     "tiktok_webapp_theme_source": "auto",
# }

# # ✅ use chrome110 or chrome124 for 0.6.3 builds
# r = requests.get(url, headers=headers, cookies=cookies, impersonate="chrome120", timeout=30)

# print(r.status_code)
# print(r.text[:1000])





# import pycurl
# from io import BytesIO

# url = "https://www.tiktok.com/api/post/item_list/?WebIdLastTime=1736951461&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F142.0.0.0%20Safari%2F537.36%20Edg%2F142.0.0.0&channel=tiktok_web&cookie_enabled=true&count=35&coverFormat=2&cursor=0&data_collection_enabled=true&device_id=7460149314773288494&device_platform=web_pc&focus_state=true&history_len=3&is_fullscreen=false&is_page_visible=true&language=en&odinId=7478784916198065170&os=windows&priority_region=US&referer=&region=US&screen_height=1080&screen_width=1920&secUid=MS4wLjABAAAAuYqWobyva4J42slRnXv8wgmO_0pv9NozRrmQ0vk1v33qPL5_qCpyoR-P_KpYBg4e&tz_name=Asia%2FSeoul&user_is_login=true&video_encoding=mp4&webcast_language=en&msToken=RyhisauVXdxKv0O64DCfY4KB4b9r4ss_hDOwPW3GGCmCSv0loXbaFhRNkObBNc3VFqRrS0ECObGorQptfHkSAY_EKroVB3MiseTpS0xyvDlBLMVub9L2V1LkG6RyZ-w_iGphoH5rApAI_7EX0dWGbKQIIw==&X-Bogus=DFSzsIVOmDJANnUoCOpfi9E-pInq&X-Gnarly=MJeMDy64wG1J3lr-dAa4/xhuKoSPFGTGLmo0KMvEmEj-Z2zYVv8CYc9EgooS0YoL8J0vqmya9ogjxmyjZ5v98bxTdtyV0ohjm7IG/1axe5cgwYujAscD6/h7Ds9PSIjug-nG0YmGU-MisFG3zc5BD7nork6hxCeYtDM7RXN69oNy2lGWwHf/NZ1YnHA4aVx8kP5H11B3Ky5lGuf0flfwJRE10PiPbVx8smPvNVxs1ImvRAg/BK-7U4n9DMh4PLL3wkhd5K3HSnSZFyAhqVRHRZj-hLbNQPuLo7Nkr98OKJMGRIBAKz1AnB9BktB-BJNF9Tv="

# cookie_str = """cookie-consent={%22optional%22:true%2C%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22hubspot%22:true%2C%22version%22:%22v10%22}; living_user_id=149999902702; tt_chain_token=g/awArl40iOADD0hHi9e/Q==; d_ticket=578cfb16f8d0da5d1f57811147ae32c1d1e4c; uid_tt=91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8; uid_tt_ss=91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8; sid_tt=c6960424c3048f7c6e0978192e012638; sessionid=c6960424c3048f7c6e0978192e012638; sessionid_ss=c6960424c3048f7c6e0978192e012638; store-idc=alisg; store-country-code=kr; store-country-code-src=uid; tt-target-idc=alisg; tt-target-idc-sign=jHcAJBth816HHWGYqpllY256Vw_XVnCFfgixI3_n23HZ8S9rc7uuJBy3lnZ69b6Lr-1s8Y2GP1RyOFAqPJOkmhJiSPC3w_-kvcpRCMG2_Lukc7i4fz-oh6V_QQvmQDqNCgP8UsHB_H-doJa_c73ADQM1cdxzfZ8ShMmIAi3TjpWjbwpU7fD1CNP8jPvqwEwMooHsXIGzhim5NP6iPydcpPFF03qitP0iPfpmRE2oCW4wYgBudTEQda95IYFPRBKVzbVLpQXhLZzzDPlqx894-oZZmhCgLc9CNoCyMaIVZlHvZ_fmW1v33PGRqPJxhxJP3At6jquz1qa_0_2CqNQ9qvwgRP5N79WQz5vidtT7so8o53vUVPt8I6qO0nvM7r8JHo66L4i9-q_ThXG3-2na1yz2Hyn8L54_o4Dn-ETt55-Cx__sgsWvYPgp8TF5jYdO9NouUQMSWJ8gUvq42P_SOnHRse8eksZCOPOkESCKl-O7c7RtKFAI8kP2ltJ9E6e5; ttwid=1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1752014034%7Cba59cb191a734d94f19af0f0136fe84f44d8797f1d8dcacf49a9ae2f8747e9db; ..."""  # (truncate for brevity)

# headers = [
#     "accept: */*",
#     "accept-language: en-US,en;q=0.9",
#     "priority: u=1, i",
#     "referer: https://www.tiktok.com/@lisen.tech",
#     "sec-ch-ua: \"Chromium\";v=\"142\", \"Microsoft Edge\";v=\"142\", \"Not_A Brand\";v=\"99\"",
#     "sec-ch-ua-mobile: ?0",
#     "sec-ch-ua-platform: \"Windows\"",
#     "sec-fetch-dest: empty",
#     "sec-fetch-mode: cors",
#     "sec-fetch-site: same-origin",
#     "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
# ]

# buffer = BytesIO()
# c = pycurl.Curl()
# c.setopt(pycurl.URL, url)
# c.setopt(pycurl.HTTPHEADER, headers)
# c.setopt(pycurl.COOKIE, cookie_str)
# c.setopt(pycurl.HTTP_VERSION, pycurl.CURL_HTTP_VERSION_2_0)
# c.setopt(pycurl.WRITEFUNCTION, buffer.write)
# c.perform()

# print("HTTP Code:", c.getinfo(pycurl.RESPONSE_CODE))
# print("Content-Type:", c.getinfo(pycurl.CONTENT_TYPE))
# print(buffer.getvalue().decode("utf-8")[:400])
# c.close()



# import subprocess

# cmd = (
#     'cmd /c curl -s -L '
#     '"https://www.tiktok.com/api/post/item_list/?WebIdLastTime=1736951461&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/142.0.0.0%20Safari/537.36%20Edg/142.0.0.0&channel=tiktok_web&cookie_enabled=true&count=35&coverFormat=2&cursor=0&data_collection_enabled=true&device_id=7460149314773288494&device_platform=web_pc&focus_state=true&history_len=3&is_fullscreen=false&is_page_visible=true&language=en&odinId=7478784916198065170&os=windows&priority_region=US&referer=&region=US&screen_height=1080&screen_width=1920&secUid=MS4wLjABAAAAuYqWobyva4J42slRnXv8wgmO_0pv9NozRrmQ0vk1v33qPL5_qCpyoR-P_KpYBg4e&tz_name=Asia%2FSeoul&user_is_login=true&video_encoding=mp4&webcast_language=en&msToken=RyhisauVXdxKv0O64DCfY4KB4b9r4ss_hDOwPW3GGCmCSv0loXbaFhRNkObBNc3VFqRrS0ECObGorQptfHkSAY_EKroVB3MiseTpS0xyvDlBLMVub9L2V1LkG6RyZ-w_iGphoH5rApAI_7EX0dWGbKQIIw==&X-Bogus=DFSzsIVOmDJANnUoCOpfi9E-pInq&X-Gnarly=MJeMDy64wG1J3lr-dAa4/xhuKoSPFGTGLmo0KMvEmEj-Z2zYVv8CYc9EgooS0YoL8J0vqmya9ogjxmyjZ5v98bxTdtyV0ohjm7IG/1axe5cgwYujAscD6/h7Ds9PSIjug-nG0YmGU-MisFG3zc5BD7nork6hxCeYtDM7RXN69oNy2lGWwHf/NZ1YnHA4aVx8kP5H11B3Ky5lGuf0flfwJRE10PiPbVx8smPvNVxs1ImvRAg/BK-7U4n9DMh4PLL3wkhd5K3HSnSZFyAhqVRHRZj-hLbNQPuLo7Nkr98OKJMGRIBAKz1AnB9BktB-BJNF9Tv=" '
#     '-H "accept: */*" '
#     '-H "accept-language: en-US,en;q=0.9" '
#     '-H "referer: https://www.tiktok.com/@lisen.tech" '
#     '-H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#     'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0" '
#     '-b "ttwid=1|S7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk|1762923750|999013bdc8124b401cb2d236d9dd57d5b5fc7730d2932fb50e5778987eedbd40; '
#     'sessionid=c6960424c3048f7c6e0978192e012638; sid_tt=c6960424c3048f7c6e0978192e012638; '
#     'tt_chain_token=g/awArl40iOADD0hHi9e/Q==; tt_csrf_token=xYWajjO9-89aI0fRrZo-yJnaslhIXLFs-kW8"'
# )

# result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
# print("Return code:", result.returncode)
# print("STDERR:", result.stderr[:500])
# print("STDOUT:", result.stdout[:1000])
# print(result.stdout.encode('utf-8'))



# import subprocess
# import json
# import sys

# def fetch_tiktok_data():
#     """
#     Execute the curl command directly using subprocess
#     """
    
#     # The curl command (for Windows, using ^ for line continuation)
#     curl_command = [
#         'curl',
#         'https://www.tiktok.com/api/post/item_list/?WebIdLastTime=1736951461&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F142.0.0.0%20Safari%2F537.36%20Edg%2F142.0.0.0&channel=tiktok_web&cookie_enabled=true&count=35&coverFormat=2&cursor=0&data_collection_enabled=true&device_id=7460149314773288494&device_platform=web_pc&focus_state=true&history_len=3&is_fullscreen=false&is_page_visible=true&language=en&odinId=7478784916198065170&os=windows&priority_region=US&referer=&region=US&screen_height=1080&screen_width=1920&secUid=MS4wLjABAAAAuYqWobyva4J42slRnXv8wgmO_0pv9NozRrmQ0vk1v33qPL5_qCpyoR-P_KpYBg4e&tz_name=Asia%2FSeoul&user_is_login=true&video_encoding=mp4&webcast_language=en&msToken=RyhisauVXdxKv0O64DCfY4KB4b9r4ss_hDOwPW3GGCmCSv0loXbaFhRNkObBNc3VFqRrS0ECObGorQptfHkSAY_EKroVB3MiseTpS0xyvDlBLMVub9L2V1LkG6RyZ-w_iGphoH5rApAI_7EX0dWGbKQIIw==&X-Bogus=DFSzsIVOmDJANnUoCOpfi9E-pInq&X-Gnarly=MJeMDy64wG1J3lr-dAa4/xhuKoSPFGTGLmo0KMvEmEj-Z2zYVv8CYc9EgooS0YoL8J0vqmya9ogjxmyjZ5v98bxTdtyV0ohjm7IG/1axe5cgwYujAscD6/h7Ds9PSIjug-nG0YmGU-MisFG3zc5BD7nork6hxCeYtDM7RXN69oNy2lGWwHf/NZ1YnHA4aVx8kP5H11B3Ky5lGuf0flfwJRE10PiPbVx8smPvNVxs1ImvRAg/BK-7U4n9DMh4PLL3wkhd5K3HSnSZFyAhqVRHRZj-hLbNQPuLo7Nkr98OKJMGRIBAKz1AnB9BktB-BJNF9Tv=',
#         '-H', 'accept: */*',
#         '-H', 'accept-language: en-US,en;q=0.9',
#         '-b', 'cookie-consent={"optional":true,"ga":true,"af":true,"fbp":true,"lip":true,"bing":true,"ttads":true,"reddit":true,"hubspot":true,"version":"v10"}; living_user_id=149999902702; tt_chain_token=g/awArl40iOADD0hHi9e/Q==; d_ticket=578cfb16f8d0da5d1f57811147ae32c1d1e4c; uid_tt=91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8; uid_tt_ss=91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8; sid_tt=c6960424c3048f7c6e0978192e012638; sessionid=c6960424c3048f7c6e0978192e012638; sessionid_ss=c6960424c3048f7c6e0978192e012638; store-idc=alisg; store-country-code=kr; store-country-code-src=uid; tt-target-idc=alisg; tt-target-idc-sign=jHcAJBth816HHWGYqpllY256Vw_XVnCFfgixI3_n23HZ8S9rc7uuJBy3lnZ69b6Lr-1s8Y2GP1RyOFAqPJOkmhJiSPC3w_-kvcpRCMG2_Lukc7i4fz-oh6V_QQvmQDqNCgP8UsHB_H-doJa_c73ADQM1cdxzfZ8ShMmIAi3TjpWjbwpU7fD1CNP8jPvqwEwMooHsXIGzhim5NP6iPydcpPFF03qitP0iPfpmRE2oCW4wYgBudTEQda95IYFPRBKVzbVLpQXhLZzzDPlqx894-oZZmhCgLc9CNoCyMaIVZlHvZ_fmW1v33PGRqPJxhxJP3At6jquz1qa_0_2CqNQ9qvwgRP5N79WQz5vidtT7so8o53vUVPt8I6qO0nvM7r8JHo66L4i9-q_ThXG3-2na1yz2Hyn8L54_o4Dn-ETt55-Cx__sgsWvYPgp8TF5jYdO9NouUQMSWJ8gUvq42P_SOnHRse8eksZCOPOkESCKl-O7c7RtKFAI8kP2ltJ9E6e5; ttwid=1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1752014034%7Cba59cb191a734d94f19af0f0136fe84f44d8797f1d8dcacf49a9ae2f8747e9db; _ga=GA1.1.150342934.1752048579; _fbp=fb.1.1752048580728.1446697223; _ga_NBFTJ2P3P3=GS1.1.1752048579.1.1.1752048630.0.0.1773973896; pre_country=KR; lang_type=en; tta_attr_id_mirror=0.1755075598.7537992296453636097; _tt_enable_cookie=1; ttcsid=1755660196386::vRKZe4gsZbYCGZvSjeBW.1.1755660196386; ttcsid_C97F14JC77U63IDI7U40=1755660196385::1jScwBvAKvOay5Y3IDYq.1.1755660196625; _ga_Y2RSHPPW88=GS2.1.s1755660196$o1$g1$t1755660202$j0$l0$h858435056; _ga_HV1FL86553=GS2.1.s1755660196$o1$g0$t1755660202$j0$l0$h430147227; _ttp=31XBbVW8z3njdHMvhKmUgOZdYYp; _ga_TEQXTT9FE4=GS1.1.1756345152.1.1.1756345319.0.0.46985635; sid_guard=c6960424c3048f7c6e0978192e012638%7C1760468508%7C15552000%7CSun%2C+12-Apr-2026+19%3A01%3A48+GMT; tt_session_tlb_tag=sttt%7C4%7CxpYEJMMEj3xuCXgZLgEmOP_________fzOi7a8IbznWsP6_DCsp0-A9Tmjey7VZ_aYnyddUwa54%3D; sid_ucp_v1=1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA; ssid_ucp_v1=1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA; tiktok_webapp_theme_source=auto; tiktok_webapp_theme=dark; delay_guest_mode_vid=5; tt_csrf_token=xYWajjO9-89aI0fRrZo-yJnaslhIXLFs-kW8; perf_feed_cache={"expireTimestamp":1763096400000,"itemIds":["7571659024123317518","7571600769183452437","7571630534619729154"]}; store-country-sign=MEIEDHTam-nuJKKbIbSH7QQgiM2-9blpYoiGl5Naw92th_0qzSOUCKDlY709fUJwfFwEEI6hZi2-p7gVYC9aLt1A5zM; odin_tt=dcb093ff589a43fa427f3779b690ffc532deb0af3d87a656d18c0caff53a1e09bbd472c3a1ad8bd33e483932d275889e3b488a8e92f2b36e516c9acd21b6363febc2ae08903ee387c425feee42c462fd; msToken=RyhisauVXdxKv0O64DCfY4KB4b9r4ss_hDOwPW3GGCmCSv0loXbaFhRNkObBNc3VFqRrS0ECObGorQptfHkSAY_EKroVB3MiseTpS0xyvDlBLMVub9L2V1LkG6RyZ-w_iGphoH5rApAI_7EX0dWGbKQIIw==; passport_fe_beating_status=false; msToken=N61y7daWdOxog7ow1sHoYqACb6IUN3jjNCqjKLNENpzQa9pWp4wPBDymVJhBupwCZdBEt8wA2ZyBTtDCMW0V1bh56L_eY3yMp50ffUTZNOI8pZtPTbTh5_2e52xFX7al9JNg28FQBMtRCWJJDD6MnLNsQw==; ttwid=1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1762923750%7C999013bdc8124b401cb2d236d9dd57d5b5fc7730d2932fb50e5778987eedbd40',
#         '-H', 'priority: u=1, i',
#         '-H', 'referer: https://www.tiktok.com/@lisen.tech',
#         '-H', 'sec-ch-ua: "Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
#         '-H', 'sec-ch-ua-mobile: ?0',
#         '-H', 'sec-ch-ua-platform: "Windows"',
#         '-H', 'sec-fetch-dest: empty',
#         '-H', 'sec-fetch-mode: cors',
#         '-H', 'sec-fetch-site: same-origin',
#         '-H', 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0'
#     ]
    
#     try:
#         # Execute curl command
#         result = subprocess.run(
#             curl_command,
#             capture_output=True,
#             text=True,
#             shell=False
#         )
        
#         if result.returncode != 0:
#             print(f"Curl command failed with return code {result.returncode}")
#             print(f"Error: {result.stderr}")
#             return None
        
#         # Parse JSON response
#         data = json.loads(result.stdout)
#         return data
        
#     except json.JSONDecodeError as e:
#         print(f"Failed to parse JSON: {e}")
#         print(f"Raw output: {result.stdout[:500]}")
#         return None
#     except Exception as e:
#         print(f"Error executing curl: {e}")
#         return None


# if __name__ == "__main__":
#     # Fetch the data
#     print("Executing curl command...")
#     data = fetch_tiktok_data()
    
#     if data:
#         print("Successfully fetched data!")
#         print(f"\nData keys: {list(data.keys())}")
        
#         # Pretty print the JSON response
#         print("\nFull response:")
#         print(json.dumps(data, indent=2, ensure_ascii=False))
#     else:
#         print("Failed to fetch data")
#         sys.exit(1)



import subprocess
import json
import sys

def fetch_tiktok_data():
    """
    Execute the curl command directly using subprocess with proper encoding handling
    """
    
    # The curl command (for Windows, using ^ for line continuation)
    curl_command = [
        'curl',
        'https://www.tiktok.com/api/post/item_list/?WebIdLastTime=1736951461&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F142.0.0.0%20Safari%2F537.36%20Edg%2F142.0.0.0&channel=tiktok_web&cookie_enabled=true&count=35&coverFormat=2&cursor=0&data_collection_enabled=true&device_id=7460149314773288494&device_platform=web_pc&focus_state=true&history_len=3&is_fullscreen=false&is_page_visible=true&language=en&odinId=7478784916198065170&os=windows&priority_region=US&referer=&region=US&screen_height=1080&screen_width=1920&secUid=MS4wLjABAAAAuYqWobyva4J42slRnXv8wgmO_0pv9NozRrmQ0vk1v33qPL5_qCpyoR-P_KpYBg4e&tz_name=Asia%2FSeoul&user_is_login=true&video_encoding=mp4&webcast_language=en&msToken=RyhisauVXdxKv0O64DCfY4KB4b9r4ss_hDOwPW3GGCmCSv0loXbaFhRNkObBNc3VFqRrS0ECObGorQptfHkSAY_EKroVB3MiseTpS0xyvDlBLMVub9L2V1LkG6RyZ-w_iGphoH5rApAI_7EX0dWGbKQIIw==&X-Bogus=DFSzsIVOmDJANnUoCOpfi9E-pInq&X-Gnarly=MJeMDy64wG1J3lr-dAa4/xhuKoSPFGTGLmo0KMvEmEj-Z2zYVv8CYc9EgooS0YoL8J0vqmya9ogjxmyjZ5v98bxTdtyV0ohjm7IG/1axe5cgwYujAscD6/h7Ds9PSIjug-nG0YmGU-MisFG3zc5BD7nork6hxCeYtDM7RXN69oNy2lGWwHf/NZ1YnHA4aVx8kP5H11B3Ky5lGuf0flfwJRE10PiPbVx8smPvNVxs1ImvRAg/BK-7U4n9DMh4PLL3wkhd5K3HSnSZFyAhqVRHRZj-hLbNQPuLo7Nkr98OKJMGRIBAKz1AnB9BktB-BJNF9Tv=',
        '-H', 'accept: */*',
        '-H', 'accept-language: en-US,en;q=0.9',
        '-b', 'cookie-consent={"optional":true,"ga":true,"af":true,"fbp":true,"lip":true,"bing":true,"ttads":true,"reddit":true,"hubspot":true,"version":"v10"}; living_user_id=149999902702; tt_chain_token=g/awArl40iOADD0hHi9e/Q==; d_ticket=578cfb16f8d0da5d1f57811147ae32c1d1e4c; uid_tt=91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8; uid_tt_ss=91e305cc67f3ebc8bc9dc50e9ab9476730069d7fecdd0086936545011db48fc8; sid_tt=c6960424c3048f7c6e0978192e012638; sessionid=c6960424c3048f7c6e0978192e012638; sessionid_ss=c6960424c3048f7c6e0978192e012638; store-idc=alisg; store-country-code=kr; store-country-code-src=uid; tt-target-idc=alisg; tt-target-idc-sign=jHcAJBth816HHWGYqpllY256Vw_XVnCFfgixI3_n23HZ8S9rc7uuJBy3lnZ69b6Lr-1s8Y2GP1RyOFAqPJOkmhJiSPC3w_-kvcpRCMG2_Lukc7i4fz-oh6V_QQvmQDqNCgP8UsHB_H-doJa_c73ADQM1cdxzfZ8ShMmIAi3TjpWjbwpU7fD1CNP8jPvqwEwMooHsXIGzhim5NP6iPydcpPFF03qitP0iPfpmRE2oCW4wYgBudTEQda95IYFPRBKVzbVLpQXhLZzzDPlqx894-oZZmhCgLc9CNoCyMaIVZlHvZ_fmW1v33PGRqPJxhxJP3At6jquz1qa_0_2CqNQ9qvwgRP5N79WQz5vidtT7so8o53vUVPt8I6qO0nvM7r8JHo66L4i9-q_ThXG3-2na1yz2Hyn8L54_o4Dn-ETt55-Cx__sgsWvYPgp8TF5jYdO9NouUQMSWJ8gUvq42P_SOnHRse8eksZCOPOkESCKl-O7c7RtKFAI8kP2ltJ9E6e5; ttwid=1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1752014034%7Cba59cb191a734d94f19af0f0136fe84f44d8797f1d8dcacf49a9ae2f8747e9db; _ga=GA1.1.150342934.1752048579; _fbp=fb.1.1752048580728.1446697223; _ga_NBFTJ2P3P3=GS1.1.1752048579.1.1.1752048630.0.0.1773973896; pre_country=KR; lang_type=en; tta_attr_id_mirror=0.1755075598.7537992296453636097; _tt_enable_cookie=1; ttcsid=1755660196386::vRKZe4gsZbYCGZvSjeBW.1.1755660196386; ttcsid_C97F14JC77U63IDI7U40=1755660196385::1jScwBvAKvOay5Y3IDYq.1.1755660196625; _ga_Y2RSHPPW88=GS2.1.s1755660196$o1$g1$t1755660202$j0$l0$h858435056; _ga_HV1FL86553=GS2.1.s1755660196$o1$g0$t1755660202$j0$l0$h430147227; _ttp=31XBbVW8z3njdHMvhKmUgOZdYYp; _ga_TEQXTT9FE4=GS1.1.1756345152.1.1.1756345319.0.0.46985635; sid_guard=c6960424c3048f7c6e0978192e012638%7C1760468508%7C15552000%7CSun%2C+12-Apr-2026+19%3A01%3A48+GMT; tt_session_tlb_tag=sttt%7C4%7CxpYEJMMEj3xuCXgZLgEmOP_________fzOi7a8IbznWsP6_DCsp0-A9Tmjey7VZ_aYnyddUwa54%3D; sid_ucp_v1=1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA; ssid_ucp_v1=1.0.0-KGIxOWM0ZjY2MWY3NjRhNzVlZWQwNjA3OGMyNGEzZWE1MWE4YmY4ZTQKGgiSiKTMnOj-5GcQnLy6xwYYsws4AUDqB0gEEAMaAm15IiBjNjk2MDQyNGMzMDQ4ZjdjNmUwOTc4MTkyZTAxMjYzOA; tiktok_webapp_theme_source=auto; tiktok_webapp_theme=dark; delay_guest_mode_vid=5; tt_csrf_token=xYWajjO9-89aI0fRrZo-yJnaslhIXLFs-kW8; perf_feed_cache={"expireTimestamp":1763096400000,"itemIds":["7571659024123317518","7571600769183452437","7571630534619729154"]}; store-country-sign=MEIEDHTam-nuJKKbIbSH7QQgiM2-9blpYoiGl5Naw92th_0qzSOUCKDlY709fUJwfFwEEI6hZi2-p7gVYC9aLt1A5zM; odin_tt=dcb093ff589a43fa427f3779b690ffc532deb0af3d87a656d18c0caff53a1e09bbd472c3a1ad8bd33e483932d275889e3b488a8e92f2b36e516c9acd21b6363febc2ae08903ee387c425feee42c462fd; msToken=RyhisauVXdxKv0O64DCfY4KB4b9r4ss_hDOwPW3GGCmCSv0loXbaFhRNkObBNc3VFqRrS0ECObGorQptfHkSAY_EKroVB3MiseTpS0xyvDlBLMVub9L2V1LkG6RyZ-w_iGphoH5rApAI_7EX0dWGbKQIIw==; passport_fe_beating_status=false; msToken=N61y7daWdOxog7ow1sHoYqACb6IUN3jjNCqjKLNENpzQa9pWp4wPBDymVJhBupwCZdBEt8wA2ZyBTtDCMW0V1bh56L_eY3yMp50ffUTZNOI8pZtPTbTh5_2e52xFX7al9JNg28FQBMtRCWJJDD6MnLNsQw==; ttwid=1%7CS7yTInj6u8v8I8XVKFxkN3NKUnl9Ynoxji3Bh0VoVzk%7C1762923750%7C999013bdc8124b401cb2d236d9dd57d5b5fc7730d2932fb50e5778987eedbd40',
        '-H', 'priority: u=1, i',
        '-H', 'referer: https://www.tiktok.com/@lisen.tech',
        '-H', 'sec-ch-ua: "Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
        '-H', 'sec-ch-ua-mobile: ?0',
        '-H', 'sec-ch-ua-platform: "Windows"',
        '-H', 'sec-fetch-dest: empty',
        '-H', 'sec-fetch-mode: cors',
        '-H', 'sec-fetch-site: same-origin',
        '-H', 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0'
    ]
    
    try:
        # Execute curl command - capture as bytes to avoid encoding issues
        result = subprocess.run(
            curl_command,
            capture_output=True,
            shell=False
        )
        
        if result.returncode != 0:
            print(f"Curl command failed with return code {result.returncode}")
            print(f"Error: {result.stderr.decode('utf-8', errors='ignore')}")
            return None
        
        # Decode as UTF-8 and parse JSON
        output_text = result.stdout.decode('utf-8', errors='ignore')
        data = json.loads(output_text)
        return data
        
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
        try:
            print(f"Raw output (first 500 chars): {result.stdout.decode('utf-8', errors='ignore')[:500]}")
        except:
            print("Could not decode output")
        return None
    except Exception as e:
        print(f"Error executing curl: {e}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    # Fetch the data
    print("Executing curl command...")
    data = fetch_tiktok_data()
    
    if data:
        print("Successfully fetched data!")
        print(f"\nData keys: {list(data.keys())}")
        
        # Check if we have items
        if 'itemList' in data:
            print(f"Number of items: {len(data['itemList'])}")
        
        # Pretty print the JSON response (limited output)
        print("\nFull response (first 1000 chars):")
        json_str = json.dumps(data, indent=2, ensure_ascii=False)
        print(json_str[:1000] + "..." if len(json_str) > 1000 else json_str)
    else:
        print("Failed to fetch data")
        sys.exit(1)