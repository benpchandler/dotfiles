"""Behavior tests — assert what the endpoints return, not merely that they run."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_ok() -> None:
    resp = client.get("/api/health")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "ok"
    assert body["version"] == "{{ cookiecutter.version }}"


def test_list_items_shape() -> None:
    resp = client.get("/api/items")
    assert resp.status_code == 200
    items = resp.json()
    assert isinstance(items, list)
    assert items[0]["name"] == "example"
    assert items[0]["done"] is False
