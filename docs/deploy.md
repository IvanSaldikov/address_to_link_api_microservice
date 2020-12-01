### Как задеплоить через Docker DJANGO-приложение

https://github.com/wiamsuri/django-gunicorn-nginx-docker

Ready-To-Deploy Django, gunicorn, NGINX, Docker Application

1. На сервере ставим Docker:
    ```
    sudo apt update
    sudo apt install -y docker.io
    sudo usermod -a -G docker $(whoami)
    sudo service docker start
    sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    ```
   
Всю инструкцию по разворачиванию Django-приложения смотрим на сайте:
https://www.haikson.com/programmirovanie/python/django-nginx-gunicorn-postgresql-docker/

