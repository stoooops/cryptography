FROM python:latest

RUN pip install --upgrade pip setuptools
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt && rm requirements.txt

VOLUME /app
WORKDIR /app
