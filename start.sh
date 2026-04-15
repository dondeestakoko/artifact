#!/bin/bash
# Script de démarrage rapide du projet
# Usage: bash start.sh

echo "🚀 Démarrage rapide - Iris API MLOps Project"
echo "============================================"

# Vérifier Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé"
    exit 1
fi

echo "✓ Python trouvé"

# Créer venv s'il n'existe pas
if [ ! -d "venv" ]; then
    echo "📦 Création de l'environnement virtuel..."
    python3 -m venv venv
fi

# Activer venv
echo "🔌 Activation de venv..."
source venv/bin/activate

# Installer dépendances
echo "📚 Installation des dépendances..."
pip install -r requirements.txt -q

# Entraîner le modèle
echo "🤖 Entraînement du modèle..."
python train.py

# Vérifier les fichiers générés
if [ -f "model.pkl" ] && [ -f "metrics.json" ]; then
    echo "✅ Modèle entraîné avec succès!"
else
    echo "❌ Erreur: Fichiers model.pkl ou metrics.json non trouvés"
    exit 1
fi

echo ""
echo "✨ Projet prêt !"
echo ""
echo "Commandes disponibles:"
echo "  make run         - Lancer l'API"
echo "  make test        - Exécuter les tests"
echo "  make docker-run  - Lancer avec Docker"
echo "  make clean       - Nettoyer les fichiers générés"
