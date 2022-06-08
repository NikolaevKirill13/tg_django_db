from django.urls import path
from .views import callback


urlpatterns = [
    path('tg_login', callback),
]
