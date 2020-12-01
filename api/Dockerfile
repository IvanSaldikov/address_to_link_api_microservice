# pull official base image
FROM python:3.8.3


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


ENV APP_ROOT /src
ENV CONFIG_ROOT /config

# install dependencies
RUN pip install --upgrade pip
RUN mkdir ${CONFIG_ROOT}
COPY requirements.txt ${CONFIG_ROOT}/requirements.txt
RUN pip install -r ${CONFIG_ROOT}/requirements.txt

RUN mkdir ${APP_ROOT}

# set work directory
WORKDIR ${APP_ROOT}

ADD . ${APP_ROOT}