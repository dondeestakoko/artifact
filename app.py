from fastapi import FastAPI
import joblib

app = FastAPI()

# Charger le modèle entraîné
model = joblib.load("model.pkl")

@app.get("/")
def root():
    return {"message": "Iris Prediction API", "endpoints": {"/health": "Check API status", "/predict": "Make predictions", "/docs": "API documentation"}}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: list):
    prediction = model.predict([data])
    return {"prediction": prediction.tolist()}