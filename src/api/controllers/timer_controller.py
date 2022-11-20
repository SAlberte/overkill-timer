from celery_worker import arduino_timer_task, arduino_set_time_task
import celery.result
from models.timer_command import Command
from celery import signature


class TimerController:
    def __init__(self):
        self.sig: signature = arduino_timer_task.s()
        self.task: None | celery.result.AsyncResult = None

    def handle_timer(self, command: str):
        if command == Command.STOP.value and self.task is not None:
            self.task.revoke(terminate=True)
        elif command == Command.START.value:
            if self.task is None:
                self.task = self.sig.apply_async()
            elif self.task.status != "PENDING":
                self.task = self.sig.apply_async()

    def set_time(self, hours: int, minutes: int, seconds: int):
        if self.task is not None and self.task.status == "PENDING":
            self.task.revoke(terminate=True)
        arduino_set_time_task.delay(
            hours=hours, minutes=minutes, seconds=seconds
        )
