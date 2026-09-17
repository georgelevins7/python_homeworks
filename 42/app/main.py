from app.routers import subjects, students, junction
from fastapi import FastAPI

app = FastAPI(
    title="Student Management API",
    description="A simple API for managing student records",
    version="1.0.0"
)

app.include_router(subjects.router)
app.include_router(students.router)
app.include_router(junction.router)