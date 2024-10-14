def headers(tele_auth=None, auth=None):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US;q=0.6,en;q=0.5",
        "Content-Type": "application/json",
        "Origin": "https://birdx.birds.dog",
        "Referer": "https://birdx.birds.dog/",
        "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    }

    if tele_auth:
        headers["Telegramauth"] = f"tma {tele_auth}"

    if auth:
        headers["Authorization"] = f"tma {auth}"

    return headers
