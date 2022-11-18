FROM python:3.9.7-bullseye

ENV PYTHONUNBUFFERED 1

ARG DEST=/code

RUN mkdir $DEST
WORKDIR $DEST

ARG SRC=./celery_
COPY $SRC/ $DEST/
COPY ./arduino_utils $DEST/arduino_utils

RUN pip install -r $DEST/deployment/requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:${DEST}"
ENTRYPOINT celery -A celery_worker.celery_app worker --loglevel=info
