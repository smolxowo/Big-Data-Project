# 🚀 Big Data Project – Airflow + PySpark + DataLake

Pipeline de traitement de données automatisé et modulaire utilisant Apache Airflow, PySpark, API REST et DataLake.

---

## 📁 Prérequis

- Système Linux, macOS ou Windows avec WSL  
- Python 3.7+  
- pip  
- git  

Pour Windows, installer WSL : [Installation WSL](https://learn.microsoft.com/fr-fr/windows/wsl/install)

---

## 🧱 Installation

### 1. Cloner le dépôt  
`git clone https://github.com/Booboo123478/Big-Data-Project.git`  
`cd Big-Data-Project`

### 2. Installer python3-venv (DANS WSL)
`sudo apt update`  
`sudo apt install python3-venv`

### 3. Créer et activer un environnement virtuel Python (DANS WSL)
`python3 -m venv airflow_venv`  
`source airflow_venv/bin/activate`

### 4. Installer Apache Airflow (version 2.9.0 avec Celery)  (DANS WSL)
Récupérer la version de Python :  
`PYTHON_VERSION=$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)`  
Puis installer Airflow avec la contrainte correspondante :  
`pip install "apache-airflow[celery]==2.9.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.0/constraints-$PYTHON_VERSION.txt"`

### 5. Installer les dépendances du projet 
`pip install -r requirements.txt`

### 6. Initialiser la base de données Airflow  
`airflow db init`

### 7. Créer un utilisateur admin Airflow  
`airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com`

### 8. Démarrer le scheduler Airflow  
`airflow scheduler`

### 9. Démarrer le webserver Airflow  
`airflow webserver --port 8080`

### 10. (Optionnel) Démarrer un worker Celery  
`airflow celery worker`

---

## ⚙️ Utilisation

- L’interface Airflow est accessible sur http://localhost:8080  
- Déployer et gérer vos DAGs via l’interface  
- Le scheduler orchestre les exécutions selon les plannings
