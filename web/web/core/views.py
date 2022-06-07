from django.shortcuts import render
from django.conf import settings
from django_telegram_login.widgets.constants import SMALL, MEDIUM, LARGE, DISABLE_USER_PHOTO
from django_telegram_login.widgets.generator import create_redirect_login_widget, create_callback_login_widget


bot_name = settings.TELEGRAM_BOT_NAME
bot_token = settings.TELEGRAM_BOT_TOKEN
redirect_url = settings.TELEGRAM_LOGIN_REDIRECT_URL

telegram_login_widget = create_redirect_login_widget(redirect_url, bot_name, size=MEDIUM, user_photo=DISABLE_USER_PHOTO)


def telegram_login(request):
    tg_login_widget = create_redirect_login_widget(bot_name, size=MEDIUM)
    context = {'tg_login_widget': tg_login_widget}
    return render(request, 'tg_login.html', context)
