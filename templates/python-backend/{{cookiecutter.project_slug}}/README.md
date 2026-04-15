# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## 🏗️ Architecture

This project uses **Vertical Slice Architecture** where each feature is self-contained with its own:
- Domain models
- API schemas
- Business logic (services)
- Data access (repositories)
- API endpoints (REST + GraphQL)
- Tests

```
src/
├── features/          # Feature slices
│   ├── health/       # Health check endpoints
│   └── example_todo/ # Example feature (can be deleted)
├── shared/           # Shared infrastructure
└── main.py          # Application entry
```

## 🚀 Quick Start

### Prerequisites

- Python {{ cookiecutter.python_version }}+
- [uv](https://github.com/astral-sh/uv) package manager
- [mise](https://mise.jdx.dev/) (optional, for Python version management)
{% if cookiecutter.include_postgres == 'y' %}- PostgreSQL 14+{% endif %}

### Installation

1. Clone the repository
2. Copy environment variables:
   ```bash
   cp .env.example .env
   ```

3. Install dependencies:
   ```bash
   make install    # Production deps only
   # or
   make dev       # Include dev dependencies
   ```

4. Run the development server:
   ```bash
   make run
   ```

The API will be available at:
- REST API: http://localhost:{{ cookiecutter.port }}
- API Docs: http://localhost:{{ cookiecutter.port }}/docs
- GraphQL: http://localhost:{{ cookiecutter.port }}/graphql (if enabled)

## 📁 Adding New Features

1. Create a new feature folder:
   ```bash
   mkdir -p src/features/my_feature/tests
   ```

2. Add feature components following the pattern in `example_todo/`:
   - `models.py` - Domain models
   - `schemas.py` - Pydantic schemas
   - `repository.py` - Data access
   - `service.py` - Business logic
   - `routes.py` - REST endpoints
   - `graphql.py` - GraphQL resolvers (optional)

3. Register routes in `src/main.py`:
   ```python
   from src.features.my_feature.routes import router as my_feature_router
   app.include_router(my_feature_router, prefix="/api/v1", tags=["my_feature"])
   ```

## 🧪 Testing

```bash
# Run all tests
make test

# Run specific test types
make test-unit
make test-integration

# Run with coverage
make test  # Includes coverage report
```

## 🔧 Development

### Code Quality

```bash
# Format code
make format

# Run linting
make lint

# Install pre-commit hooks
make pre-commit
```

### Database Migrations
{% if cookiecutter.include_postgres == 'y' %}
```bash
# Create a new migration
make db-migrate message="Add user table"

# Apply migrations
make db-upgrade

# Rollback migration
make db-downgrade
```
{% else %}
Database support is not configured. To add PostgreSQL:
1. Set `include_postgres: y` when creating from template
2. Or manually add SQLAlchemy dependencies and configuration
{% endif %}

## 🐳 Docker/OrbStack

Build and run with OrbStack:

```bash
# Build image
make orb-build

# Run container
make orb-run

# View logs
make orb-logs

# Stop container
make orb-stop
```

## 📚 API Documentation

- **Swagger UI**: http://localhost:{{ cookiecutter.port }}/docs
- **ReDoc**: http://localhost:{{ cookiecutter.port }}/redoc
- **OpenAPI JSON**: http://localhost:{{ cookiecutter.port }}/openapi.json

## 🏛️ Project Structure

```
.
├── src/
│   ├── features/         # Feature slices (vertical architecture)
│   │   └── [feature]/
│   │       ├── __init__.py
│   │       ├── models.py      # Domain models
│   │       ├── schemas.py     # API schemas
│   │       ├── repository.py  # Data access
│   │       ├── service.py     # Business logic
│   │       ├── routes.py      # REST endpoints
│   │       ├── graphql.py     # GraphQL (optional)
│   │       └── tests/         # Feature tests
│   ├── shared/           # Shared infrastructure
│   │   ├── config.py     # Settings
│   │   ├── database.py   # DB connection
│   │   ├── middleware.py # Middleware
│   │   └── graphql.py    # GraphQL setup
│   └── main.py          # App entry point
├── tests/               # Global test configuration
├── scripts/             # Utility scripts
├── .claude/             # AI assistant commands
├── Dockerfile           # OrbStack/Docker config
├── Makefile            # Common commands
└── pyproject.toml      # Project dependencies
```

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Run tests and linting
4. Submit a pull request

## 📝 License

[Your License Here]