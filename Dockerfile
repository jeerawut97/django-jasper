FROM python:3.9.16

# Install Java
RUN apt-get update && apt-get install -y openjdk-11-jdk

# Set Java environment variables
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY ./requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the application code
COPY . /app

# Copy Gunicorn configuration file
COPY gunicorn_conf.py /app

# Set the entrypoint to use Gunicorn with the custom configuration
ENTRYPOINT ["gunicorn", "--config", "gunicorn_conf.py", "mysite.wsgi"]
