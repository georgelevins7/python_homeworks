from pydantic import BaseModel, Field, field_validator

class MovieCreate(BaseModel):
    title: str = Field(min_length=3, max_length=30)
    genre: str = Field(min_length=3, max_length=20)
    year: int = Field(ge=1900, le=2026)
    rating: float = Field(ge=0, le=10)
    description: str | None = None


class MovieUpdate(BaseModel):
    title: str | None = Field(None, min_length=3, max_length=30)
    genre: str | None = Field(None, min_length=3, max_length=20)
    year: int | None = Field(None, ge=1900, le=2026)
    rating: float | None = Field(None, ge=0, le=10)
    description: str | None = None

class MovieResponse(BaseModel):
    id: int
    title: str
    genre: str
    year: int
    rating: float
    description: str | None = None

    class Config:
        from_attributes = True