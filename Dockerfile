FROM python:3.6

ENV PYTHONUNBUFFERED=1 ENVIRONMENT=DOCKER

RUN pip install --no-cache-dir django coverage

WORKDIR /app

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 8001
