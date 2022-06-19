from django.urls import path, re_path
from .views import login, auth


urlpatterns = [
    path('', login),

    path('auth/', auth)
]
