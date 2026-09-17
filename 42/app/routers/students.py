from fastapi import APIRouter
from app.models import Student
from app.database import get_db
from app.schemas.students import StudentCreate, StudentResponse
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

router = APIRouter(prefix="/students")