from django.urls import path
from . import views             # 이 곳은 articles 앱의 URL 입니다.

app_name = 'articles'
urlpatterns = [
    path("", views.articles, name="articles"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.article_detail, name="article_detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/comments/", views.comment_create, name="comment_create"),
    #
    path("index/", views.index, name="index"),
    #
    path("data-throw/", views.data_throw, name="throw"),
    path("data-catch/", views.data_catch, name="catch"),
]