from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas import UserCreate
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService.create(db, user)


@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return UserService.get_all(db)


@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = UserService.get(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = UserService.delete(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted"}