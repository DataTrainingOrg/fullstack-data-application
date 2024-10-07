from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from models.database import BaseSQL


class Post(BaseSQL):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    title = Column(String)
    description = Column(String)

    user_id = Column(UUID, ForeignKey("users.id"))
    user = relationship("User", back_populates="posts")

    created_at = Column(DateTime())
    updated_at = Column(DateTime())
