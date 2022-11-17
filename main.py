from fastapi import FastAPI
import time
from pydantic import BaseModel
from timer_controller import TimerController


class TimerComand(BaseModel):
    command: str


app = FastAPI()
timer_controller = TimerController()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/timer")
def timer(timer_command: TimerComand):
    timer_controller.handle_timer(timer_command.command)




