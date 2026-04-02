import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ---------- UI TESTS ----------

def test_login_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_dashboard_page(client):
    response = client.get("/dashboard")
    assert response.status_code == 200


# ---------- API TESTS ----------

def test_api_home(client):
    response = client.get("/api")
    assert response.status_code == 200
    assert "message" in response.get_json()


def test_add_client(client):
    response = client.post("/api/clients", json={
        "name": "TestUser",
        "age": 25,
        "weight": 70
    })
    assert response.status_code == 200
    assert response.get_json()["message"] == "Client added"


def test_get_clients(client):
    response = client.get("/api/clients")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_get_single_client(client):
    # assuming ID 1 may exist
    response = client.get("/api/clients/1")
    assert response.status_code in [200, 404]


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "OK"
