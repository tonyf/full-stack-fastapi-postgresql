from typing import Optional
from sqlalchemy.orm import Session

from app.data import crud, schemas, models
from app.core.config import settings

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


async def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)
    auth: Optional[models.Auth] = await crud.auth.get_by_email(
        db, email=settings.FIRST_SUPERUSER
    )
    if not auth:
        auth_in = schemas.AuthCreate(
            email=settings.FIRST_SUPERUSER, password=settings.FIRST_SUPERUSER_PASSWORD,
        )
        auth = await crud.auth.create(db, obj_in=auth_in)  # noqa: F841

    user = auth.user
    if not user:
        user_in = schemas.UserCreate(
            auth_id=auth.id,
            first_name=settings.FIRST_SUPERUSER_FIRST_NAME,
            last_name=settings.FIRST_SUPERUSER_LAST_NAME,
            is_superuser=True,
        )
        user = await crud.user.create(db, obj_in=user_in)  # noqa: F841
