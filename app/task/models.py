from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime, func
from app.database import Base
from sqlalchemy.orm import relationship


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String)
    start_date = Column(DateTime, default=func.now())
    end_date = Column(DateTime, nullable=True)
    priority = Column(Integer, nullable=True)
    status = Column(String, nullable=True)
    # assigned_to = Column(String)  # или ForeignKey, в зависимости от того, как вы храните пользователей
    # tags = Column(String)  # Можно использовать JSON для хранения списка тегов
    # attachments = Column(String)  # Можно использовать JSON для хранения списка файлов
    # progress = Column(Float, default=0.0)
    # comments = Column(String)  # Можно использовать JSON для хранения списка комментариев
    is_complete = Column(Boolean, default=False)
