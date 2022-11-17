from celery import Celery
from src.celery_.arduino.arduino_controller import ArduinoController
import time


celery_app = Celery(
    "celery_worker",
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)


@celery_app.task
def arduino_timer_task():
    arduino = ArduinoController()
    ms_in_sec = 1000
    sec_in_min = 60
    min_in_hour = 60
    min_timer_time = 0
    loop_time = 1
    with open("src/data/time.txt", "r+") as f:
        time_ms = int(f.read())
    while time_ms >= min_timer_time:
        with open("src/data/time.txt", "r+") as f:
            time_ms = int(f.read())
            f.seek(0)
            seconds = int(time_ms//ms_in_sec)
            minutes = int(seconds//sec_in_min)
            hours = int(minutes//min_in_hour)

            seconds %= sec_in_min
            minutes %= min_in_hour
            arduino.write(f"{hours}:{minutes}:{seconds}\n")
            f.write(str(time_ms-ms_in_sec))
            f.truncate()
            time.sleep(loop_time)

