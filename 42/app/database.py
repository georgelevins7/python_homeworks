from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

db_url = "postgresql+psycopg2://postgres:1234@localhost:5432/test"
engine = create_engine(db_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()