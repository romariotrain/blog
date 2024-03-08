from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    is_active = Column(Boolean)


class Teacher(User):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    # Дополнительные поля для учителей


class Student(User):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)