FROM python:3.13-bullseye

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry

COPY ../../ /data/app/
WORKDIR /data/app/

RUN poetry install --no-root --no-interaction