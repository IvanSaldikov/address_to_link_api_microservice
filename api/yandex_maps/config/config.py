# Параметры конфигурации приложения

from environs import Env

# Инициализация переменной для чтения переменных окружения или файла-.env
env = Env()
env.read_env()

YANDEX_API_KEY = env.str("YANDEX_API_KEY")
DJANGO_SECRET_KEY = env.str("DJANGO_SECRET_KEY")
DJANGO_DEBUG = env.str("DJANGO_DEBUG")