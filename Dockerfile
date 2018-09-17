FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN apk update \
    && apk add --no-cache --virtual .build-deps \
       postgresql-client \
       postgresql-dev \
       gcc \
       libc-dev \
       jpeg-dev \
       bash \
       zlib-dev \
    && mkdir -p /app/assets \
    && mkdir -p /app/logs \
    && chmod 755 /app \
    && pip install -U pip setuptools \
    && pip install --no-cache-dir -r /app/requirements.txt \
    && rm -rf /var/cache/apk/* \
    && find /usr/local \
       \( -type d -a -name test -o -name tests \) \
       -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
       -exec rm -rf '{}' + \
    && apk add --virtual .rundeps $runDeps

ADD . /app

# Server
EXPOSE 8000
STOPSIGNAL SIGINT

RUN chmod +x /app/docker-entrypoint.sh

ENTRYPOINT ["/app/docker-entrypoint.sh"]
