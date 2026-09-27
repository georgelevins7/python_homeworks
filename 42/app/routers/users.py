from fastapi import APIRouter, Depends, HTTPException, status
from app.models.users import User
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas.users import UserCreate, UserLogin, UserResponse, UserUpdate
from app.security import create_access_token, hash_password, refresh_access_token, require_admin, verify_password, get_current_user

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

    access_token = create_access_token(data={"user_id": authorized_user.id})
    refresh_token = refresh_access_token(data={"user_id": authorized_user.id})
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"

    }

@router.get("/me", response_model=UserResponse)
def get_user_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db), current_user: User = Depends(require_admin)):
    users = db.query(User).all()
    return users

@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(require_admin)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(require_admin)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(user)
    db.commit()
    return {"detail": f"User {user_id} deleted successfully"}

@router.patch("/me", response_model=UserResponse)
def update_current_user(user_update: UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user_data = user_update.model_dump(exclude_unset=True)
    if "username" in user_data:
        existing_user = db.query(User).filter(User.username == user_data["username"]).first()
        if existing_user and existing_user.id != current_user.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already taken")

    if "email" in user_data:
        existing_user = db.query(User).filter(User.email == user_data["email"]).first()
        if existing_user and existing_user.id != current_user.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already taken")
    if "password" in user_data:
        user_data["password"] = hash_password(user_data["password"])
    user_data.pop("confirm_password", None)
    for key, value in user_data.items():
        setattr(current_user, key, value)
    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return current_user
