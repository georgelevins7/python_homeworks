from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    is_completed = Column(Boolean, default=False)