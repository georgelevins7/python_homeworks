from pydantic import BaseModel, EmailStr, Field, model_validator, field_validator
import re
from datetime import datetime

class UserCreate(BaseModel):
    username: str = Field(min_length=5, max_length=20, description="Username must be between 5 and 20 characters.")
    email: EmailStr = Field(description="Valid email address.")
    password: str = Field(min_length=8, max_length=100, description="Password must be between 8 and 100 characters.")
    confirm_password: str = Field(min_length=8, max_length=100, description="Confirm password must match the password.")

    @model_validator(mode="before")
    def validate_passwords(cls, values):
        password = values.get("password")
        confirm_password = values.get("confirm_password")
        if password != confirm_password:
            raise ValueError("Passwords do not match.")
        return values

    @field_validator("password")
    def validate_password_strength(cls, password):
        if not re.search(r"[A-Z]", password):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not re.search(r"[a-z]", password):
            raise ValueError("Password must contain at least one lowercase letter.")
        if not re.search(r"[0-9]", password):
            raise ValueError("Password must contain at least one digit.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValueError("Password must contain at least one special character.")
        return password

    @field_validator("username")
    def validate_username(cls, username):
        if not re.match(r"^[a-zA-Z0-9_]+$", username):
            raise ValueError("Username can only contain letters, numbers, and underscores.")
        return username

class UserLogin(BaseModel):
    username: str = Field(min_length=5, max_length=20, description="Username must be between 5 and 20 characters.")
    password: str = Field(min_length=8, max_length=100, description="Password must be between 8 and 100 characters.")

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True