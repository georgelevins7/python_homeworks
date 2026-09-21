from fastapi import APIRouter, Depends, HTTPException, status
from app.models.users import User
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas.users import UserCreate, UserLogin, UserResponse
from app.security import hash_password, verify_password

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter((User.username == user.username) | (User.email == user.email)).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username or email already exists")

    hashed_password = hash_password(user.password)
    db_user = user.model_dump(exclude={"password", "confirm_password"})
    new_user = User(**db_user, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    authorized_user = db.query(User).filter(User.username == user.username).first()
    if not authorized_user or not verify_password(user.password, authorized_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    return "User logged in successfully"