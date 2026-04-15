"""Business logic for todo feature."""
from typing import Optional
from uuid import UUID

from fastapi import Depends

from .schemas import TodoCreate, TodoUpdate, TodoResponse, TodoListResponse
from .repository import TodoRepository


class TodoService:
    """Todo service handling business logic."""
    
    def __init__(self, repository: TodoRepository = Depends(TodoRepository)):
        self.repository = repository
    
    async def create(self, todo_data: TodoCreate) -> TodoResponse:
        """Create a new todo."""
        todo = await self.repository.create(todo_data.model_dump())
        return TodoResponse.model_validate(todo)
    
    async def get(self, todo_id: UUID) -> Optional[TodoResponse]:
        """Get a todo by ID."""
        todo = await self.repository.get(todo_id)
        if todo:
            return TodoResponse.model_validate(todo)
        return None
    
    async def list(
        self, 
        page: int = 1, 
        per_page: int = 20,
        completed: Optional[bool] = None
    ) -> TodoListResponse:
        """List todos with pagination."""
        todos, total = await self.repository.list(
            skip=(page - 1) * per_page,
            limit=per_page,
            completed=completed
        )
        
        return TodoListResponse(
            items=[TodoResponse.model_validate(todo) for todo in todos],
            total=total,
            page=page,
            per_page=per_page
        )
    
    async def update(self, todo_id: UUID, todo_update: TodoUpdate) -> Optional[TodoResponse]:
        """Update a todo."""
        # Only include non-None values in update
        update_data = todo_update.model_dump(exclude_unset=True)
        
        todo = await self.repository.update(todo_id, update_data)
        if todo:
            return TodoResponse.model_validate(todo)
        return None
    
    async def delete(self, todo_id: UUID) -> bool:
        """Delete a todo."""
        return await self.repository.delete(todo_id)