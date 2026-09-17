import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_ui_endpoint():
    """Test that the root endpoint serves the HTML UI dashboard."""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers.get("content-type", "")
    assert "CI/CD Test App" in response.text
    assert "FastAPI Backend Service" in response.text


def test_healthz_endpoint():
    """Test the health check probe endpoint."""
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_catch_all_single_segment():
    """Test the catch-all route with a simple path."""
    response = client.get("/test-endpoint")
    assert response.status_code == 200
    data = response.json()
    assert data["received_path"] == "test-endpoint"
    assert data["message"] == "Hello from the Python test app"
    assert data["version"] == "1.0.0"


def test_catch_all_nested_segments():
    """Test the catch-all route with nested sub-paths."""
    response = client.get("/api/v1/users/42")
    assert response.status_code == 200
    data = response.json()
    assert data["received_path"] == "api/v1/users/42"
    assert data["message"] == "Hello from the Python test app"
    assert data["version"] == "1.0.0"
