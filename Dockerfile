FROM python:3.10.4-slim-buster

ENV PYTHONUNBUFFERED=1 ENVIRONMENT=DOCKER PYTHONPATH="${PYTHONPATH}:/app/"

RUN pip install --upgrade pip && pip install --no-cache-dir django coverage tox build twine black isort

WORKDIR /app

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 8001
