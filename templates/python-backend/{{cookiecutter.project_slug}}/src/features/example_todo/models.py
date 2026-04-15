"""Domain models for the todo feature."""
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

{% if cookiecutter.include_postgres == 'y' %}from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.shared.database import Base


class Todo(Base):
    """Todo database model."""
    
    __tablename__ = "todos"
    
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[Optional[str]] = mapped_column(String(1000), nullable=True)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
{% else %}
from pydantic import BaseModel, Field


class Todo(BaseModel):
    """Todo domain model (in-memory only)."""
    
    id: UUID = Field(default_factory=uuid4)
    title: str = Field(..., max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
{% endif %}