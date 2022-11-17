from fastapi import FastAPI
from src.controllers.timer_controller import TimerController
from src.api.models.timer_command import TimerCommand

app = FastAPI()
timer_controller = TimerController()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/timer")
def timer(timer_command: TimerCommand):
    timer_controller.handle_timer(timer_command.command)




