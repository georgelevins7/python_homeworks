from pydantic import BaseModel, Field

class SubjectCreate(BaseModel):
    name: str = Field(min_length=2, max_length=30)
    duration: int = Field(gt=0)

class SubjectResponse(BaseModel):
    id: int
    name: str
    duration: int

    class Config:
        from_attributes = True