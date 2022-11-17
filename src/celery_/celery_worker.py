from celery import Celery
from src.celery_.arduino.arduino_controller import ArduinoController
import time


celery_app = Celery(
    "celery_worker",
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)


def format_time(time_ms: int) -> [int, int, int]:
    ms_in_sec = 1000
    sec_in_min = 60
    min_in_hour = 60
    seconds = int(time_ms // ms_in_sec)
    minutes = int(seconds // sec_in_min)
    hours = int(minutes // min_in_hour)

    seconds %= sec_in_min
    minutes %= min_in_hour
    return seconds, minutes, hours


@celery_app.task
def arduino_timer_task():
    arduino = ArduinoController()
    min_timer_time = 1000
    loop_time = 1
    with open("src/data/time.txt", "r+") as f:
        time_ms = int(f.read())
    seconds, minutes, hours = format_time(time_ms)
    arduino.write(f"{hours}:{minutes}:{seconds}\n")
    time.sleep(loop_time)
    while time_ms >= min_timer_time:
        with open("src/data/time.txt", "r+") as f:
            time_ms = int(f.read())-min_timer_time
            seconds, minutes, hours = format_time(time_ms)
            f.seek(0)
            arduino.write(f"{hours}:{minutes}:{seconds}\n")
            f.write(str(time_ms))
            f.truncate()
        time.sleep(loop_time)

