from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, sessionmaker
import os

# Database URL - loaded from environment (via direnv/.envrc or system env)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./vaultnote.db")

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
    if DATABASE_URL.startswith("sqlite")
    else {},
)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Create modern Base class with dataclass features
class Base(DeclarativeBase, MappedAsDataclass):
    pass


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
