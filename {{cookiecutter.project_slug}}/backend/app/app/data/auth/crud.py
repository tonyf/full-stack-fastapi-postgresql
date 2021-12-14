from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.data.base.crud import CRUDBase
from app.data.auth.model import Auth
from app.data.auth.schemas import AuthCreate, AuthUpdate


class CRUDAuth(CRUDBase[Auth, AuthCreate, AuthUpdate]):
    async def get_by_email(self, db: Session, *, email: str) -> Optional[Auth]:
        return db.query(Auth).filter(Auth.email == email).first()

    async def create(self, db: Session, *, obj_in: AuthCreate) -> Auth:
        db_obj = Auth(
            email=obj_in.email, hashed_password=get_password_hash(obj_in.password),
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    async def update(
        self, db: Session, *, db_obj: Auth, obj_in: Union[AuthUpdate, Dict[str, Any]]
    ) -> Auth:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return await super().update(db, db_obj=db_obj, obj_in=update_data)


auth = CRUDAuth(Auth)
