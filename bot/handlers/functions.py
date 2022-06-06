from time import time
import requests
from config import config


def get_warns(user_id):
    url = config.WEB_URL + ""
    params = [user_id]
    return requests.get(url=url,params=params)


def mute_time(user_id):
    warns = get_warns(user_id=user_id)
    _time = time() + warns * 600 + (warns - 1) * 600
    return _time


def get_faq() -> list:
    url = config.WEB_URL + "api/faq?format=json"
    response = requests.get(url=url)
    content = response.json()
    return content