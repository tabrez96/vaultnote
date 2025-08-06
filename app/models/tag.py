from __future__ import annotations

from sqlalchemy import String, DateTime, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import Optional, TYPE_CHECKING
from ..db.base import Base

if TYPE_CHECKING:
    from .user import User
    from .note import Note


class Tag(Base):
    __tablename__ = "tags"

    # Primary key and basic info
    id: Mapped[int] = mapped_column(primary_key=True, index=True, init=False)
    name: Mapped[str] = mapped_column(String(50), index=True)
    description: Mapped[Optional[str]] = mapped_column(Text, default=None)
    color: Mapped[str] = mapped_column(
        String(7), default="#3B82F6"
    )  # Hex color code for tag visualization

    # User ownership
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    # Timestamps (auto-generated, not in constructor)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), init=False
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), onupdate=func.now(), init=False, default=None
    )

    # Relationships (not in constructor)
    owner: Mapped["User"] = relationship("User", back_populates="tags", init=False)
    notes: Mapped[list["Note"]] = relationship(
        "Note", secondary="note_tags", back_populates="tags", init=False
    )
