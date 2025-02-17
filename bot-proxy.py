import sys

sys.dont_write_bytecode = True

from hokireceh_claimer import base
from core.info import get_info
from core.task import process_do_task, process_boost_speed
from core.mint import process_mint_worm
from core.game import process_break_egg
from core.upgrade import process_upgrade

import time
import json


class Birds:
    def __init__(self):
        # 파일 디렉토리 가져오기
        self.data_file = base.file_path(file_name="data-proxy.json")
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
            accounts = json.load(open(self.data_file, "r"))["accounts"]
            num_acc = len(accounts)
            base.log(self.line)
            base.log(f"{base.green}계정 수: {base.white}{num_acc}")

            for no, account in enumerate(accounts):
                base.log(self.line)
                base.log(f"{base.green}계정 번호: {base.white}{no+1}/{num_acc}")
                data = account["acc_info"]
                proxy_info = account["proxy_info"]
                parsed_proxy_info = base.parse_proxy_info(proxy_info)
                if parsed_proxy_info is None:
                    break

                actual_ip = base.check_ip(proxy_info=proxy_info)

                proxies = base.format_proxy(proxy_info=proxy_info)

                try:
                    get_info(data=data, proxies=proxies)

                    # 작업 수행
                    if self.auto_do_task:
                        base.log(f"{base.yellow}자동 작업 수행: {base.green}켜짐")
                        process_do_task(data=data, proxies=proxies)
                    else:
                        base.log(f"{base.yellow}자동 작업 수행: {base.red}꺼짐")

                    # 속도 부스트
                    if self.auto_boost_speed:
                        base.log(f"{base.yellow}자동 속도 부스트: {base.green}켜짐")
                        process_boost_speed(data=data, proxies=proxies)
                    else:
                        base.log(f"{base.yellow}자동 속도 부스트: {base.red}꺼짐")

                    # 지렁이 민팅
                    if self.auto_mint_worm:
                        base.log(f"{base.yellow}자동 지렁이 민팅: {base.green}켜짐")
                        process_mint_worm(data=data, proxies=proxies)
                    else:
                        base.log(f"{base.yellow}자동 지렁이 민팅: {base.red}꺼짐")

                    # 알 깨기
                    if self.auto_break_egg:
                        base.log(f"{base.yellow}자동 알 깨기: {base.green}켜짐")
                        process_break_egg(data=data, proxies=proxies)
                    else:
                        base.log(f"{base.yellow}자동 알 깨기: {base.red}꺼짐")

                    # 알 업그레이드
                    if self.auto_upgrade_egg:
                        base.log(f"{base.yellow}자동 알 업그레이드: {base.green}켜짐")
                        process_upgrade(data=data, proxies=proxies)
                    else:
                        base.log(f"{base.yellow}자동 알 업그레이드: {base.red}꺼짐")

                    get_info(data=data, proxies=proxies)

                except Exception as e:
                    base.log(f"{base.red}오류: {base.white}{e}")

            print()
            wait_time = 60 * 60
            base.log(f"{base.yellow}{int(wait_time/60)}분 대기!")
            time.sleep(wait_time)


if __name__ == "__main__":
    try:
        birds = Birds()
        birds.main()
    except KeyboardInterrupt:
        sys.exit()
