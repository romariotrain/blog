from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None
    priority: int | None = None
    status: str | None = None
    # assigned_to: str | None = None
    # tags: Optional[List[str]] = []
    # attachments: Optional[List[str]] = []
    # progress: Optional[float] = 0.0
    # comments: Optional[List[str]] = []

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    is_complete: bool

    class Config:
        orm_mode = True