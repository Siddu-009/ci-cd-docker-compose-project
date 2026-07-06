from sqlalchemy.orm import Session

from app import crud
from app.schemas import UserCreate


class UserService:

    @staticmethod
    def create(db: Session, user: UserCreate):
        return crud.create_user(db, user)

    @staticmethod
    def get_all(db: Session):
        return crud.get_users(db)

    @staticmethod
    def get(db: Session, user_id: int):
        return crud.get_user(db, user_id)

    @staticmethod
    def delete(db: Session, user_id: int):
        return crud.delete_user(db, user_id)