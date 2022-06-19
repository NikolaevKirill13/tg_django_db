from django.urls import path, re_path
from .views import login, auth, IndexView
from django.views.generic import TemplateView


urlpatterns = [
    path('', IndexView.as_view()),
    path('login/', login),
    path('login/auth/', auth),
]
