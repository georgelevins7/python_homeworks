from app.database import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Subject(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)
    duration: Mapped[int] = mapped_column(Integer, nullable=False)

    junctions: Mapped[list["Junction"]] = relationship("Junction", back_populates="subject", cascade="all, delete-orphan") # type: ignore

def __str__(self) -> str:
    return self.name