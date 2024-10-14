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


def process_break_egg(data):
    if data is None:
        base.log(f"{base.red}오류: 데이터가 None입니다.")
        return None

    try:
        # 여기에 알 깨기 로직을 구현합니다.
        # 예를 들어:
        user_id = data['user']['id']
        # API 호출 또는 다른 로직을 통해 알 깨기 작업을 수행
        result = "알 깨기 성공"  # 실제 결과로 대체해야 합니다.
        return result
    except KeyError as e:
        base.log(f"{base.red}키 오류 (알 깨기): {base.white}{e}")
        return None
    except Exception as e:
        base.log(f"{base.red}알 깨기 중 오류: {base.white}{e}")
        return None


def process_speed_boost(data):
    if data is None:
        base.log(f"{base.red}오류: 데이터가 None입니다.")
        return None

    try:
        # 속도 부스트 로직 구현
        user_id = data['user']['id']
        # API 호출 또는 다른 로직을 통해 속도 부스트 작업을 수행
        current_speed = "5"  # 실제 속도로 대체해야 합니다.
        return current_speed
    except KeyError as e:
        base.log(f"{base.red}키 오류 (속도 부스트): {base.white}{e}")
        return None
    except Exception as e:
        base.log(f"{base.red}속도 부스트 중 오류: {base.white}{e}")
        return None


def process_mint_worm(data):
    if data is None:
        base.log(f"{base.red}오류: 데이터가 None입니다.")
        return None

    try:
        # 지렁이 민팅 로직 구현
        user_id = data['user']['id']
        # API 호출 또는 다른 로직을 통해 지렁이 민팅 작업을 수행
        result = "지렁이 민팅 성공"  # 실제 결과로 대체해야 합니다.
        return result
    except KeyError as e:
        base.log(f"{base.red}키 오류 (지렁이 민팅): {base.white}{e}")
        return None
    except Exception as e:
        base.log(f"{base.red}지렁이 민팅 중 오류: {base.white}{e}")
        return None
