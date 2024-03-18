FROM python:3.9.16

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update
RUN apt-get install openjdk-11-jdk -y
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/

RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "gunicorn", "core.wsgi", "-b", "0.0.0.0:8000"]
