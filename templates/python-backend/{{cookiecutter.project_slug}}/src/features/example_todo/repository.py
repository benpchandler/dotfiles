"""Data access layer for todo feature."""
from typing import Optional, List, Tuple, Dict, Any
from uuid import UUID
{% if cookiecutter.include_postgres == 'y' %}from datetime import datetime

from fastapi import Depends
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.shared.database import get_db
from .models import Todo


class TodoRepository:
    """Repository for todo data access."""
    
    def __init__(self, db: AsyncSession = Depends(get_db)):
        self.db = db
    
    async def create(self, todo_data: Dict[str, Any]) -> Todo:
        """Create a new todo in the database."""
        todo = Todo(**todo_data)
        self.db.add(todo)
        await self.db.commit()
        await self.db.refresh(todo)
        return todo
    
    async def get(self, todo_id: UUID) -> Optional[Todo]:
        """Get a todo by ID."""
        result = await self.db.execute(
            select(Todo).where(Todo.id == todo_id)
        )
        return result.scalar_one_or_none()
    
    async def list(
        self,
        skip: int = 0,
        limit: int = 20,
        completed: Optional[bool] = None
    ) -> Tuple[List[Todo], int]:
        """List todos with pagination and filtering."""
        query = select(Todo)
        count_query = select(func.count()).select_from(Todo)
        
        if completed is not None:
            query = query.where(Todo.completed == completed)
            count_query = count_query.where(Todo.completed == completed)
        
        query = query.offset(skip).limit(limit).order_by(Todo.created_at.desc())
        
        result = await self.db.execute(query)
        todos = result.scalars().all()
        
        total_result = await self.db.execute(count_query)
        total = total_result.scalar()
        
        return todos, total
    
    async def update(self, todo_id: UUID, update_data: Dict[str, Any]) -> Optional[Todo]:
        """Update a todo."""
        todo = await self.get(todo_id)
        if not todo:
            return None
        
        for key, value in update_data.items():
            setattr(todo, key, value)
        
        todo.updated_at = datetime.utcnow()
        await self.db.commit()
        await self.db.refresh(todo)
        return todo
    
    async def delete(self, todo_id: UUID) -> bool:
        """Delete a todo."""
        todo = await self.get(todo_id)
        if not todo:
            return False
        
        await self.db.delete(todo)
        await self.db.commit()
        return True
{% else %}from datetime import datetime

from .models import Todo


# In-memory storage for demo purposes
_todos_db: Dict[UUID, Todo] = {}


class TodoRepository:
    """Repository for todo data access (in-memory implementation)."""
    
    async def create(self, todo_data: Dict[str, Any]) -> Todo:
        """Create a new todo in memory."""
        todo = Todo(**todo_data)
        _todos_db[todo.id] = todo
        return todo
    
    async def get(self, todo_id: UUID) -> Optional[Todo]:
        """Get a todo by ID."""
        return _todos_db.get(todo_id)
    
    async def list(
        self,
        skip: int = 0,
        limit: int = 20,
        completed: Optional[bool] = None
    ) -> Tuple[List[Todo], int]:
        """List todos with pagination and filtering."""
        todos = list(_todos_db.values())
        
        if completed is not None:
            todos = [t for t in todos if t.completed == completed]
        
        # Sort by created_at descending
        todos.sort(key=lambda t: t.created_at, reverse=True)
        
        total = len(todos)
        todos = todos[skip:skip + limit]
        
        return todos, total
    
    async def update(self, todo_id: UUID, update_data: Dict[str, Any]) -> Optional[Todo]:
        """Update a todo."""
        todo = _todos_db.get(todo_id)
        if not todo:
            return None
        
        # Update fields
        for key, value in update_data.items():
            setattr(todo, key, value)
        
        todo.updated_at = datetime.utcnow()
        return todo
    
    async def delete(self, todo_id: UUID) -> bool:
        """Delete a todo."""
        if todo_id in _todos_db:
            del _todos_db[todo_id]
            return True
        return False
{% endif %}