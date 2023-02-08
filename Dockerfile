# Pull base image
FROM python:3.10

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/
COPY . /code/

# Install dependencies
RUN pip install -r requirements.txt

EXPOSE 2023
