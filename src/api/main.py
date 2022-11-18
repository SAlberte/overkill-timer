from fastapi import FastAPI
from controllers.timer_controller import TimerController
from models.timer_command import TimerCommand
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
timer_controller = TimerController()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/timer")
def timer(timer_command: TimerCommand):
    timer_controller.handle_timer(timer_command.command)




