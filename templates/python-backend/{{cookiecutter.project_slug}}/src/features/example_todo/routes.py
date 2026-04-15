"""REST API routes for todo feature."""
from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status

from .schemas import TodoCreate, TodoUpdate, TodoResponse, TodoListResponse
from .service import TodoService

router = APIRouter(prefix="/todos")


@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
async def create_todo(
    todo_data: TodoCreate,
    service: TodoService = Depends(TodoService),
) -> TodoResponse:
    """Create a new todo."""
    return await service.create(todo_data)


@router.get("/", response_model=TodoListResponse)
async def list_todos(
    page: int = Query(1, ge=1),
    per_page: int = Query(20, ge=1, le=100),
    completed: Optional[bool] = None,
    service: TodoService = Depends(TodoService),
) -> TodoListResponse:
    """List todos with pagination."""
    return await service.list(page=page, per_page=per_page, completed=completed)


@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo(
    todo_id: UUID,
    service: TodoService = Depends(TodoService),
) -> TodoResponse:
    """Get a specific todo by ID."""
    todo = await service.get(todo_id)
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo {todo_id} not found"
        )
    return todo


@router.patch("/{todo_id}", response_model=TodoResponse)
async def update_todo(
    todo_id: UUID,
    todo_update: TodoUpdate,
    service: TodoService = Depends(TodoService),
) -> TodoResponse:
    """Update a todo."""
    todo = await service.update(todo_id, todo_update)
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo {todo_id} not found"
        )
    return todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(
    todo_id: UUID,
    service: TodoService = Depends(TodoService),
) -> None:
    """Delete a todo."""
    deleted = await service.delete(todo_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo {todo_id} not found"
        )