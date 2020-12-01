from rest_framework import generics
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from .services.yandex import YandexMap

# Параметры конфигурации приложения
from environs import Env
# Инициализация переменной для чтения переменных окружения или файла-.env
env = Env()
env.read_env()


# Возвращаем ссылку на Яндекс-карты из строки адреса или -1, если ничего не найдено
def get_link(query_str: str) -> str:
    yandex_map = YandexMap(env.str("YANDEX_API_KEY", ''))
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

