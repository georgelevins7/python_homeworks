from fastapi import APIRouter
from app.models import Subject
from app.database import get_db
from app.schemas.subjects import SubjectCreate, SubjectResponse
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

router = APIRouter(prefix="/subjects", tags=["Subjects"])

@router.post("/", response_model=SubjectResponse)
def create_subject(subject: SubjectCreate, db: Session = Depends(get_db)):
    db_subject = Subject(**subject.model_dump())
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

@router.get("/", response_model=list[SubjectResponse])
def all_subjects(db: Session = Depends(get_db)):
    return db.query(Subject).all()

@router.get("/{subject_id}", response_model=SubjectResponse)
def get_subject(subject_id: int, db: Session = Depends(get_db)):
    subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return subject

@router.delete("/{subject_id}", status_code=204)
def delete_subject(subject_id: int, db: Session = Depends(get_db)):
    subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    db.delete(subject)
    db.commit()