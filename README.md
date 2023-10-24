<p align="center">
    <img alt="logo" src="https://github.com/LeChat76/Projet13OC/assets/119883313/9b12a59f-24e7-47bb-b4d2-0d3bf2681cff">
</p>

## Résumé

- developpement modulaire d'un projet Django
- tests unitaires
- journalisation Sentry
- deploiement d'une image avec Docker
- automatisation des tests et intégration avec CircleCi

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI ou logiciel graphique divers
- Interpréteur Python, version 3.6 ou supérieure (version utilisée 3.11.5)
- Docker desktop

#### Cloner le repository

- `git clone https://github.com/LeChat76/Projet13OC.git`
- `cd Projet13OC`  
- créez un environnement virtuel: `python -m venv .venv`  
- activez l'environnement virtuel:
  - Linux `source .venv/bin/activate`  
  - Windows `.\.venv\Scripts\activate` 
- installez les dépendances: `pip install -r requirements.txt` 
- lancez le serveur django web `python .\manage.py runserver`
- allez sur `http://localhost:8000` depuis votre navigateur internet

#### configurer Sentry

- créez un fichier `.env` à la racine de votre projet (là où se trouve le fichier `manage.py`)
- créez votre compte sur Sentry [https://sentry.io/welcome/] (vous pouvez utiliser votre compte github ou email)
- cliquez sur le bouton "Start" de l'option "Install Sentry"
- selectionnez le langage de programmation "Python" puis cliquez sur "Configure SDK"
- selectionnez le framework "Django" puis cliquez sur "Configure SDK"
- copiez/collez le dsn dans votre fichier `.env` en l'associant à la variable "SENTRY_DSN"
exemple  de contenu de fichier `.env` : `SENTRY_DSN="https://45f906586c84632cb0451169bf194667@o4506032337125376.ingest.sentry.io/4506032346169344"`

#### Linting

- positionnez-vous dans le dossier racine du projet (là ou se trouve le fichier `manage.py`)  
- depuis l'environnement virtuel, executez la commande `flake8`  

#### Tests unitaires

- positionnez-vous dans le dossier racine du projet (là ou se trouve le fichier `manage.py`)   
- depuis l'environnement virtuel, executez les commandes:
  - `coverage run -m pytest --nomigrations --disable-warnings`
  - `coverage report` pour un rapport CLI ou `coverage html` pour un rapport HTML (`index.html` dans dossier `htmlcov`)

#### Base de données

- positionnez-vous dans le dossier racine du projet (là ou se trouve le fichier `manage.py`)
- ouvrez une session shell `sqlite3`
- connectez-vous à la base de données `.open oc-lettings-site.sqlite3`
- Affichez les tables dans la base de données `.tables`
- Affichez les colonnes dans le tableau des profils, `pragma table_info(oc_lettings_site_profile);`
- Lancez une requête sur la table des profils, `select user_id, favorite_city from oc_lettings_site_profile where favorite_city like 'B%';`
- `.quit` pour quitter

Si vous souhaitez une interface graphique, je conseil l'utilisation du logiciel gratuit `DB Browser for SQLite` téléchargeable ici [https://sqlitebrowser.org/dl/]

#### Page d'administration

- Allez sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

#### Docker

- executez l'application `Docker Desktop`
- positionnez-vous dans le dossier racine du projet (là ou se trouve le fichier `manage.py`)
- lancez la commande `docker build -t lechat76/projet13oc:latest .`
- executez localement l'image avec la commande `docker run --rm --name projet13oc -p 8000:8000 lechat76/projet13oc`
- testez à nouveau l'accès à l'application en allant sur `http://localhost:8000` depuis votre navigateur internet
