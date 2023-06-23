FROM python:3.10.6

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ENV DJANGO_ALLOWED_HOSTS=*

ENV DEVELOPMENT_MODE=True