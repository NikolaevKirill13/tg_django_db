from django.urls import path, re_path
from .views import apiOverview, FaqList, FaqDetail, BlockList, BlockDetail, UserList, UserDetail


urlpatterns = [
    path('', apiOverview),
    path('faq', FaqList.as_view()),
    path('faq/<str:title>', FaqDetail.as_view()),
    path('block', BlockList.as_view()),
    re_path(r'^block/(?P<user>\d+)$', BlockDetail.as_view()),
    path('user', UserList.as_view()),
    re_path(r'^user/(?P<user_id_tg>\d+)$', UserDetail.as_view()),
]
