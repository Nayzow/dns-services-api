# Dns-Services-Api

Api Python FastApi pour recenser et géolocaliser de potentiels sites de phishing frauduleux.

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

### Lancer l'API avec Docker

Si vous souhaitez utiliser Docker, voici les étapes pour construire et exécuter ce projet

#### 1. Build l'image Docker

À la racine du projet, exécuter la commande suivante :

```bash
docker build -t dns-services-api .
```

#### 2. Run un conteneur à partir de l'image Docker

```bash
docker run --name dns-services-api -p 8000:8000 -d dns-services-api
```

Après avoir exécuté ces commandes, votre API FastAPI sera disponible à l'adresse http://localhost:8000.
Vous pouvez maintenant utiliser les différentes routes de l'API documentées en dessous.

## Documentation de l'API

L'API expose ces différentes routes :

```
/phishing/{dns} : retourne les sites de phishing associés à un nom de domaine.
```

```
/phishing/hexa/{hexadecimal} : retourne les sites de phishing associés à la représentation hexadécimale d'un nom de domaine.
```

```
/ip/{dns} : retourne l'ip d'un nom de domaine
```

```
/location/{dns} : retourne des informations de géolocalisation d'un nom de domaine
```
