# pull official base image
FROM python:3.8.3

# Создаем пользователя точно такого же, как и на виртуальной машине, чтобы создаваемые файлы были не под root-ом
RUN groupadd --gid 1000 www \
  && useradd --uid 1000 --gid www --shell /bin/bash --create-home www
ARG UID=1000
ARG GID=1000
ENV UID=${UID}
ENV GID=${GID}
RUN usermod -u $UID www \
  && groupmod -g $GID www

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_ROOT /srv/www/api
ENV CONFIG_ROOT /config

# Копируем все файлы проекта в эту директорию в Докере
COPY ./api ${APP_ROOT}

# install dependencies
RUN pip install --upgrade pip
RUN mkdir ${CONFIG_ROOT}
COPY api/requirements.txt ${CONFIG_ROOT}/requirements.txt
RUN pip install -r ${CONFIG_ROOT}/requirements.txt

# set work directory
WORKDIR ${APP_ROOT}

# Collect static files
#RUN python3 manage.py collectstatic --noinput
