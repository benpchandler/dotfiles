.PHONY: help install dev run test lint format clean docker-build docker-run

# Default target
.DEFAULT_GOAL := help

# Python interpreter
PYTHON := python{{ cookiecutter.python_version }}
UV := uv

help: ## Show this help message
	@echo "{{ cookiecutter.project_name }} - Available commands:"
	@echo ""
	@awk 'BEGIN {FS = ":.*##"; printf "\033[36m%-20s\033[0m %s\n", "Command", "Description"} /^[a-zA-Z_-]+:.*?##/ { printf "\033[36m%-20s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

install: ## Install production dependencies
	$(UV) sync --frozen

dev: ## Install development dependencies
	$(UV) sync --frozen --all-extras

run: ## Run the development server
	$(UV) run uvicorn src.main:app --reload --host 0.0.0.0 --port {{ cookiecutter.port }}

test: ## Run tests with coverage
	$(UV) run pytest tests/ -v --cov=src --cov-report=term-missing

test-unit: ## Run unit tests only
	$(UV) run pytest tests/unit -v

test-integration: ## Run integration tests only
	$(UV) run pytest tests/integration -v

lint: ## Run linting checks
	$(UV) run ruff check src tests
	$(UV) run mypy src

format: ## Format code with ruff
	$(UV) run ruff format src tests
	$(UV) run ruff check --fix src tests

clean: ## Clean up generated files
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .coverage .pytest_cache .ruff_cache .mypy_cache
	rm -rf dist build *.egg-info

{% if cookiecutter.include_postgres == 'y' %}
# Database commands
db-migrate: ## Create a new database migration
	$(UV) run alembic revision --autogenerate -m "$(message)"

db-upgrade: ## Apply database migrations
	$(UV) run alembic upgrade head

db-downgrade: ## Rollback database migration
	$(UV) run alembic downgrade -1

db-reset: ## Reset database (drop and recreate)
	$(UV) run python -c "from src.shared.database import drop_tables, create_tables; import asyncio; asyncio.run(drop_tables()); asyncio.run(create_tables())"
{% endif %}

# Docker/OrbStack commands
orb-build: ## Build Docker image with OrbStack
	orb build -t {{ cookiecutter.project_slug }}:latest .

orb-run: ## Run container with OrbStack
	orb run -d \
		--name {{ cookiecutter.project_slug }} \
		-p {{ cookiecutter.port }}:{{ cookiecutter.port }} \
		--env-file .env \
		{{ cookiecutter.project_slug }}:latest

orb-stop: ## Stop and remove container
	orb stop {{ cookiecutter.project_slug }} && orb rm {{ cookiecutter.project_slug }}

orb-logs: ## Show container logs
	orb logs -f {{ cookiecutter.project_slug }}

# Pre-commit hooks
pre-commit: ## Install pre-commit hooks
	$(UV) run pre-commit install

pre-commit-run: ## Run pre-commit on all files
	$(UV) run pre-commit run --all-files