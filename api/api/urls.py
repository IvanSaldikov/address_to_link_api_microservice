from django.contrib import admin
from django.urls import path, include
from .settings import DEBUG

urlpatterns = [
    path('api/v1/yandex_maps/', include('yandex_maps.urls')),
]

# Добавляем админку только на локальном сервере
if DEBUG:
    urlpatterns.append(path('admin/', admin.site.urls))

