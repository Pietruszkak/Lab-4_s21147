# Lab-4_s21147

## Spis treści
- [Klonowanie repozytorium](#klonowanie-repozytorium)
- [Uruchomienie aplikacji lokalnie](#uruchomienie-aplikacji-lokalnie)
- [Uruchomienie aplikacji z wykorzystanie dockera](#uruchomienie-aplikacji-z-wykorzystaniem-dockera)
- [Użycie aplikacji](#użycie-aplikacji)

## Klonowanie repozytorium
#### 1. Zainstaluj git:
[https://git-scm.com/downloads](https://git-scm.com/downloads).
#### 2. Sklonuj repozytorium:
Otwórz terminal (lub Git Bash na Windowsie) i wprowadź poniższą komendę:
```console
git clone https://github.com/Pietruszkak/Lab-4_s21147.git
```
#### 3. Wejdź do katalogu repozytorium:
W terminalu wprowadź:
```console
cd Lab-4_s21147
```
## Uruchomienie aplikacji lokalnie
#### 1. Zainstaluj Pythona
https://www.python.org/downloads/
Aby sprawdzić wersję pythona, otwórz terminal (lub Git Bash na Windowsie) i wprowadź:

```console
python --version
```
lub
```console
python3 --version
```
#### 2. Wejdź do katalogu repozytorium:
Otwórz terminal (lub Git Bash na Windowsie) i wprowadź:
```console
cd Lab-4_s21147
```
#### 3. Zainstaluj zależności:
Wprowadź komendę:
```console
pip install -r requirements.txt
```
#### 4. Uruchom aplikację:
```console
fastapi run pred_app.py
```
## Uruchomienie aplikacji z wykorzystaniem dockera
#### 1. Zainstaluj Dockera
[Docker Desktop: The #1 Containerization Tool for Developers | Docker](https://www.docker.com/products/docker-desktop/)
#### 2. Wejdź do katalogu repozytorium:
Otwórz terminal (lub Git Bash na Windowsie) i wprowadź:
```console
cd Lab-4_s21147
```
#### 3. Budowanie obrazu Docker
W katalogu głównym projektu, w terminalu, uruchom:
```console
docker build -t pred_app .
```
#### 4. Uruchomienie kontenera
Aby uruchomić kontener, użyj:
```console
docker run -p 80:80 pred_app
```
## Uruchomienie aplikacji z wykorzystaniem obrazu z Dockerhuba
#### 1. Zaloguj się do Docker Hub
Użyj poniższej komendy:
```console
docker login
```
#### 2. Pobierz obraz z Docker Hub
```console
docker pull 99051400/pred_app
```
#### 3. Uruchom obraz
```console
docker run -p 80:80 pred_app
```
## Użycie aplikacji
#### 1. Uruchom aplikację za pomocą dockera lub lokalnie
[Opcje](#spis-treści)
#### 2. Zainstaluj Postmana
[Download Postman | Get Started for Free](https://www.postman.com/downloads/)
#### 3. Wysyłanie danych za pomocą Postman:

1.  **Ustaw typ żądania** na **POST**.
2.  Ustaw **URL** na `http://localhost:8000/submit-data`
3.  W sekcji **Body** wybierz opcję **raw** i **JSON**.
4.  Wklej dane JSON do treści żądania.
5.  **Wyślij żądanie**.
#### 4. Dane
Przykładowe dane do wysłania:
```json
{
"gender":  "female",
"ethnicity":  "other",
"fcollege":  false,
"mcollege":  false,
"home":  false,
"urban":  false,
"unemp":  6.199999809265137,
"wage":  8.09000015258789,
"distance":  0.6000000238418579,
"tuition":  0.8891500234603882,
"education":  15,
"income":  "low",
"region":  "other"
}
```
Przykładowe dane w odpowiedzi:
```json
{
"received_data":  [
54.72487094222125
]
}
```