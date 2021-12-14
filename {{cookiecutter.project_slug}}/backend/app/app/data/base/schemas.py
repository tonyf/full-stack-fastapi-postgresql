import datetime as dt

from typing import Optional
from pydantic import BaseModel


class ModelInDBMixin(BaseModel):
    id: Optional[int] = None
    created_at: Optional[dt.datetime] = None
    updated_at: Optional[dt.datetime] = None

    class Config:
        orm_mode = True


class Pagination(BaseModel):
    prev_page: Optional[int]
    next_page: Optional[int]
    total_pages: int
    count: int
