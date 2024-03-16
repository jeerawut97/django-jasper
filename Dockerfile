FROM python:3.9.16

RUN apt-get update
RUN apt-get install openjdk-11-jdk -y
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/
RUN apt-get install poppler-utils -y
RUN pip install --upgrade pip

WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
