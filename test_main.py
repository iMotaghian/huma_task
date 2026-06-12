from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_log_succsec():
    response = client.post(json={"client_id":"client_1","message":"this is test"})
    assert response.status_code == 201
    assert response.json()["status"] == "ok"