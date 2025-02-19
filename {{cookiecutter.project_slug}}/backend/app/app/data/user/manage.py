from typing import Optional

from data import crud, schemas
from sqlalchemy.orm import Session
from app.core.security import  verify_password

class ManageUser:
    @staticmethod
    async def create_user(db: Session, obj_in: schemas.UserAuthCreate) -> schemas.User:
        auth = await crud.auth.create(
            db, obj_in=schemas.AuthCreate(email=obj_in.email, password=obj_in.password)
        )
        user = await crud.user.create(
            db,
            obj_in=schemas.UserCreate(
                auth_id=auth.id,
                first_name=obj_in.first_name,
                last_name=obj_in.last_name,
                is_active=obj_in.is_active,
                is_superuser=obj_in.is_superuser,
            ),
        )
        return user

    @staticmethod
    async def authenticate(db: Session, *, email: str, password: str) -> Optional[schemas.User]:
        user = crud.user.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

user = ManageUser()
