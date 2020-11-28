### Микросервис, преобразующий введенный адрес в ссылку на Яндекс.Карты

Работает на основе Django REST API

Реализация RESTFul API на Django REST Framework: https://www.youtube.com/watch?v=C6S3dMt1s_M

`django-admin startproject api`

`python manage.py migrate`

`settings.py`: `LANGUAGE_CODE = 'ru'`
`TIME_ZONE = 'Europe/Moscow'`
                
`pip install djangorestframework`

    INSTALLED_APPS = [
    
    ...
        
        'rest_framework',
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


Делаем сериализатор:
    ```python
    from rest_framework import serializers
    from . import models
    
    class QueryDetailSerializer(serializers.ModelSerializer):
        """Делаем запрос для добавления запроса в БД, а заодно используем модуль для извлечения данных по Яндекс.Картам"""
    
        class Meta:
            model = models.YandexMapsQ
            fields = '__all__'
    ```
    
Дополнительные 10 лайфхаков сериализаторов DRF:
https://zen.yandex.ru/media/sonus_space/10-laifhakov-dlia-django-rest-framework-chast-1-5c9fc77b72723e00b331d059
https://zen.yandex.ru/media/sonus_space/10-laifhakov-dlia-django-rest-framework-chast-2-5ca0a25553239a00b3a731a0    