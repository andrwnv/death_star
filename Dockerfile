FROM alpine:3.16.0

RUN set -xe;

WORKDIR /app
COPY . .

RUN apk add --no-cache python3 py3-pip uvicorn fastapi; \
    addgroup -g 1000 appuser; \
    adduser -u 1000 -G appuser -D -h /app appuser; \
    chown -R appuser:appuser /app

USER appuser

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 2023/tcp

CMD [ "python3", "main.py" ]
