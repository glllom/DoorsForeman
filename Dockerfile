
FROM python:3.11-alpine

COPY ./requirements.txt /temp/requirements.txt
COPY . /doors_foreman

WORKDIR /doors_foreman

EXPOSE 8000

RUN pip install -r /temp/requirements.txt
RUN adduser --disabled-password service-user

USER service-user