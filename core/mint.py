import requests
import urllib.parse

from hokireceh_claimer import base
from core.headers import headers


def mint_status(data, proxies=None):
    url = "https://worm.birds.dog/worms/mint-status"

    try:
        # Get headers and ensure it's a dictionary
        header_dict = headers(auth=data)
        if not isinstance(header_dict, dict):
            raise TypeError(f"headers() returned {type(header_dict)} instead of dict")

        # URL encode the header values
        encoded_headers = {k: urllib.parse.quote(v) for k, v in header_dict.items()}
        
        response = requests.get(
            url=url,
            headers=encoded_headers,
            proxies=proxies,
            timeout=20,
        )
        response.raise_for_status()
        data = response.json()
        status = data["data"]["status"]

        return status
    except requests.exceptions.RequestException as e:
        base.log(f"{base.red}민트 상태 확인 중 요청 오류: {str(e)}")
        if isinstance(e, requests.exceptions.HTTPError) and e.response.status_code == 401:
            base.log(f"{base.red}인증 오류: 토큰이 만료되었거나 유효하지 않습니다.")
    except KeyError as e:
        base.log(f"{base.red}민트 상태 데이터 파싱 오류: {str(e)}")
    except TypeError as e:
        base.log(f"{base.red}헤더 생성 오류: {str(e)}")
    except Exception as e:
        base.log(f"{base.red}민트 상태 확인 중 예상치 못한 오류: {str(e)}")
    return None


def mint(data, proxies=None):
    url = "https://worm.birds.dog/worms/mint"

    try:
        response = requests.post(
            url=url,
            headers=headers(auth=data),
            json={},
            proxies=proxies,
            timeout=20,
        )
        data = response.json()

        return data
    except:
        return None


def process_mint_worm(data, proxies=None):
    status = mint_status(data=data, proxies=proxies)
    if status == "MINT_OPEN":
        start_mint_worm = mint(data=data, proxies=proxies)
        if start_mint_worm is None:
            base.log(f"{base.white}Auto Mint Worm: {base.red}Fail - 민팅 요청 실패")
            return
        mint_worm_status = start_mint_worm["message"] == "SUCCESS"
        if mint_worm_status:
            worm_type = start_mint_worm["minted"]["type"]
            energy = start_mint_worm["minted"]["reward"]
            base.log(
                f"{base.white}Auto Mint Worm: {base.green}Success {base.white}| {base.green}Worm type: {base.white}{worm_type} - {base.green}Energy: {base.white}{energy}"
            )
        else:
            base.log(f"{base.white}Auto Mint Worm: {base.red}Fail - {start_mint_worm.get('message', 'Unknown error')}")
    elif status == "WAITING":
        base.log(f"{base.white}Auto Mint Worm: {base.yellow}Not time to mint")
    elif status is None:
        base.log(f"{base.white}Auto Mint Worm: {base.red}상태 확인 불가 - 자세한 오류는 로그를 확인하세요")
    else:
        base.log(f"{base.white}Auto Mint Worm: {base.red}Unknown status - {status}")
