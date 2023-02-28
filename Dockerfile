FROM alpine:3.16.0

WORKDIR /app

RUN set -xe;

COPY . .

RUN apk add --no-cache python3 py3-pip; \
    pip install --upgrade pip; \ 
    pip install fastapi uvicorn names websocket

EXPOSE 2023/tcp
CMD python3 main.py
