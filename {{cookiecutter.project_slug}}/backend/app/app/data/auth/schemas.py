from typing import Optional

from pydantic import BaseModel, EmailStr
from app.data.base.schemas import ModelInDBMixin


# Shared properties
class AuthBase(BaseModel):
    email: Optional[EmailStr] = None


# Properties to receive via API on creation
class AuthCreate(AuthBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class AuthUpdate(AuthBase):
    email: Optional[EmailStr] = None
    password: Optional[str] = None


class AuthInDBBase(AuthBase, ModelInDBMixin):
    pass


# Additional properties to return via API
class Auth(AuthInDBBase):
    pass


# Additional properties stored in DB
class AuthInDB(AuthInDBBase):
    pass


class RelatedAuth(AuthInDBBase):
    email: EmailStr
