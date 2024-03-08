from sqlalchemy import Column, Integer

from app.users.models import User


class Teacher(User):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
