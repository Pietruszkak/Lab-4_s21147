# bazowy obraz Pythona
FROM python:3.10-slim

# katalog roboczy w kontenerze
WORKDIR /app

# plik requirements.txt do obrazu
COPY requirements.txt .

# zależności
RUN pip install --no-cache-dir -r requirements.txt

# pliki projektu do katalogu roboczego
COPY . .

# port 80 dla FastAPI
EXPOSE 80

# Uruchomienie aplikacji FastAPI
CMD ["fastapi", "run", "pred_app.py", "--host", "0.0.0.0", "--port", "80"]