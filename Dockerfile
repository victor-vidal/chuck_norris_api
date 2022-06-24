FROM python:3.8.2-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y build-essential

RUN mkdir /app
EXPOSE 50000
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/