from typing import Optional

from pydantic import BaseModel
from pydantic.networks import EmailStr
from app.data.base.schemas import ModelInDBMixin


# Shared properties
class UserBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False


# Properties to receive via API on creation
class UserCreate(UserBase):
    auth_id: int
    first_name: str
    last_name: str


class UserAuthCreate(UserBase):
    email: EmailStr
    password: Optional[str] = None
    first_name: str
    last_name: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase, ModelInDBMixin):
    auth_id: int


# Additional properties to return via API
class User(UserInDBBase):
    email: str


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    pass
