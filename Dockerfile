FROM alpine:3.16.0

WORKDIR /app

RUN set -xe;

COPY . .

RUN apk add --no-cache python3 py3-pip
RUN pip install --upgrade pip
RUN pip install fastapi uvicorn names websockets

EXPOSE 2023/tcp

CMD python3 main.py
