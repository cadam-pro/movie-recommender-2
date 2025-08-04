# Utilise une image de base Python complète
FROM python:3.10-slim

# Définit le répertoire de travail
WORKDIR /app

# Installe les dépendances Python
COPY api/requirements.in .
RUN pip install --no-cache-dir -r requirements.in

COPY . .

# ENV PYTHONPATH=/app/src/movie_recommender
# Commande de lancement de l'API (à adapter selon ton app)




CMD ["uvicorn", "api.webapi:mr_api", "--host", "0.0.0.0", "--port", "8000"]