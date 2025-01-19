from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rooms/', include('rooms.urls')),  # rooms 앱의 URL 연결
] 