# pull official base image
FROM python:3.10.6-alpine3.16

# set work directory
WORKDIR /usr/src/web

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY web/requirements.txt .
RUN pip install -r requirements.txt
#RUN DJANGO_SUPERUSER_PASSWORD=test python manage.py createsuperuser --noinput test
#RUN python manage.py makemigrations
# copy project
COPY web/web .
