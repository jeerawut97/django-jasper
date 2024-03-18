FROM python:3.9.16-alpine

# Install build dependencies
RUN apk update && \
    apk add --no-cache \
    build-base \
    openjdk11 \
    postgresql-dev \
    tzdata \
    libffi-dev \
    openssl-dev \
    && cp /usr/share/zoneinfo/UTC /etc/localtime && \
    echo "UTC" > /etc/timezone

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk

WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the Django project code
COPY . /app

# Start Gunicorn server
CMD ["gunicorn", "mysite.wsgi", "-b", "0.0.0.0:8000"]
