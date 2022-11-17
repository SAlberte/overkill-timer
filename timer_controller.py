from celery_tasks import divide
import celery.result
from enum import Enum


class TimerController:

    def __init__(self):
        self.sig = divide.s(1, 2)
        self.task: None | celery.result.AsyncResult = None

    def handle_timer(self, command: str):
        if command == "STOP" and self.task is not None:
            self.task.revoke(terminate=True)
        elif command == "START":
            if self.task is None:
                self.task = self.sig.apply_async()
            elif self.task.status != "PENDING":
                self.task = self.sig.apply_async()
