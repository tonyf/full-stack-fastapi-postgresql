from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import RelationshipProperty, relationship
from sqlalchemy.ext.hybrid import hybrid_property

from app.data.base.model import Base

if TYPE_CHECKING:
    from data.auth.model import Auth  # noqa: F401

    AuthRelationship = RelationshipProperty[Auth]
else:
    AuthRelationship = RelationshipProperty


class User(Base):
    id = Column(Integer, primary_key=True, index=True)

    auth_id = Column(Integer, ForeignKey("auth.id"), nullable=False)
    auth: AuthRelationship = relationship("Auth", uselist=False, back_populates="user")

    # TODO: move to rbac
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

    first_name = Column(String)
    last_name = Column(String)

    @hybrid_property
    def email(self) -> str:
        return self.auth.email
