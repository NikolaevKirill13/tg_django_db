from .models import User
from .auth import chek_authentication
from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist


class TgAuthUserBackend(object):

    """Аутентификация через Телеграмм"""

    def autentificate(self, request):
        request_data = request.GET
        if chek_authentication(request_data):
            user_id_tg = request.GET.get('id')
            username = request.GET.get('username')
            if username is None:
                first_name = request.GET.get('first_name')
                username = str(first_name) + str(user_id_tg)
                print(username)
            User.objects.filter(user_id_tg=user_id_tg)
            try:
                user = User.objects.get(user_id_tg=user_id_tg)
                login(request, user)
            except ObjectDoesNotExist:
                user = User.objects.create_user(username=username, password=username, user_id_tg=user_id_tg)
                print(user)
                user = User.objects.get(username=user.username)
                login(request, user)
            return user
        else:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return None
