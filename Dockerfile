# Stage de build de l'application Python
FROM python:3.10-slim AS base
# Adapter le chemin de travail au dossier hôte
WORKDIR /app

# Copier le code
COPY requirements.txt .

# Installer les dépendances\ nCOPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN apt update && apt install netcat-traditional -y

# Copier le code
COPY app/ .
COPY entrypoint.sh /app

# Rendre le script d'entrée exécutable
RUN chmod +x /app/entrypoint.sh

# Entrypoint pour attendre la DB
ENTRYPOINT ["/app/entrypoint.sh"]

# Commande de démarrage par défaut
CMD ["python","/app/main.py"]
