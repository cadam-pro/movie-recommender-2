FROM python:3.10-slim

WORKDIR /project

RUN apt-get update && apt-get install -y make

COPY keys/kaggle.json /root/.kaggle/kaggle.json
RUN chmod 600 /root/.kaggle/kaggle.json

COPY requirements.in .
RUN pip install --no-cache-dir -r requirements.in

COPY . .

# Exposer le port par défaut de Jupyter
EXPOSE 8888

# Commande pour lancer le notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser"]
