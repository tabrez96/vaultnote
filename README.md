# VaultNote

A secure, encrypted personal note-taking application built with FastAPI, HTMX, and Alpine.js. VaultNote combines the power of server-side rendering with modern interactivity to create a fast, secure, and user-friendly note-taking experience.

## Features

- 🔐 End-to-end encryption for note content
- 🏷️ Tag-based note organization
- 🔍 Full-text search capabilities
- 🚀 High-performance FastAPI backend
- ⚡ HTMX for seamless server-side interactions
- 🎨 Alpine.js for enhanced client-side interactivity
- 📱 Progressive enhancement for better accessibility
- 🔑 Secure session-based authentication

## Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer and resolver
- [direnv](https://direnv.net/) (optional) - Automatic virtual environment activation

## Quick Start

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd vaultnote
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Unix or MacOS
   # or
   .venv\Scripts\activate  # On Windows
   ```

3. Install dependencies using uv:
   ```bash
   uv pip install -e .
   ```

4. Run the development server:
   ```bash
   cd app
   python main.py
   ```

The application will be available at `http://localhost:8000`.

## Technologies Used

- **Backend**:
  - FastAPI - High-performance web framework
  - SQLAlchemy - Database ORM
  - Jinja2 - Template engine
  - Python-Jose - JWT handling
  - PassLib - Password hashing

- **Frontend**:
  - HTMX - Dynamic HTML updates without JavaScript
  - Alpine.js - Lightweight JavaScript framework
  - Tailwind CSS - Utility-first CSS framework
  - PostCSS - CSS processing

## Project Structure

```
vaultnote/
├── app/
│   ├── static/      # Static assets (CSS, JavaScript)
│   │   ├── css/     # Tailwind CSS and custom styles
│   │   └── js/      # Alpine.js components
│   ├── templates/   # Jinja2 templates
│   │   ├── base/    # Base templates and layouts
│   │   ├── components/ # Reusable UI components
│   │   └── pages/   # Page-specific templates
│   ├── routes/      # FastAPI route handlers
│   ├── db/          # Database models and configuration
│   ├── models/      # Pydantic models
│   ├── schemas/     # SQLAlchemy schemas
│   ├── services/    # Business logic and services
│   └── main.py      # FastAPI application entry point
├── pyproject.toml   # Project dependencies and metadata
├── uv.lock          # Dependency lock file
└── .envrc           # direnv configuration
```

## Development

### Installing Development Dependencies

```bash
uv pip install -e ".[test]"
```

### Running Tests

```bash
pytest
```

### Code Style

This project uses Ruff for code formatting and linting:

```bash
ruff check .    # Lint the code
ruff format .   # Format the code
```

## API Documentation

Once the server is running, you can access:
- OpenAPI documentation at `http://localhost:8000/docs`
- ReDoc alternative documentation at `http://localhost:8000/redoc`

## Configuration

The application can be configured using environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `VAULTNOTE_SECRET_KEY` | JWT secret key | Required |
| `VAULTNOTE_DB_URL` | Database connection URL | `sqlite:///./vaultnote.db` |
| `VAULTNOTE_LOG_LEVEL` | Logging level | `info` |

## Security

- All notes are encrypted using AES-256 before being stored in the database
- Passwords are hashed using bcrypt
- JWT tokens are used for API authentication
- CORS is configured for development but should be restricted in production

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes using Conventional Commits
4. Push to your branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
