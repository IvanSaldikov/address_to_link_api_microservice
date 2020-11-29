### Микросервис, преобразующий введенный адрес в ссылку на Яндекс.Карты

Работает на основе Django REST API

Реализация RESTFul API на Django REST Framework: https://www.youtube.com/watch?v=C6S3dMt1s_M

Django Secret Key generator: https://djecrety.ir/

`django-admin startproject api`

`python manage.py migrate`

`settings.py`: `LANGUAGE_CODE = 'ru'`
`TIME_ZONE = 'Europe/Moscow'`
                
`pip install djangorestframework`

    INSTALLED_APPS = [
    
    ...
        
        'rest_framework',
        'yandex_maps',
    ]
                    
`python manage.py startapp yandex_maps`

Делаем модель
```
from django.db import models

# Create your models here.
class YandexMapsQ(models.Model):
    """
    БД запросов к нашему API
    """
    user = models.IntegerField(verbose_name='ID пользователя из БД backend-а',
                                blank=True, null=True)
    tguser = models.IntegerField(verbose_name='ID пользователя из Telegram-а',
                                blank=True, null=True)
    query_str = models.CharField(max_length=500, verbose_name='Введенная строка пользователем. Ожидается - адрес')
    link_to_ya_map = models.TextField(verbose_name='Ссылка на Яндекс.Карты')
    created = models.DateTimeField(auto_now=True, verbose_name='Дата создания/редактирования записи в БД')

    def __str__(self):
        return "%s" % (self.query_str)

    class Meta:
        verbose_name = 'Запроса'
        verbose_name_plural = 'Запросы'
```

Создаем и исполняем миграции: 
`python manage.py makemigrations`
`python manage.py migrate`

Делаем суперпользователя, чтобы можно было просмтривать через админку
`python manage.py createsuperuser`


Делаем сериализатор `serializers.py`:
    ```
    from rest_framework import serializers
    from . import models


    class QueryDetailSerializer(serializers.ModelSerializer):
        """Делаем запрос для добавления запроса в БД"""
        class Meta:
            model = models.YandexMapsQ
            # Поля, доступные для внесения методом POST извне
            fields = ('user', 'tguser', 'query_str', 'link_to_ya_map')

    ```
    
Делаем контроллеры во `views.py`:
    ```
    from rest_framework import generics
    from . import serializers
    from rest_framework.response import Response
    from rest_framework import status
    from yandex_maps.services.yandex import YandexMap
    from yandex_maps.config import config
    
    
    # Возвращаем ссылку на Яндекс-карты из строки адреса или -1, если ничего не найдено
    def get_link(query_str: str) -> str:
        yandex_map = YandexMap(config.YANDEX_API_KEY)
        return yandex_map.get_link(query_str)
    
    
    class CreateQueryView(generics.CreateAPIView):
        """Добавляем запрос в БД"""
        serializer_class = serializers.QueryDetailSerializer
    
        def create(self, request, *args, **kwargs):
            """Переопределяем метод create для того, чтобы просто подменить ссылку для сохранения
            и вернуть только ссылку пользователю"""
            #request.data['link_to_ya_map'] = get_link(request.data['query_str'])
            serializer = self.get_serializer(data=request.data)
            #get_link(request.data['query_str'])
            serializer.is_valid(raise_exception=True)
            link = get_link(request.data['query_str'])
            serializer.validated_data['link_to_ya_map'] = link
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            ret = {
                'status': 'success',
                'link': link
            }
            return Response(ret, status=status.HTTP_201_CREATED, headers=headers)
    ```
    
    
Делаем `urls.py`:
    ```
    from django.contrib import admin
    from django.urls import path, include
    from . import views
    
    
    urlpatterns = [
        path('query/make/', views.CreateQueryView.as_view(), name='index'),
    ]
    ```