FROM python:3.9.0-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY django_aws/django-ecs-terraform/app/requirements.txt .
RUN pip install -r requirements.txt

COPY . .
