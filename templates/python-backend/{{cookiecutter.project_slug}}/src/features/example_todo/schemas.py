"""Pydantic schemas for todo feature API."""
from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class TodoBase(BaseModel):
    """Base todo schema."""
    
    title: str = Field(..., max_length=200, description="Todo title")
    description: Optional[str] = Field(None, max_length=1000, description="Todo description")
    completed: bool = Field(False, description="Completion status")


class TodoCreate(TodoBase):
    """Schema for creating a todo."""
    pass


class TodoUpdate(BaseModel):
    """Schema for updating a todo."""
    
    title: Optional[str] = Field(None, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    completed: Optional[bool] = None


class TodoResponse(TodoBase):
    """Schema for todo responses."""
    
    id: UUID
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class TodoListResponse(BaseModel):
    """Schema for paginated todo list."""
    
    items: list[TodoResponse]
    total: int
    page: int = 1
    per_page: int = 20