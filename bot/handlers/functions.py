from time import time
import requests


def get_warns(user_id):
    url = "127.0.0.1"#add port and test this function need a test server
    params = [user_id]
    return requests.get(url=url,params=params)


def mute_time(user_id):
    warns = get_warns(user_id=user_id)
    _time = time() + warns * 600 + (warns - 1) * 600
    return _time
