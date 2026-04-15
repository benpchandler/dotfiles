"""Unit tests for health check endpoints."""
from fastapi.testclient import TestClient


def test_health_check(client: TestClient):
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert data["service"] == "{{ cookiecutter.project_name }}"


def test_readiness_check(client: TestClient):
    """Test the readiness check endpoint."""
    response = client.get("/ready")
    assert response.status_code == 200
    
    data = response.json()
    assert "api" in data
    assert data["api"] is True
    assert "timestamp" in data
    assert "ready" in data