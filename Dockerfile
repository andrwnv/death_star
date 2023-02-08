FROM alpine:3.16.0

WORKDIR /app
COPY . .

RUN apk add --no-cache python3 py3-pip tini; \
    pip install --upgrade pip setuptools-scm; \
    python3 setup.py install; \
    python3 martor_demo/manage.py makemigrations; \
    python3 martor_demo/manage.py migrate; \
    addgroup -g 1000 appuser; \
    adduser -u 1000 -G appuser -D -h /app appuser; \
    chown -R appuser:appuser /app

USER appuser

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 2023/tcp

ENTRYPOINT [ "tini", "--" ]
CMD [ "python3", "main.pu" ]
