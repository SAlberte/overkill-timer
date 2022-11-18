FROM python:3.10

ENV PYTHONUNBUFFERED 1

ARG DEST=/code

RUN mkdir $DEST
WORKDIR $DEST

ARG SRC=./api
COPY $SRC/ $DEST/

COPY ./arduino_utils/ $DEST/arduino_utils
COPY ./celery_/celery_worker.py $DEST/celery_worker.py

RUN pip install -r $DEST/deployment/requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:${DEST}"

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]