import hmac
import hashlib


class NotTelegramDataError(Exception):
    """
    Если ошибка данных от телеграм
    """
    pass


def chek_authentication(bot_token, request_data):
    """
    Проверка хеш телеграмм
    """
    request_data = request_data.copy()

    received_hash = request_data['hash']

    request_data.pop('hash', None)
    request_data_alphabetical_order = sorted(request_data.items(), key=lambda x: x[0])

    data_check_string = []

    for data_pair in request_data_alphabetical_order:
        key, value = data_pair[0], data_pair[1]
        data_check_string.append(key + '=' + value)

    data_check_string = '\n'.join(data_check_string)

    secret_key = hashlib.sha256(bot_token.encode()).digest()
    _hash = hmac.new(secret_key, msg=data_check_string.encode(), digestmod=hashlib.sha256).hexdigest()

    if _hash != received_hash:
        raise NotTelegramDataError(
            'Данные не соответствуют'
        )

    return True
