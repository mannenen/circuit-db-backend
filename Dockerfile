FROM python:3-alpine

ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk add --no-cache build-base

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY pytest.ini /app/tests/pytest.ini

WORKDIR /app/src
CMD uvicorn --host 0.0.0.0 --port 5000 --access-log --reload backend.main:app --log-level debug