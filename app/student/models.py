from sqlalchemy import Column, Integer

from app.users.models import User


class Student(User):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)