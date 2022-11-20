from celery import Celery
from arduino_utils.arduino_controller import ArduinoController
import time
import os

TIMEDATA_URI = os.getenv("TIMEDATA_URI")
ARDUINO_BAUDRATE = os.getenv("ARDUINO_BAUDRATE")
ARDUINO_PORT = os.getenv("ARDUINO_PORT")
ARDUINO_TIMEOUT = os.getenv("ARDUINO_TIMEOUT")
WORKER_NAME = os.getenv("WORKER_NAME")
BROKER_URL_ = os.getenv("BROKER_URL_")

ALL_ENVS: [str]=[TIMEDATA_URI,
          ARDUINO_BAUDRATE,
          ARDUINO_PORT,
          ARDUINO_TIMEOUT,
          WORKER_NAME,
          BROKER_URL_]

print(ALL_ENVS)

if None in ALL_ENVS:
    raise RuntimeError("Some env variables are not defined.")


celery_app = Celery(
    WORKER_NAME,
    broker=BROKER_URL_,
    backend=BROKER_URL_
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
    arduino = ArduinoController(
        baudrate=int(ARDUINO_BAUDRATE),
        port=ARDUINO_PORT,
        timeout=float(ARDUINO_TIMEOUT)
    )
    min_timer_time = 1000
    loop_time = 1
    with open(TIMEDATA_URI, "r+") as f:
        time_ms = int(f.read())
    seconds, minutes, hours = format_time(time_ms)
    arduino.write(f"{hours}:{minutes}:{seconds}\n")
    time.sleep(loop_time)
    while time_ms >= min_timer_time:
        with open(TIMEDATA_URI, "r+") as f:
            time_ms = int(f.read())-min_timer_time
            seconds, minutes, hours = format_time(time_ms)
            f.seek(0)
            arduino.write(f"{hours}:{minutes}:{seconds}\n")
            f.write(str(time_ms))
            f.truncate()
        time.sleep(loop_time)


@celery_app.task
def arduino_set_time_task(hours, minutes, seconds):
    arduino = ArduinoController(
        baudrate=int(ARDUINO_BAUDRATE),
        port=ARDUINO_PORT,
        timeout=float(ARDUINO_TIMEOUT)
    )
    time_ms = int(hours*3.6e6+minutes*60000+seconds*1000)
    with open(TIMEDATA_URI, "w") as f:
        f.write(str(time_ms))
    arduino.write(f"{hours}:{minutes}:{seconds}\n")

