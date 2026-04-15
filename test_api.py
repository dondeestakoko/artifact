"""
Tests simples pour l'API
"""

import pytest
import json
from app import app

@pytest.fixture
def client():
    from fastapi.testclient import TestClient
    return TestClient(app)

def test_root(client):
    """Test l'endpoint racine"""
    response = client.get("/")
    assert response.status_code == 200
    assert "Iris Prediction API" in response.json()["message"]

def test_health(client):
    """Test l'endpoint de santé"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_predict_valid(client):
    """Test une prédiction valide"""
    response = client.post(
        "/predict",
        json={"features": [5.1, 3.5, 1.4, 0.2]}
    )
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert isinstance(data["prediction"], int)
    assert data["prediction"] in [0, 1, 2]

def test_predict_invalid_length(client):
    """Test une prédiction avec un nombre de features invalide"""
    response = client.post(
        "/predict",
        json={"features": [5.1, 3.5, 1.4]}  # Seulement 3 features au lieu de 4
    )
    assert response.status_code == 400
    assert "exactement 4" in response.json()["detail"]

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
