import requests
from rest_framework.response import Response



def post_user():
    """
    Запрос POST на добавление юзверя в БД.
    """
    url = 'http://127.0.0.1:8000/api/user'
    data = {'username': 'qwe', 'first_name': '', 'last_name': '', 'user_id_tg': '1313', 'warn': '0'}
    send = requests.post(url=url, json=data)
    return send


def post_faq():
    """добавление справки"""
    url = 'http://127.0.0.1:8000/api/faq'
    data = {'title': 'test', 'description': 'test test'}
    send = requests.post(url=url, json=data)
    return send


def post_poll():
    """
    Запрос POST на добавление голосования. Отправляем ид клавиатуры и ид кто проголосовал.
    В ответ придет ид голосования, кто проголосовал и общее количество голосовавших. Повторы не будут учитываться
    Запрос GET вернет все созданные голосования, запрос GET api/poll/id голосования вернет само голосование
    """
    url = 'http://127.0.0.1:8000/api/poll'
    data = {'keyboard_id': '123', 'user_id': '112233'}
    send = requests.post(url=url, json=data)
    return send


def post_block():
    """
    Запрос на добавление юзверя в мут. Нужно только для записи в БД, общей статистики. Добавляет только существующего
    юзверя. Если в ответ на добавление приходит "detail": "Страница не найдена" - то такого юзверя в базе нет
    """
    url = 'http://127.0.0.1:8000/api/block'
    data = {'user': '300', 'permanent': False}
    send = requests.post(url=url, json=data)
    print(send)
    print(Response)
    return send

#post_user()
#post_faq()
post_poll()
#post_block()