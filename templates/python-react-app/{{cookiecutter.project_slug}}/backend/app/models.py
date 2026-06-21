"""Pydantic models — the single source of truth for API shapes.

These models define the OpenAPI schema, which `scripts/dump_openapi.py` emits and
the frontend turns into `src/types/api.generated.ts`. Change a model here and the
type-drift CI check forces the frontend types to be regenerated.
"""

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    version: str


class Item(BaseModel):
    id: int
    name: str
    done: bool = False
