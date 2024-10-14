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
            base.log(f"{base.white}Auto Break Egg: {base.red}Failed to get turn information")
            break
        
        turns = get_turn.get("turn", 0)
        total = get_turn.get("total", 0)
        
        if turns > 0:
            start_play = play(data=data, proxies=proxies)
            result = start_play.get("result") if start_play else None
            if result:
                base.log(
                    f"{base.white}Auto Break Egg: {base.green}Play Success {base.white}| {base.green}Reward: {base.white}{result}"
                )
            else:
                base.log(f"{base.white}Auto Break Egg: {base.red}Play Fail")
        elif total > 0:
            start_claim = claim(data=data, proxies=proxies)
            if start_claim:
                base.log(
                    f"{base.white}Auto Break Egg: {base.green}Claim Success | Added {total} points"
                )
            else:
                base.log(f"{base.white}Auto Break Egg: {base.red}Claim Fail")
            break
        else:
            base.log(f"{base.white}Auto Break Egg: {base.red}No turn to crack egg")
            break

