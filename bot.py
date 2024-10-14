import sys
import urllib.parse

sys.dont_write_bytecode = True

from hokireceh_claimer import base
from core.info import get_info
from core.task import process_do_task, process_boost_speed
from core.mint import process_mint_worm
from core.game import process_break_egg
from core.upgrade import process_upgrade

import time
from urllib.parse import parse_qs, unquote
import json


class Birds:
    def __init__(self):
        # 파일 디렉토리 가져오기
        self.data_file = base.file_path(file_name="data.txt")
        self.config_file = base.file_path(file_name="config.json")

        # 라인 초기화
        self.line = base.create_line(length=50)

        # 배너 초기화
        self.banner = base.create_banner(game_name="Birds")

        # 설정 가져오기
        self.auto_do_task = base.get_config(
            config_file=self.config_file, config_name="auto-do-task"
        )

        self.auto_boost_speed = base.get_config(
            config_file=self.config_file, config_name="auto-boost-speed"
        )

        self.auto_mint_worm = base.get_config(
            config_file=self.config_file, config_name="auto-mint-worm"
        )

        self.auto_break_egg = base.get_config(
            
            config_file=self.config_file, config_name="auto-break-egg"
        )

        self.auto_upgrade_egg = base.get_config(
            config_file=self.config_file, config_name="auto-upgrade-egg"
        )

    def main(self):
        while True:
            base.clear_terminal()
            print(self.banner)
            try:
                data = open(self.data_file, "r", encoding="utf-8").read().splitlines()
                base.log(f"{base.green}데이터 파일 읽기 성공")
            except Exception as e:
                base.log(f"{base.red}데이터 파일 읽기 실패: {e}")
                return

            num_acc = len(data)
            base.log(self.line)
            base.log(f"{base.green}계정 수: {base.white}{num_acc}")

            for no, account_data in enumerate(data):
                base.log(self.line)
                base.log(f"{base.green}계정 번호: {base.white}{no+1}/{num_acc}")
                base.log(f"{base.yellow}계정 데이터: {base.white}{account_data}")

                try:
                    # 정보 가져오기
                    base.log(f"{base.yellow}정보 가져오기 시도")
                    get_info(data=account_data)
                    base.log(f"{base.green}정보 가져오기 성공")

                    # 작업 수행
                    if self.auto_do_task:
                        base.log(f"{base.yellow}자동 작업 수행: {base.green}켜짐")
                        base.log(f"{base.yellow}작업 수행 시도")
                        parsed_data = process_do_task(account_data)
                        if parsed_data is None:
                            base.log(f"{base.red}작업 수행 실패")
                            continue
                        base.log(f"{base.green}작업 수행 성공")

                    if self.auto_speed_boost:
                        base.log(f"{base.yellow}자동 속도 부스트: {base.green}켜짐")
                        auto_speed_boost(parsed_data)
                    if self.auto_mint_worm:
                        base.log(f"{base.yellow}자동 지렁이 민팅: {base.green}켜짐")
                        auto_mint_worm(parsed_data)
                    if self.auto_hatch_egg:
                        base.log(f"{base.yellow}자동 알 깨기: {base.green}켜짐")
                        auto_hatch_egg(parsed_data)

                    # 알 업그레이드
                    if self.auto_upgrade_egg:
                        base.log(f"{base.yellow}자동 알 업그레이드: {base.green}켜짐")
                        process_upgrade(data=account_data)
                    else:
                        base.log(f"{base.yellow}자동 알 업그레이드: {base.red}꺼짐")

                except Exception as e:
                    base.log(f"{base.red}계정 처리 중 오류: {base.white}{e}")
                    base.log(f"{base.red}오류 상세 정보: {base.white}{str(e.__class__.__name__)}: {str(e)}")

            print()
            wait_time = 60 * 60
            base.log(f"{base.yellow}{int(wait_time/60)}분 대기!")
            time.sleep(wait_time)

def parse_data(data):
    base.log(f"{base.yellow}데이터 파싱 시작")
    try:
        # URL 디코딩
        decoded_data = urllib.parse.unquote(data)
        
        # 쿼리 문자열을 딕셔너리로 변환
        parsed_dict = dict(urllib.parse.parse_qsl(decoded_data))
        
        # user 필드가 JSON 문자열이므로 이를 파싱
        if 'user' in parsed_dict:
            parsed_dict['user'] = json.loads(parsed_dict['user'])
        
        base.log(f"{base.green}데이터 파싱 성공")
        return parsed_dict
    except Exception as e:
        base.log(f"{base.red}데이터 파싱 중 오류 발생: {str(e)}")
        return None

def process_do_task(data):
    base.log(f"{base.yellow}작업 수행 함수 시작")
    
    if data is None:
        base.log(f"{base.red}입력 데이터가 None입니다.")
        return None
    
    parsed_data = parse_data(data)
    if parsed_data is None:
        base.log(f"{base.red}데이터 파싱 실패")
        return None
    
    try:
        # 사용자 정보 출력
        user_info = parsed_data.get('user', {})
        base.log(f"{base.green}사용자 정보: {user_info}")
        
        # 여기에 실제 작업 수행 코드 추가
        # 예: API 호출, 데이터베이스 조작 등
        
        base.log(f"{base.green}작업 완료")
    
    except Exception as e:
        base.log(f"{base.red}작업 수행 중 오류 발생: {str(e)}")
        base.log(f"{base.red}오류 상세 정보: {str(e.__class__.__name__)}: {str(e)}")
        return None

    base.log(f"{base.yellow}작업 수행 함수 종료")
    return parsed_data  # 파싱된 데이터 반환

def auto_speed_boost(data):
    base.log(f"{base.yellow}자동 속도 부스트 시작")
    try:
        if data is None or 'speed' not in data:
            base.log(f"{base.red}속도 정보가 없습니다.")
            return
        current_speed = data['speed']
        base.log(f"{base.green}Current Speed: x {current_speed}")
        # 여기에 속도 부스트 로직 추가
    except Exception as e:
        base.log(f"{base.red}속도 부스트 중 오류 발생: {str(e)}")

def auto_mint_worm(data):
    base.log(f"{base.yellow}자동 지렁이 민팅 시작")
    try:
        if data is None or 'worm_mint_time' not in data:
            base.log(f"{base.red}지렁이 민팅 정보가 없습니다.")
            return
        # 여기에 지렁이 민팅 로직 추가
    except Exception as e:
        base.log(f"{base.red}지렁이 민팅 중 오류 발생: {str(e)}")

def auto_hatch_egg(data):
    base.log(f"{base.yellow}자동 알 깨기 시작")
    try:
        if data is None or 'eggs' not in data:
            base.log(f"{base.red}알 정보가 없습니다.")
            return
        eggs = data['eggs']
        # 여기에 알 깨기 로직 추가
    except Exception as e:
        base.log(f"{base.red}알 깨기 중 오류 발생: {str(e)}")

if __name__ == "__main__":
    try:
        birds = Birds()
        birds.main()
    except KeyboardInterrupt:
        sys.exit()
