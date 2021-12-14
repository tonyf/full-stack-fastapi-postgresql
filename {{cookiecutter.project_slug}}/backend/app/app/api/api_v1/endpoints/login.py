from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app.data import crud, models, schemas
from app.api import deps
from app.core import security
from app.core.config import settings

router = APIRouter()


@router.post("/access-token", response_model=schemas.Token)
async def login_access_token(
    db: Session = Depends(deps.get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    auth = await crud.auth.authenticate(
        db, email=form_data.username, password=form_data.password
    )
    if not auth:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not await crud.user.is_active(auth.user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    return {
        "access_token": security.create_access_token(
            auth.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.post("/test-token", response_model=schemas.User)
async def test_token(
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Test access token
    """
    return current_user


@router.put("/me", response_model=schemas.Auth)
async def update_credentials(
    *,
    db: Session = Depends(deps.get_db),
    email: EmailStr = Body(None),
    password: str = Body(None),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update auth data.
    """
    auth_in = schemas.AuthUpdate()
    if email:
        auth_in.email = email
    if password:
        auth_in.password = password
    auth = await crud.auth.update(db, db_obj=current_user.auth, obj_in=auth_in)
    return auth
