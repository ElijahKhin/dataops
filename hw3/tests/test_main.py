from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_happy_path():

    payload = {
        "age": 35,
        "income": 70000,
        "months_on_book": 12,
        "credit_limit": 15000
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert "prediction" in data
    assert "score" in data


def test_predict_bad_input():

    payload = {
        "age": 35,
        "income": "invalid"
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 422
