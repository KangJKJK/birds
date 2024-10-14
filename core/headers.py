import platform
from hokireceh_claimer import base

def headers(tele_auth=None, auth=None):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/json",
        "Origin": "https://birdx.birds.dog",
        "Referer": "https://birdx.birds.dog/",
        "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": f'"{platform.system()}"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    }

    if tele_auth:
        headers["Telegramauth"] = tele_auth
        base.log(f"{base.white}Telegramauth 헤더 추가됨: {base.green}{tele_auth[:10]}...")

    if auth:
        headers["Authorization"] = f"Bearer {auth}"
        base.log(f"{base.white}Authorization 헤더 추가됨: {base.green}Bearer {auth[:10]}...")

    return headers
