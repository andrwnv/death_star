FROM alpine:3.16.0

WORKDIR /app

RUN set -xe;

COPY . .

RUN apk add --no-cache python3 py3-pip; \
    pip install --upgrade pip; \ 
    pip install fastapi uvicorn \
    addgroup -g 1000 appuser; \
    adduser -u 1000 -G appuser -D -h /app appuser; \
    chown -R appuser:appuser /app

USER appuser
EXPOSE 2023/tcp
CMD [ "python3", "main.py" ]
