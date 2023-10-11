<p align="center">
    <img alt="logo" src="https://github.com/LeChat76/Projet13OC/assets/119883313/9b12a59f-24e7-47bb-b4d2-0d3bf2681cff">
</p>

## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/LeChat76/Projet13OC.git`

#### Créer l'environnement virtuel

- `cd /path/to/Projet13OC`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement:
  - sur linux : `source venv/bin/activate`
  - sur Windows : `.\venv\Scripts\activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel:
  - sur Linux : `which python`
  - sur Windows : `where python`
  le chemin de votre environnement virtuel doit apparaitre dans la liste
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel:
  - sur linux : `which pip`
  - sur Windows : `where pip`
  le chemin de votre environnement virtuel doit apparaitre dans la liste
- Pour désactiver l'environnement:
  - sur Linux : `deactivate`
  - sur Windows : `.\venv\Scripts\deactivate`

#### configurer Sentry

- créer un fichier `.env` à la racine de votre projet (là où se trouve le fichier `manage.py`)
- Créer votre compte sur Sentry [https://sentry.io/welcome/] (vous pouvez utiliser votre compte github ou email)
- cliquer sur le bouton "Start" de l'option "Install Sentry"
- selectionner votre langage de programmation ("Python" dans mon cas) puis cliquer sur "Configure SDK"
- selectionner le framework utilisé (dans mon cas "Django") cliquer sur "Configure SDK"
- recherchez le "dsn" que Sentry a généré puis copiez/collez le dans votre fichier `.env` en l'associant à la variable "SENTRY_DSN"
exemple  de contenu de fichier `.env` : `SENTRY_DSN="https://45f906586c84632cb0451169bf194667@o4506032337125376.ingest.sentry.io/4506032346169344"`

#### Exécuter le site

- `cd /path/to/Projet13OC`
- Activer l'environnement:
  - sur linux : `source venv/bin/activate`
  - sur Windows : `.\venv\Scripts\activate`
- `pip install --r requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Projet13OC`
- Activer l'environnement:
  - sur linux : `source venv/bin/activate`
  - sur Windows : `.\venv\Scripts\activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Projet13OC`
- Activer l'environnement:
  - sur linux : `source venv/bin/activate`
  - sur Windows : `.\venv\Scripts\activate`
- `coverage run -m pytest --nomigrations --disable-warnings`
- `coverage report` pour un rapport CLI ou `coverage html` pour un rapport HTML (`index.html` dans dossier `htmlcov`)

#### Base de données

- `cd /path/to/Projet13OC`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(oc_lettings_site_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from oc_lettings_site_profile where favorite_city like 'B%';`
- `.quit` pour quitter

Si vous souhaitez une interface graphique, je conseil l'utilisation du logiciel gratuit `DB Browser for SQLite` téléchargeable ici [https://sqlitebrowser.org/dl/]

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command python).Path`
