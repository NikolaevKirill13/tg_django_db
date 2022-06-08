from django.urls import path
from .views import callback, redirect, index


urlpatterns = [
    path('tg_login', redirect),
    path('', index),
]
