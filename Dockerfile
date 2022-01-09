FROM python:3.9.9

LABEL maintainer="Geovane Pacheco <geovane.pacheco99@gmail.com>"

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/