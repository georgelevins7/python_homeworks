from fastapi import APIRouter
from app.models import Subject
from app.database import get_db
from app.schemas.subjects import SubjectCreate, SubjectResponse
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

router = APIRouter(prefix="/subjects")