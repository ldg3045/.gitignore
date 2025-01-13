from django.urls import path
from . import views          # 이 곳은 users 앱의 URL 입니다.

app_name = 'users'
urlpatterns = [
    path("", views.users, name="users"),
    path("profile/<str:username>/", views.profile, name="profile"),
]

