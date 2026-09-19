from fastapi import APIRouter
from app.models import Junction
from app.database import get_db
from app.schemas.junction import JunctionResponse
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from app.schemas.students import StudentResponse
from app.schemas.subjects import SubjectResponse

router = APIRouter(tags=["Junctions"])

@router.post("/students/{student_id}/subjects/{subject_id}", response_model=JunctionResponse)
def create_junction(student_id: int, subject_id: int, db: Session = Depends(get_db)):
    existing_junction = db.query(Junction).filter(Junction.student_id == student_id, Junction.subject_id == subject_id).first()
    if existing_junction:
        raise HTTPException(status_code=400, detail="Junction already exists")
    junction = Junction(student_id=student_id, subject_id=subject_id)
    db.add(junction)
    db.commit()
    db.refresh(junction)
    return junction

@router.get("/students/{student_id}/subjects", response_model=list[SubjectResponse])
def get_subjects_for_student(student_id: int, db: Session = Depends(get_db)):
    junctions = db.query(Junction).filter(Junction.student_id == student_id).all()
    if not junctions:
        raise HTTPException(status_code=404, detail="No subjects found for this student")
    return [junction.subject for junction in junctions]

@router.get("/subjects/{subject_id}/students", response_model=list[StudentResponse])
def get_students_for_subject(subject_id: int, db: Session = Depends(get_db)):
    junctions = db.query(Junction).filter(Junction.subject_id == subject_id).all()
    if not junctions:
        raise HTTPException(status_code=404, detail="No students found for this subject")
    return [junction.student for junction in junctions]

@router.delete("/students/{student_id}/subjects/{subject_id}", status_code=status.HTTP_204_NO_CONTENT)
def student_delete_from_subject(student_id: int, subject_id: int, db: Session = Depends(get_db)):
    junction = db.query(Junction).filter(Junction.student_id == student_id, Junction.subject_id == subject_id).first()
    if not junction:
        raise HTTPException(status_code=404, detail="Junction not found")
    db.delete(junction)
    db.commit()
