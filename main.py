from typing import Union

from fastapi import FastAPI
from app.users.routers import router as user_router
from app.task.routers import router as task_router

app = FastAPI()


app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(task_router, prefix="/task", tags=["task"])
