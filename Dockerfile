FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements-dev.txt /tmp/requirements-dev.txt
COPY ./src/rag /app/src/rag
COPY ./src/rag/.env /app/src/rag/.env
COPY ./tests/rag /app/tests/rag
COPY ./.flake8 /app

WORKDIR /app

EXPOSE 8000

ARG DEV=false

RUN bash src/rag/.env && \
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
    then /py/bin/pip install -r /tmp/requirements-dev.txt ; \
    fi && \
    rm -rf /tmp

ENV PATH="/py/bin:$PATH"