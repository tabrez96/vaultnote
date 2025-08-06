from .base import Base, engine


def create_tables():
    """Create all tables in the database."""
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")


def drop_tables():
    """Drop all tables from the database."""
    Base.metadata.drop_all(bind=engine)
    print("Database tables dropped successfully!")


def reset_database():
    """Drop and recreate all tables."""
    drop_tables()
    create_tables()
    print("Database reset complete!")


# To run this, use: python -m db.init_db from the app directory
# Or import and call the functions from another module
