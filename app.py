from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os

app = FastAPI(
    title="Iris Prediction API",
    description="API pour prédire l'espèce d'iris",
    version="1.0.0"
)

# Charger le modèle entraîné
model_path = "model.pkl"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Le modèle {model_path} n'existe pas. Veuillez d'abord entraîner le modèle avec: python train.py")

model = joblib.load(model_path)

class PredictionInput(BaseModel):
    features: list[float]

class PredictionOutput(BaseModel):
    prediction: int
    confidence: float = None

@app.get("/")
def root():
    return {
        "message": "Iris Prediction API",
        "version": "1.0.0",
        "endpoints": {
            "/health": "Vérifier l'état du service",
            "/predict": "Faire une prédiction (POST)",
            "/docs": "Documentation Swagger"
        }
    }

@app.get("/health")
def health():
    return {"status": "ok", "service": "iris-api"}

@app.post("/predict", response_model=PredictionOutput)
def predict(data: PredictionInput):
    """
    Prédire l'espèce d'iris à partir de 4 caractéristiques.
    
    Entrée : liste de 4 floats [sepal_length, sepal_width, petal_length, petal_width]
    Sortie : prédiction (0=setosa, 1=versicolor, 2=virginica)
    """
    if len(data.features) != 4:
        raise HTTPException(
            status_code=400,
            detail="Les entrées doivent contenir exactement 4 caractéristiques"
        )
    
    try:
        prediction = model.predict([data.features])[0]
        return {"prediction": int(prediction)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la prédiction: {str(e)}")