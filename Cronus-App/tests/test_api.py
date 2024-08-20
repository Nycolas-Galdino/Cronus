from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.api.endpoints import router

app = FastAPI()
app.include_router(router)

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bem-vindo ao Cronus API"}
