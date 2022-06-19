from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from django.views.generic import TemplateView
from .models import User
from .backend import TgAuthUserBackend


bot_name = settings.TELEGRAM_BOT_NAME
bot_token = settings.TELEGRAM_BOT_TOKEN
redirect_url = settings.TELEGRAM_LOGIN_REDIRECT_URL

class IndexView(View):

    @staticmethod
    def get(request):
        context = {
            'hello': 'Здрасте=)'
        }
        template = 'index.html'
        return render(request, template, context)


def login(request):
    """ Страница для размещения всх вариантов входа в систему"""
    return render(request, 'registration/login.html', context={})


class UserDetail(DetailView):
    """Страница профиля пользователя"""
    template_name = 'profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    model = User



def auth(request):
    """
    Функция проверки запроса, отправки данных на авторизацию и перенаправления в профиль
    пользователя
    """
    if not request.GET.get('hash'):
        print('проблема с данными')  # нужно исправить на что-то удобоваримое для юзверей
    else:
        user_id_tg = request.GET.get('id')
        print(user_id_tg)
        user = TgAuthUserBackend.autentificate(request, request)
        return redirect(f'/profile/{user.username}')

