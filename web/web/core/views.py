from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from .backend import TgAuthUserBackend


bot_name = settings.TELEGRAM_BOT_NAME
bot_token = settings.TELEGRAM_BOT_TOKEN
redirect_url = settings.TELEGRAM_LOGIN_REDIRECT_URL


def login(request):
    print('выходим на редирект')
    return render(request, 'login.html', context={})

def auth(request):
    if not request.GET.get('hash'):
        print('проблема с данными')
    else:
        print('Идем на аутентификацию')
        user_id_tg = request.GET.get('id')
        print(user_id_tg)
        user = TgAuthUserBackend.autentificate(request, request)
        return render(request, 'profile.html', context={'user': request.user, 'user_auth': user})

