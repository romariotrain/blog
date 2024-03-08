from pydantic import BaseModel


class StudentBase(BaseModel):
    username: str
    email: str


class UserCreate(StudentBase):
    password: str


class User(StudentBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True