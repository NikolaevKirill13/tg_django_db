from django.urls import path, re_path
from .views import login, auth
from django.views.generic import TemplateView


urlpatterns = [
    path('', login),
    path('auth/', auth),
]
