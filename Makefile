.PHONY: help install train run test docker-build docker-run clean

help:
	@echo "Commandes disponibles:"
	@echo "  make install      - Installer les dépendances"
	@echo "  make train        - Entraîner le modèle"
	@echo "  make run          - Lancer l'API localement"
	@echo "  make test         - Exécuter les tests"
	@echo "  make docker-build - Build l'image Docker"
	@echo "  make docker-run   - Lancer le conteneur Docker"
	@echo "  make docker-compose - Lancer avec docker-compose"
	@echo "  make clean        - Supprimer les fichiers générés"

install:
	pip install -r requirements.txt

train:
	python train.py

run:
	uvicorn app:app --reload

test:
	pytest test_api.py -v

docker-build:
	docker build -t iris-api:latest .

docker-run: docker-build
	docker run -p 8000:8000 iris-api:latest

docker-compose:
	docker-compose up

clean:
	rm -f model.pkl metrics.json
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
