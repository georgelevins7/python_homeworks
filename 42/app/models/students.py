from app.database import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(40), unique=True)

    junctions: Mapped[list["Junction"]] = relationship("Junction", back_populates="student", cascade="all, delete-orphan") # type: ignore

def __str__(self) -> str:
    return self.first_name + " " + self.last_name