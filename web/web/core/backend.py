from .models import User
from .auth import chek_authentication
from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist


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
