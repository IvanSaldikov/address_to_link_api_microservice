# Параметры конфигурации приложения

from environs import Env

# Инициализация переменной для чтения переменных окружения или файла-.env
env = Env()
env.read_env()

YANDEX_API_KEY = env.str("YANDEX_API_KEY", '')
DJANGO_SECRET_KEY = env.str("DJANGO_SECRET_KEY", '')
DJANGO_DEBUG = env.bool("DJANGO_DEBUG", False)

# Считываем настройки базы данных
DB_HOST = env.str("DB_HOST", '127.0.0.1')
DB_USER = env.str("DB_USER", '')
DB_PASSWORD = env.str("DB_PASSWORD", '')
DB_NAME = env.str("DB_NAME", '')
DB_PORT = env.str("DB_PORT", 5432)
DB_TYPE = env.int("DB_TYPE", 1)  # Database type: 1 - Postgresql, 0 - SQLite3

ALLOWED_HOST_4=env.str("ALLOWED_HOST_4", '')
CACHE_ENABLED=env.bool("CACHE_ENABLED", False)
EMAIL_HOST=env.str("EMAIL_HOST", '')
EMAIL_PORT=env.str("EMAIL_PORT", '')
EMAIL_HOST_USER=env.str("EMAIL_HOST_USER", '')
EMAIL_HOST_APP_KEY=env.str("EMAIL_HOST_APP_KEY", '')

