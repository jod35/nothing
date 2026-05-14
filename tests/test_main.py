from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_read_item():
    response = client.get("/items/42?q=fastapi")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "fastapi"}