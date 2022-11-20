from pydantic import BaseModel
from enum import Enum


class Status(str, Enum):
    STOPPED = "STOPPED"
    STARTED = "STARTED"


class TimerStatus(BaseModel):
    status: Status
