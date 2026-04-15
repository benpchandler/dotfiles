"""Health check endpoints for monitoring and readiness probes."""
from datetime import datetime
from typing import Dict, Any

from fastapi import APIRouter, Depends
{% if cookiecutter.include_postgres == 'y' %}from sqlalchemy.ext.asyncio import AsyncSession

from src.shared.database import get_db
{% endif %}

router = APIRouter()


@router.get("/health")
async def health_check() -> Dict[str, Any]:
    """Basic health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "{{ cookiecutter.project_name }}",
    }


@router.get("/ready")
async def readiness_check(
    {% if cookiecutter.include_postgres == 'y' %}db: AsyncSession = Depends(get_db){% endif %}
) -> Dict[str, Any]:
    """Readiness check that verifies all dependencies are available."""
    checks = {
        "api": True,
        "timestamp": datetime.utcnow().isoformat(),
    }
    
    {% if cookiecutter.include_postgres == 'y' %}
    # Check database connection
    try:
        await db.execute("SELECT 1")
        checks["database"] = True
    except Exception as e:
        checks["database"] = False
        checks["database_error"] = str(e)
    {% endif %}
    
    # Overall status
    checks["ready"] = all(
        v for k, v in checks.items() 
        if k not in ["timestamp", "ready"] and isinstance(v, bool)
    )
    
    return checks