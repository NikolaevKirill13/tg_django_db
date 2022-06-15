from .models import User
from .auth import chek_authentication
from django.contrib.auth import settings


class TgAuthBackend(object):

    """Аутентификация через Телеграмм"""

    def autentificate(self, request_data):
        try:
            user_id = request_data['id']
            user = User.objects.get(user_id_tg=user_id)
            bot_token = settings.TELEGRAM_BOT_TOKEN
            if chek_authentication(bot_token, request_data):
                return user
            return None
        except User.DoesNotExist:
            return None #  тут надо будет создавать юзверя

    def get_user(self, user_id_tg):
        try:
            return User.objects.get(pk=user_id_tg)
        except User.DoesNotExist:
            return None