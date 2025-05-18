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

### 2. Installer python3-venv (DANS WSL à faire une fois)
`sudo apt update`  
`sudo apt install python3-venv`

### 3. Créer un environnement virtuel Python (DANS WSL à faire une fois)
`python3 -m venv airflow_venv` 

### 4. Activer un environnement virtuel Python (DANS WSL)
`source airflow_venv/bin/activate`

### 5. Installer Apache Airflow (version 2.9.0 avec Celery)  (DANS WSL)
Récupérer la version de Python :  
`PYTHON_VERSION=$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)`  
Puis installer Airflow avec la contrainte correspondante :  
`pip install "apache-airflow[celery]==2.9.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.0/constraints-$PYTHON_VERSION.txt"`

### 6. Installer les dépendances du projet 
`pip install -r requirements.txt`

### 7. Définir le dossier des DAGs (Dans le cas où tu as déjà définis des DAGs ailleurs)
`export AIRFLOW__CORE__DAGS_FOLDER=/mnt/c/Users/<TON_USER>/OneDrive/Documents/GitHub/Big-Data-Project/dags`
# Ou
`nano ~/airflow/airflow.cfg`
# Met en commentaire la ligne suivante
`dags_folder = /home/<TON_USER>/airflow/dags`
# Et rajoute la suivante
`dags_folder = /mnt/c/Users/<TON_USER>/OneDrive/Documents/GitHub/Big-Data-Project/dags`

### 8. Lancer Airflow sur le port 8080
`airflow standalone`

### 9.

---

## ⚙️ Utilisation

- L’interface Airflow est accessible sur http://localhost:8080  
- Déployer et gérer vos DAGs via l’interface  
- Le scheduler orchestre les exécutions selon les plannings
