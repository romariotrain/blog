from pydantic import BaseModel


class TeacherBase(BaseModel):
    username: str
    email: str


class UserCreate(TeacherBase):
    password: str


class User(TeacherBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True