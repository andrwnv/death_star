FROM python:slim-bookworm

COPY requirements.txt requirements.txt

RUN pip3 install --progress-bar off -r requirements.txt
