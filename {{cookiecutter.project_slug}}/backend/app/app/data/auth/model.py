from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import RelationshipProperty, relationship

from app.data.base.model import Base

if TYPE_CHECKING:
    from app.data.user.model import User  # noqa: F401

    UserRelationship = RelationshipProperty[User]
else:
    UserRelationship = RelationshipProperty


class Auth(Base):
    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String)

    user: UserRelationship = relationship("User", uselist=False, back_populates="auth")
