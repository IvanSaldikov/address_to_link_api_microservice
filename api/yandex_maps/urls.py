from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('query/make/', views.CreateQueryView.as_view(), name='index'),
    path('query/get_all/', views.QueriesListView.as_view(), name='address_list'),
]
