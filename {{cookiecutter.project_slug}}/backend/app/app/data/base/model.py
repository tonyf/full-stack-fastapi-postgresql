from datetime import datetime as dt
from typing import Any

from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    created_at = Column(DateTime, default=dt.now)
    updated_at = Column(DateTime, default=dt.now, onupdate=dt.now)

    # Generate __tablename__ automatically

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
