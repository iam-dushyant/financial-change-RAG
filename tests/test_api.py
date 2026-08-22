import os
os.environ["MOCK_LLM"] = "true"
from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_health():
    assert client.get("/health").json() == {"status": "healthy"}

def test_ask_returns_sources():
    r = client.post("/ask", json={"question": "Can I deploy a payment schema change in peak hours without rollback?"})
    assert r.status_code == 200
    body = r.json()
    assert body["answer"]
    assert len(body["sources"]) == 2