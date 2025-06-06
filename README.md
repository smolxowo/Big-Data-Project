# 🚀 Big Data Project – Airflow + PySpark + DataLake

Pipeline de traitement de données automatisé et modulaire utilisant Apache Airflow, PySpark, API REST et DataLake.

---

## 📁 Prérequis

- Système Linux, macOS ou Windows avec WSL
- Python 3.7+
- pip
- git
- Compte Kaggle avec clé API (`kaggle.json`)

Pour Windows, installer WSL : [Installation WSL](https://learn.microsoft.com/fr-fr/windows/wsl/install)

---

## 🧱 Installation

### 1. Cloner le dépôt

`git clone https://github.com/Booboo123478/Big-Data-Project.git`  
`cd Big-Data-Project`

### 2. Installer les dépendances du projet (Dans le projet)

`pip install -r requirements.txt`

### 3. Chemin classic (Dans WSL) (à redéfinir à votre cas)

`cd /mnt/c/Users/<TON_USER>/OneDrive/Documents/GitHub/Big-Data-Project`

### 4. Installer python3-venv (DANS WSL à faire une fois)

`sudo apt update`  
`sudo apt install python3-venv`

### 5. Créer un environnement virtuel Python (DANS WSL à faire une fois)

`python3 -m venv airflow_venv`

### 6. Activer un environnement virtuel Python (DANS WSL)

`source airflow_venv/bin/activate`

### 7. Installer Apache Airflow (version 2.9.0 avec Celery) (DANS WSL à faire une fois)

Récupérer la version de Python :  
`PYTHON_VERSION=$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)`  
Puis installer Airflow avec la contrainte correspondante :  
`pip install "apache-airflow[celery]==2.9.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.0/constraints-$PYTHON_VERSION.txt"`

### 8. Définir le dossier des DAGs (Dans le cas où tu as déjà définis des DAGs ailleurs)

`export AIRFLOW__CORE__DAGS_FOLDER=/mnt/c/Users/<TON_USER>/OneDrive/Documents/GitHub/Big-Data-Project/dags`

#### Ou

`nano ~/airflow/airflow.cfg`

#### Met en commentaire la ligne suivante

`dags_folder = /home/<TON_USER>/airflow/dags`

#### Et rajoute la suivante

`dags_folder = /mnt/c/Users/<TON_USER>/OneDrive/Documents/GitHub/Big-Data-Project/dags`

### 9. Lancer Airflow sur le port 8080

`airflow standalone`

## KAGGLE

### 1. Rentrer clé API KAGGLE dans dossier "config"

`Kaggle -> Settings -> API -> Create New Token -> mettre "kaggle.json" dans "config" `

### 2. Définir emplacement clé API KAGGLE

`export KAGGLE_CONFIG_DIR=/chemin/vers/mon-projet/config`

### 3. Télécharger Data Lake

`python .\download_netflix.py`
`python .\download_tmdb_movies.py`

## Spark

### 1. Installer Java
`sudo apt update`
`sudo apt install openjdk-17-jdk -y`

Vérification :
`readlink -f $(which java)`

Tu dois obtenir un chemin comme :
`/usr/lib/jvm/java-17-openjdk-amd64/bin/java`

Vérifie que ça correspond bien au script `start_airflow.sh`

---

## ⚙️ Utilisation

- L’interface Airflow est accessible sur http://localhost:8080
- Déployer et gérer vos DAGs via l’interface
- Le scheduler orchestre les exécutions selon les plannings

## Scripts démarrage et arrêtage Airflow

Rend exécutables les scripts (une seule fois) :
Dans le terminal WSL du projet : `chmod +x start_airflow.sh stop_airflow.sh`

### Démarrer Airflow

Dans le terminal WSL : `./start_airflow.sh`

Ce script :
- Active automatiquement l’environnement virtuel airflow_venv
- Configure le bon dossier de DAGs pour ce projet (dags/)
- Lance le serveur Airflow (webserver, scheduler, etc.)
Une fois lancé :
- Accédez à l'interface : http://localhost:8080
- Identifiants par défaut : admin / admin

### Arrêter Airflow proprement

Dans le terminal WSL : `./stop_airflow.sh`

