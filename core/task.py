import requests
from urllib.parse import parse_qs, unquote
import json

from hokireceh_claimer import base
from core.headers import headers


def get_task(data, proxies=None):
    url = "https://birdx-api2.birds.dog/project"

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


def do_task(data, task_id, channel_id, slug, point, proxies=None):
    url = "https://birdx-api2.birds.dog/project/join-task"
    payload = {"taskId": task_id, "channelId": channel_id, "slug": slug, "point": point}

    try:
        response = requests.post(
            url=url,
            headers=headers(tele_auth=data),
            json=payload,
            proxies=proxies,
            timeout=20,
        )
        data = response.json()
        status = data["msg"] == "Successfully"

        return status
    except:
        return None


def check_completed_task(data, proxies=None):
    url = "https://birdx-api2.birds.dog/user-join-task"

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


def process_do_task(data):
    if data is None:
        base.log(f"{base.red}오류: 데이터가 None입니다.")
        return

    try:
        base.log(f"{base.yellow}처리할 데이터 구조: {base.white}{type(data)}")
        base.log(f"{base.yellow}데이터 내용: {base.white}{data}")

        user_info = data['user']
        user_id = user_info['id']
        username = user_info['username']

        base.log(f"{base.green}사용자 ID: {base.white}{user_id}")
        base.log(f"{base.green}사용자 이름: {base.white}{username}")

        # 자동 속도 부스트
        base.log(f"{base.yellow}자동 속도 부스트: {base.green}켜짐")
        current_speed = process_speed_boost(data)
        base.log(f"{base.green}Current Speed: x {current_speed}")

        # 자동 지렁이 민팅
        base.log(f"{base.yellow}자동 지렁이 민팅: {base.green}켜짐")
        mint_result = process_mint_worm(data)
        base.log(f"{base.green}Auto Mint Worm: {mint_result}")

        # 자동 알 깨기
        base.log(f"{base.yellow}자동 알 깨기: {base.green}켜짐")
        egg_result = process_break_egg(data)
        base.log(f"{base.green}Auto Break Egg: {egg_result}")

    except KeyError as e:
        base.log(f"{base.red}키 오류: {base.white}{e}")
        base.log(f"{base.yellow}데이터에서 필요한 키를 찾을 수 없습니다.")
    except Exception as e:
        base.log(f"{base.red}작업 수행 중 오류: {base.white}{e}")
    finally:
        base.log(f"{base.yellow}처리된 데이터: {base.white}{data}")


def boost_speed(data, proxies=None):
    url = "https://birdx-api2.birds.dog/minigame/boost-speed"

    try:
        response = requests.get(
            url=url,
            headers=headers(tele_auth=data),
            proxies=proxies,
            timeout=20,
        )
        data = response.json()
        speed = data["speed"]

        return speed
    except:
        return None


def update_speed(data, speed, proxies=None):
    url = "https://birdx-api2.birds.dog/minigame/boost-speed/update-speed"
    payload = {"speed": speed}

    try:
        response = requests.post(
            url=url,
            headers=headers(tele_auth=data),
            json=payload,
            proxies=proxies,
            timeout=20,
        )
        data = response.json()
        status = data["msg"] == "Successfully"

        return status
    except:
        return None


def process_boost_speed(data, proxies=None):
    speed_list = [1, 1.2, 1.4, 1.6, 1.8, 2, 2.5]
    current_speed = boost_speed(data=data, proxies=proxies)
    next_speed = (
        speed_list[speed_list.index(current_speed) + 1]
        if current_speed in speed_list and current_speed != speed_list[-1]
        else None
    )
    if next_speed:
        base.log(
            f"{base.green}Current Speed: {base.white}x {current_speed} - {base.green}Next Speed: {base.white}x {next_speed}"
        )
        update_speed_status = update_speed(data=data, speed=next_speed, proxies=proxies)
        if update_speed_status:
            base.log(f"{base.white}Auto Boost Speed: {base.green}Success")
        else:
            base.log(f"{base.white}Auto Boost Speed: {base.red}Requirement not meet")
    else:
        base.log(
            f"{base.green}Current Speed: {base.white}x {current_speed} - {base.green}Max speed reached"
        )
