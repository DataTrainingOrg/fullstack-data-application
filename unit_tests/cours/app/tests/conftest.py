# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_read_item():
    response = client.get("/items/42", params={"q": "example"})
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "example"}
