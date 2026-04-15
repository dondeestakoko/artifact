"""
Script d'entraînement du modèle Iris
Version améliorée avec meilleure évaluation
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, f1_score
import joblib
import json

# Charger les données
print("Chargement des données Iris...")
data = load_iris()
X = data.data
y = data.target

# Diviser en ensemble d'entraînement et de test
print("Division des données en train/test...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner le modèle
print("Entraînement du modèle RandomForest...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Évaluation
print("Évaluation du modèle...")
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

# Afficher les métriques
print("\n=== MÉTRIQUES DU MODELE ===")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"F1-Score:  {f1:.4f}")

# Sauvegarder le modèle
print("\nSauvegarde du modèle...")
joblib.dump(model, "model.pkl")

# Sauvegarder les métriques
metrics = {
    "accuracy": float(accuracy),
    "precision": float(precision),
    "f1_score": float(f1)
}
with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("Modèle sauvegardé dans model.pkl")
print("Métriques sauvegardées dans metrics.json")
