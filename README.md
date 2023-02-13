# Dns-Services-Api

Api Python FastApi pour recenser et géolocaliser de potentiels sites de phishing frauduleux.

- Lien de l'application web frontend pour cette API : https://github.com/Nayzow/DNS-Services-Frontend

- Lien de la documentation complète du projet : https://github.com/Nayzow/Domain-sh


### 1. Cloner le dépôt

```bash
git clone https://github.com/Nayzow/Dns-Services-Api
```

### 2. Lancer l'API

Vous pouvez choisir de lancer l'api sur votre machine avec uvicorn ou sinon vous pouvez le faire avec Docker. Les 2 procédures d'installation sont détaillées en dessous.

### Lancer l'API avec Uvicorn

À la racine du projet, exécuter les commandes suivantes :

```bash
pip install -r requirements.txt
```

```bash
uvicorn app.main:app
```
Après avoir exécuté ces commandes, votre API FastAPI sera disponible à l'adresse http://localhost:8000.

### Lancer l'API avec Docker

Si vous souhaitez utiliser Docker, voici les étapes pour construire et exécuter ce projet

#### 1. Build l'image Docker

À la racine du projet, exécuter la commande suivante :

```bash
docker build -t dns-services-api .
```

#### 2. Run un conteneur à partir de l'image Docker

```bash
docker run --name dns-services-api -p 8888:8888 -d dns-services-api
```

Après avoir exécuté ces commandes, votre API FastAPI sera disponible à l'adresse http://localhost:8888.
Vous pouvez maintenant utiliser les différentes routes de l'API documentées ci-dessous.

## Documentation de l'API

L'API expose ces différentes routes :

### GET

#### Les deux principales routes, notamment utilisées pour l'application web.

```
/api/domains/{domain} : retourne les potentiels sites de phishing associés à un nom de domaine.
```

```
/api/domain/{domain} : retourne les information relatives à un nom de domaine.
```

#### Réponse de la requête pour récupérer la data sur un domaine

```json
{
  "name": "google.fr",
  "ip": "142.250.201.163",
  "available": false,
  "location": {
    "continent": "North America",
    "country": "United States",
    "regionName": "Colorado",
    "city": "Arvada",
    "zip": "80004",
    "lat": 39.8147,
    "lon": -105.1168,
    "timezone": "America/Denver",
    "currency": "USD",
    "isp": "Google LLC",
    "org": "Google LLC",
    "reverse": "par10s41-in-f3.1e100.net",
    "mobile": false,
    "proxy": false,
    "hosting": true,
    "query": "142.250.75.227"
  }
}
```

#### Autres routes utiles

```
/api/ip/{domain} : retourne l'ip d'un nom de domaine.
```

```
/api/location/{domain} : retourne des informations de géolocalisation d'un nom de domaine
```

```
/api/available/{domain} : retourne true si le domaine est disponible à l'achat, false si il ne l'est pas.
```
