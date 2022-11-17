from pydantic import BaseModel


class TimerCommand(BaseModel):
    command: str
