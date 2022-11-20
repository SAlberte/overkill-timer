from pydantic import BaseModel
from enum import Enum


class Command(str, Enum):
    STOP = "STOP"
    START = "START"


class TimerCommand(BaseModel):
    command: Command
