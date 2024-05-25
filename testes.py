import pytest

from fastapi.testclient import TestClient

from main import app 

client = TestClient(app)


def test_ola_mundo():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Olá": "Mundo"}

def test_ola_mundo_json():
    response = client.get("/")
    assert response.json() == {"Olá":"Mundo"}