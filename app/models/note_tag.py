from sqlalchemy import Table, Column, Integer, ForeignKey
from ..db.base import Base

# Association table for many-to-many relationship between notes and tags
note_tags = Table(
    "note_tags",
    Base.metadata,
    Column("note_id", Integer, ForeignKey("notes.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)
