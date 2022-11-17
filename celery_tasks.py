from celery import Celery
import time

celery_app = Celery(
    "celery_worker",
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)


@celery_app.task
def divide(x, y):
    time.sleep(10)
    return x / y