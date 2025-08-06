from __future__ import annotations

from sqlalchemy import String, DateTime, Boolean, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import Optional, TYPE_CHECKING
from ..db.base import Base

if TYPE_CHECKING:
    from .note import Note
    from .tag import Tag


class User(Base):
    __tablename__ = "users"

    # Primary key and authentication
    id: Mapped[int] = mapped_column(primary_key=True, index=True, init=False)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))

    # User settings and encryption
    encryption_key_salt: Mapped[str] = mapped_column(
        String(255)
    )  # Salt for deriving user's encryption key
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # Timestamps (auto-generated, not in constructor)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), init=False
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), onupdate=func.now(), init=False, default=None
    )
    last_login: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), init=False, default=None
    )

    # Profile information (optional)
    full_name: Mapped[Optional[str]] = mapped_column(String(100), default=None)
    bio: Mapped[Optional[str]] = mapped_column(Text, default=None)

    # Relationships (not in constructor)
    notes: Mapped[list["Note"]] = relationship(
        "Note", back_populates="owner", cascade="all, delete-orphan", init=False
    )
    tags: Mapped[list["Tag"]] = relationship(
        "Tag", back_populates="owner", cascade="all, delete-orphan", init=False
    )
