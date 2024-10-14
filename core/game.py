import requests

from hokireceh_claimer import base
from core.headers import headers


def join(data, proxies=None):
    url = "https://birdx-api2.birds.dog/minigame/egg/join"

    try:
        response = requests.get(
            url=url,
            headers=headers(tele_auth=data),
            proxies=proxies,
            timeout=20,
        )
        data = response.json()

        return data
    except:
        return None


def turn(data, proxies=None):
    url = "https://birdx-api2.birds.dog/minigame/egg/turn"

    try:
        response = requests.get(
            url=url,
            headers=headers(tele_auth=data),
            proxies=proxies,
            timeout=20,
        )
        data = response.json()

        return data
    except:
        return None


def play(data, proxies=None):
    url = "https://birdx-api2.birds.dog/minigame/egg/play"

    try:
        response = requests.get(
            url=url,
            headers=headers(tele_auth=data),
            proxies=proxies,
            timeout=20,
        )
        data = response.json()

        return data
    except:
        return None


def claim(data, proxies=None):
    url = "https://birdx-api2.birds.dog/minigame/egg/claim"

    try:
        response = requests.get(
            url=url,
            headers=headers(tele_auth=data),
            proxies=proxies,
            timeout=20,
        )
        data = response.text

        return data
    except:
        return None


def process_break_egg(data, proxies=None):
    while True:
        start_join = join(data=data, proxies=proxies)
        get_turn = turn(data=data, proxies=proxies)
        
        if get_turn is None:
            base.log(f"{base.white}자동 알 깨기: {base.red}턴 정보를 가져오는데 실패했습니다")
            break
        
        turns = get_turn.get("turn", 0)
        total = get_turn.get("total", 0)
        
        if turns > 0:
            start_play = play(data=data, proxies=proxies)
            result = start_play.get("result") if start_play else None
            if result:
                base.log(
                    f"{base.white}자동 알 깨기: {base.green}플레이 성공 {base.white}| {base.green}보상: {base.white}{result}"
                )
            else:
                base.log(f"{base.white}자동 알 깨기: {base.red}플레이 실패")
        elif total > 0:
            start_claim = claim(data=data, proxies=proxies)
            if start_claim:
                base.log(
                    f"{base.white}자동 알 깨기: {base.green}보상 수령 성공 | {total} 포인트 추가됨"
                )
            else:
                base.log(f"{base.white}자동 알 깨기: {base.red}보상 수령 실패")
            break
        else:
            base.log(f"{base.white}자동 알 깨기: {base.red}알을 깰 턴이 없습니다")
            break
