from pydantic import BaseModel, Field
from datetime import datetime

class JunctionCreate(BaseModel):
    student_id: int = Field(gt=0)
    subject_id: int = Field(gt=0)

class JunctionResponse(BaseModel):
    id: int
    student_id: int
    subject_id: int
    created_at: datetime

    class Config:
        from_attributes = True