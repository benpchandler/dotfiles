"""{{ cookiecutter.project_name }} — FastAPI application."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.models import HealthResponse, Item

app = FastAPI(
    title="{{ cookiecutter.project_name }}",
    description="{{ cookiecutter.description }}",
    version="{{ cookiecutter.version }}",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
async def health() -> HealthResponse:
    """Liveness probe."""
    return HealthResponse(status="ok", version="{{ cookiecutter.version }}")


@app.get("/api/items")
async def list_items() -> list[Item]:
    """Example typed endpoint — drives the OpenAPI schema the frontend types derive from."""
    return [Item(id=1, name="example", done=False)]
