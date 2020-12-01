# pull official base image
FROM python:3.8.3

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_ROOT /srv/www/api
ENV CONFIG_ROOT /config

# set work directory
WORKDIR ${APP_ROOT}

# install dependencies
RUN pip install --upgrade pip
RUN mkdir ${CONFIG_ROOT}
COPY api/requirements.txt ${CONFIG_ROOT}/requirements.txt
RUN pip install -r ${CONFIG_ROOT}/requirements.txt

# Создаем App директорию для приложения
#RUN mkdir ${APP_ROOT}

# Копируем все файлы проекта в эту директорию в Докере
COPY ./api ${APP_ROOT}

ADD . ${APP_ROOT}

