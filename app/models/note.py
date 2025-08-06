from __future__ import annotations

from sqlalchemy import String, DateTime, ForeignKey, Text, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import Optional, TYPE_CHECKING
from ..db.base import Base

if TYPE_CHECKING:
    from .user import User
    from .tag import Tag


class Note(Base):
    __tablename__ = "notes"

    # Primary key and basic info
    id: Mapped[int] = mapped_column(primary_key=True, index=True, init=False)
    title: Mapped[str] = mapped_column(String(200), index=True)

    # Encrypted content fields
    encrypted_content: Mapped[str] = mapped_column(Text)  # Encrypted note content
    content_iv: Mapped[str] = mapped_column(
        String(255)
    )  # Initialization vector for encryption
    content_hash: Mapped[Optional[str]] = mapped_column(
        String(255), default=None
    )  # Hash for integrity verification

    # Search and metadata (stored unencrypted for search capabilities)
    content_preview: Mapped[Optional[str]] = mapped_column(
        Text, default=None
    )  # First 100-200 chars for preview
    word_count: Mapped[int] = mapped_column(default=0)

    # Note settings
    is_pinned: Mapped[bool] = mapped_column(Boolean, default=False)
    is_archived: Mapped[bool] = mapped_column(Boolean, default=False)
    is_favorite: Mapped[bool] = mapped_column(Boolean, default=False)

    # User ownership
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    # Timestamps (auto-generated, not in constructor)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), init=False
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), onupdate=func.now(), init=False, default=None
    )
    last_accessed: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), init=False, default=None
    )

    # Relationships (not in constructor)
    owner: Mapped["User"] = relationship("User", back_populates="notes", init=False)
    tags: Mapped[list["Tag"]] = relationship(
        "Tag", secondary="note_tags", back_populates="notes", init=False
    )
