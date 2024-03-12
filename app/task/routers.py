from datetime import datetime
import uuid
from app.task import schema, models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from ..database import get_db
# from app.oauth2 import require_user

router = APIRouter()

@router.get("/tasks/{task_id}")
def read_task(task_id: int):
    return {"task_id": task_id}


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schema.TaskBase)
def create_post(task: schema.TaskCreate, db: Session = Depends(get_db)):
    new_post = models.Task(**task.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post