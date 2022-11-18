from pydantic import BaseModel, Field


class TimerTime(BaseModel):
    hours: int = Field(ge=0, le=99)
    minutes: int = Field(ge=0, le=59)
    seconds: int = Field(ge=0, le=59)
