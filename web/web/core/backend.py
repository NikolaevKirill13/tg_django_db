import jwt
from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from rest_framework import authentication, exceptions

from .models import User
from .auth import chek_authentication


class TgAuthUserBackend(object):

    """Аутентификация через Телеграмм"""

    def autentificate(self, request):  # получаем в метод запрос
        request_data = request.GET  # переводим в удобоваримый вид(а надо ли?)
        if chek_authentication(request_data):  # проводим проверку на валидность
            user_id_tg = request.GET.get('id')  # если запрос валиден вытаскиваем id
            username = request.GET.get('username')  # и username  юзера в telegram
            u = User.objects.all()
            for i in u:
                if i.username == username or username is None:
                    first_name = request.GET.get('first_name')  # получаем имя юзера из телеграмм
                    username = str(first_name) + str(user_id_tg)  # собираем вместе с id для уникальности
            user = User.objects.filter(user_id_tg=user_id_tg)  # запрашиваем наличие юзера в БД(почему не работает с get?)
            try:  # если юзер есть
                # user = User.objects.get(user_id_tg=user_id_tg)  # выводим его в переменную
                login(request, user)  # логиним юзера(создаем сессию)
            except ObjectDoesNotExist:  # если юзера нет
                user = User.objects.create_user(  # создаем юзера
                    username=username,
                    password=username,
                    user_id_tg=user_id_tg)
                login(request, user)  # и логиним юзера(создаем сессию)
            return user  # возвращаем юзера
        else:
            return None  # если проверка на валидность не пройдена возвращаем None

    def get_user(self, user_id):  #
        try:  #
            return User.objects.get(pk=user_id)  #
        except ObjectDoesNotExist:  #
            return None  #


class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'

    def authenticate(self, request):
        request.user = None
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()
        if not auth_header:
            return None
        if len(auth_header) == 1:
            return None
        elif len(auth_header) > 2:
            return None

        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() != auth_header_prefix:
            return None
        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except Exception:
            msg = 'Токен не соответствует'
            raise exceptions.AuthenticationFailed(msg)
        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            msg = 'Пользователь не найден'
            raise exceptions.AuthenticationFailed(msg)
        return (user, token)
