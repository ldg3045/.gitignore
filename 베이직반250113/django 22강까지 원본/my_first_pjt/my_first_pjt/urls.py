""" 원본
URL configuration for my_first_pjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

""" 번역
    my_first_pjt 프로젝트의 URL 설정

urlpatterns 리스트는 URL들을 뷰로 라우팅합니다. 자세한 정보는 다음을 참고하세요:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/

예시들:
함수 기반 뷰
    1. 뷰를 임포트하기: from my_app import views
    2. urlpatterns에 URL 추가하기: path('', views.home, name='home')
클래스 기반 뷰
    1. 뷰를 임포트하기: from other_app.views import Home
    2. urlpatterns에 URL 추가하기: path('', Home.as_view(), name='home')
다른 URL 설정 포함하기
    1. include 함수 임포트하기: from django.urls import include, path
    2. urlpatterns에 URL 추가하기: path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/", views.index, name="index"),
    path("articles/", include("articles.urls")),
    path("users/", include("users.urls")),
    path("accounts/", include("accounts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
