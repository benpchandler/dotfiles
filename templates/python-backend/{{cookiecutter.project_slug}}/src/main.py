"""{{ cookiecutter.project_name }} - Main application entry point."""
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.shared.config import settings
from src.shared.middleware import setup_middleware
{% if cookiecutter.include_postgres == 'y' %}from src.shared.database import create_tables{% endif %}

# Import feature routers
from src.features.health.routes import router as health_router
from src.features.example_todo.routes import router as todo_router

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events."""
    logger.info("Starting {{ cookiecutter.project_name }}...")
    {% if cookiecutter.include_postgres == 'y' %}
    # Create database tables
    await create_tables()
    {% endif %}
    yield
    logger.info("Shutting down {{ cookiecutter.project_name }}...")


# Create FastAPI app
app = FastAPI(
    title="{{ cookiecutter.project_name }}",
    description="{{ cookiecutter.project_description }}",
    version="0.1.0",
    lifespan=lifespan,
)

# Setup middleware
setup_middleware(app)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include feature routers
app.include_router(health_router, tags=["health"])
app.include_router(todo_router, prefix="/api/v1", tags=["todos"])

# GraphQL support (optional)
if settings.ENABLE_GRAPHQL:
    from src.shared.graphql import graphql_app
    app.mount("/graphql", graphql_app)


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Welcome to {{ cookiecutter.project_name }}",
        "docs": "/docs",
        "health": "/health",
    }