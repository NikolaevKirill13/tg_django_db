from django.urls import path
from .views import telegram_login


urlpatterns = [
    path('tg_login', telegram_login),
]