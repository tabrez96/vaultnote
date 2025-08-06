# Claude Development Notes

This file contains project-specific information and preferences for Claude Code to ensure consistent development practices.

## Commit Message Preferences

- **Do NOT include** "Co-Authored-By: Claude" in commit messages
- **Do include** the Claude Code generation line: `🤖 Generated with [Claude Code](https://claude.ai/code)`
- Use conventional commit format: `feat:`, `fix:`, `refactor:`, etc.

## Project Context

**VaultNote** - A secure, encrypted personal note-taking application built with FastAPI, HTMX, and Alpine.js.

### Technology Stack
- **Backend**: FastAPI, SQLAlchemy 2.0, Python 3.11+
- **Database**: SQLite (development), supports PostgreSQL/MySQL
- **Frontend**: HTMX, Alpine.js, Tailwind CSS
- **Environment**: direnv for automatic environment loading
- **Code Quality**: ruff for linting and formatting, pre-commit hooks

### Database Models
- **User**: Authentication, encryption keys, user settings
- **Note**: Encrypted content with metadata, belongs to User
- **Tag**: Organization labels, belongs to User
- **Note-Tag**: Many-to-many relationship via association table

### Development Practices
- Use modern SQLAlchemy 2.0 syntax with `DeclarativeBase` and `MappedAsDataclass`
- Type hints with `Mapped[T]` and proper forward references using `TYPE_CHECKING`
- Environment configuration via `.env` files and direnv
- Database initialization via CLI script (`create_db.py`)

### Key Features
- End-to-end encryption for note content
- Tag-based organization system
- Full-text search capabilities
- Progressive enhancement for accessibility
- Session-based authentication

## Development Commands

```bash
# Environment setup
direnv allow                    # Enable automatic environment loading

# Database management
python create_db.py create      # Create database tables
python create_db.py reset       # Reset database (drop and recreate)

# Development server
cd app && python main.py        # Run FastAPI development server
```

## Code Style Notes
- No unnecessary code comments unless explicitly requested
- Follow existing patterns and conventions
- Use absolute imports where possible
- Prefer editing existing files over creating new ones
- Keep responses concise and direct