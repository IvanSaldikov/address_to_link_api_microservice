from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from .settings import DEBUG
from django.views.static import serve

urlpatterns = [
    path('api/v1/yandex_maps/', include('yandex_maps.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
]

# Добавляем админку только на локальном сервере
if DEBUG:
    urlpatterns.append(path('admin/', admin.site.urls))

