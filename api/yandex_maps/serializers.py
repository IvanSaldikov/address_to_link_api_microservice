from rest_framework import serializers
from . import models


class QueryDetailSerializer(serializers.ModelSerializer):
    """Делаем запрос для добавления запроса в БД"""
    class Meta:
        model = models.YandexMapsQ
        # Поля, доступные для внесения методом POST извне
        fields = ('user', 'tguser', 'query_str', 'link_to_ya_map')


