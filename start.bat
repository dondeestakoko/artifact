@echo off
REM Script de démarrage rapide pour Windows
REM Usage: start.bat

echo.
echo 🚀 Démarrage rapide - Iris API MLOps Project
echo ============================================
echo.

REM Vérifier Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python n'est pas installé
    exit /b 1
)

echo ✓ Python trouvé
echo.

REM Créer venv s'il n'existe pas
if not exist "venv" (
    echo 📦 Création de l'environnement virtuel...
    python -m venv venv
)

REM Activer venv
echo 🔌 Activation de venv...
call venv\Scripts\activate.bat

REM Installer dépendances
echo 📚 Installation des dépendances...
pip install -r requirements.txt -q

REM Entraîner le modèle
echo 🤖 Entraînement du modèle...
python train.py

REM Vérifier les fichiers générés
if exist "model.pkl" (
    if exist "metrics.json" (
        echo ✅ Modèle entraîné avec succès!
    ) else (
        echo ❌ Erreur: Fichier metrics.json non trouvé
        exit /b 1
    )
) else (
    echo ❌ Erreur: Fichier model.pkl non trouvé
    exit /b 1
)

echo.
echo ✨ Projet prêt !
echo.
echo Commandes disponibles:
echo   make run         - Lancer l'API
echo   make test        - Exécuter les tests
echo   make docker-run  - Lancer avec Docker
echo   make clean       - Nettoyer les fichiers générés
echo.
