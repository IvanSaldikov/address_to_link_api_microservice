from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('yandex_maps.urls')),
]
