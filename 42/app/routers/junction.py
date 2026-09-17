from fastapi import APIRouter
from app.models import Junction
from app.database import get_db
from app.schemas.junction import JunctionCreate, JunctionResponse
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

router = APIRouter(prefix="/junctions")