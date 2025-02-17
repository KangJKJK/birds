import requests

from hokireceh_claimer import base
from core.headers import headers


def make_request(url, data, proxies=None):
    try:
        response = requests.get(
            url=url,
            headers=headers(tele_auth=data),
            proxies=proxies,
            timeout=20,
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        base.log(f"{base.white}요청 실패: {base.red}{url} - {str(e)}")
        return None


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
    try:
        start_join = make_request("https://birdx-api2.birds.dog/minigame/egg/join", data, proxies)
        if not start_join:
            base.log(f"{base.white}자동 알 깨기: {base.red}게임 참여 실패")
            return

        base.log(f"{base.white}자동 알 깨기: {base.green}게임 참여 성공")

        total_reward = 0
        while True:
            get_turn = make_request("https://birdx-api2.birds.dog/minigame/egg/turn", data, proxies)
            if not get_turn:
                base.log(f"{base.white}자동 알 깨기: {base.red}턴 정보를 가져오는데 실패했습니다")
                break

            turns = get_turn.get("turn", 0)
            total = get_turn.get("total", 0)

            if turns > 0:
                start_play = make_request("https://birdx-api2.birds.dog/minigame/egg/play", data, proxies)
                if start_play:
                    result = start_play.get("result", 0)
                    total_reward += result
                    base.log(f"{base.white}자동 알 깨기: {base.green}플레이 성공 {base.white}| {base.green}보상: {base.white}{result} | 남은 턴: {turns-1}")
                else:
                    base.log(f"{base.white}자동 알 깨기: {base.red}플레이 실패")
            elif total > 0:
                start_claim = make_request("https://birdx-api2.birds.dog/minigame/egg/claim", data, proxies)
                if start_claim:
                    base.log(f"{base.white}자동 알 깨기: {base.green}보상 수령 성공 | 총 {total_reward} 포인트 추가됨")
                else:
                    base.log(f"{base.white}자동 알 깨기: {base.red}보상 수령 실패")
                break
            else:
                base.log(f"{base.white}자동 알 깨기: {base.yellow}알을 깰 턴이 없습니다")
                break

    except Exception as e:
        base.log(f"{base.white}자동 알 깨기: {base.red}예외 발생 - {str(e)}")
