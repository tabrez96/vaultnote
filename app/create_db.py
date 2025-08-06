#!/usr/bin/env python3
"""
Database initialization script for VaultNote.
Run this script to create database tables.
"""

import sys
from pathlib import Path

# Add the app directory to Python path
app_dir = Path(__file__).parent
sys.path.insert(0, str(app_dir))

from db.init_db import create_tables, drop_tables, reset_database  # noqa: E402


def main():
    import argparse

    parser = argparse.ArgumentParser(description="VaultNote Database Management")
    parser.add_argument(
        "action", choices=["create", "drop", "reset"], help="Database action to perform"
    )

    args = parser.parse_args()

    if args.action == "create":
        create_tables()
    elif args.action == "drop":
        drop_tables()
    elif args.action == "reset":
        reset_database()


if __name__ == "__main__":
    main()
