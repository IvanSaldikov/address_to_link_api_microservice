# Класс для работы с картами Яндекса

import requests


class YandexMap:
    """Класс для работы с Я.Картами"""

    # https://yandex.ru/dev/maps/geocoder/doc/desc/examples/geocoder_examples.html/
    # https://developer.tech.yandex.ru/services/3
    # https://pypi.org/project/yandex-maps/ (только для второй версии Python)

    def __init__(self, yandex_token):
        # Ключ API для Яндекс-карт (JavaScript API и HTTP Геокодер)
        self.YANDEX_API_KEY = yandex_token

    def _get_geocode(self, addr):
        """Метод для получения ширины и долготы по введенному адресу с помощьюч API Яндекс-карт"""
        URL = f"https://geocode-maps.yandex.ru/1.x/?apikey={self.YANDEX_API_KEY}&geocode={addr}&format=json&results=1&lang=ru_RU"
        result = requests.get(URL).json()
        try:
            # return result['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
            # Возвращаем координаты точки адреса, введенного пользователем
            return result['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        except:
            return -1

    def _form_href_to_yamap(self, long, wide):
        """Формируем ссылку на карты для перехода"""
        # https://yandex.ru/blog/mapsapi/18681
        # http://maps.yandex.ru/?ll=30.373136,60.006291&spn=0.067205,0.018782&z=15&l=map,stv,pht
        return f"http://maps.yandex.ru/?ll={long},{wide}&spn=0.067205,0.018782&z=15&l=map,stv&text={wide}%20{long}"

    # Возвращаем ссылку на Яндекс-карты из строки адреса или -1, если ничего не найдено
    def get_link(self, query_str: str) -> str:
        # Нужно подчистить строку запроса, потому что * в телеграм-боте не воспринимается
        address = str(query_str).replace('*', '')
        # Делаем запрос на Яндекс-API, чтобы получить координаты точки по адресу
        yandex_answer = self._get_geocode(address)
        # Если ничего не найдено
        link_to_yamaps = '-1'
        # Если пришел нормальный ответ от API (два числа через пробел)
        if yandex_answer != -1:
            arr = str(yandex_answer).split()
            if len(arr) == 2:
                long = arr[0]
                wide = arr[1]
                # То, создаем ссылку через опять же метод нашего модуля
                link_to_yamaps = self._form_href_to_yamap(long, wide)
        return link_to_yamaps