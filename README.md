# 🚀 Big Data Project – Airflow + PySpark + DataLake

Pipeline de traitement de données automatisé et modulaire utilisant Apache Airflow, PySpark, API KAGGLE, DataLake, Elasticsearch et Kibana.

---

## 📁 Prérequis

- Système Linux/macOS ou Windows avec WSL
- Python 3.7+
- pip
- git
- Compte Kaggle avec clé API (`kaggle.json`)

---

## 🧱 Installation & Configuration

### 🔁 Passage sous WSL (si Windows)
Suivre le guide officiel : [Installation WSL](https://learn.microsoft.com/fr-fr/windows/wsl/install)

---

## 🔧 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/Booboo123478/Big-Data-Project.git
cd Big-Data-Project
```

### 2. Créer un environnement virtuel

```bash
sudo apt update
sudo apt install python3-venv -y
python3 -m venv airflow_venv
source airflow_venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Installer Airflow

```bash
PYTHON_VERSION=$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)
pip install "apache-airflow[celery]==2.9.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.0/constraints-$PYTHON_VERSION.txt"
```

---

## 🔗 Configuration Airflow

### 1. Modifier le dossier des DAGs (si besoin)

```bash
export AIRFLOW__CORE__DAGS_FOLDER=$(pwd)/dags
```

Ou modifier dans `~/airflow/airflow.cfg` :

```ini
# dags_folder = /home/username/airflow/dags
dags_folder = /mnt/c/Users/<TON_USER>/Documents/GitHub/Big-Data-Project/dags
```

### 2. Connexion Spark dans Airflow

Interface Airflow > Admin > Connections > Ajouter

- Conn Id: `spark_default`
- Conn Type: `Spark`
- Host: `local`
- Extra:

```json
{
  "master": "local[*]"
}
```

---

## 📦 KAGGLE

### 1. Mettre `kaggle.json` dans `config/`

Depuis le site Kaggle > Mon compte > Create New Token

### 2. Exporter la variable

```bash
export KAGGLE_CONFIG_DIR=$(pwd)/config
```

---

## ✨ Lancement Airflow

### Rendre les scripts exécutables :

```bash
chmod +x start_airflow.sh stop_airflow.sh
```

### Lancer

```bash
cd scripts
./start_airflow.sh
```

Airflow accessible sur [http://localhost:8080](http://localhost:8080)

### Arrêter

```bash
cd scripts
./stop_airflow.sh
```

---

## 🧩 Spark

### 1. Installer Java

```bash
sudo apt update
sudo apt install openjdk-17-jdk -y
```

### 2. Vérifier le chemin Java

```bash
readlink -f $(which java)
```

Mettre ce chemin dans `start_airflow.sh` sous `JAVA_HOME`

### 3. Installer Spark

```bash
wget https://dlcdn.apache.org/spark/spark-3.4.1/spark-3.4.1-bin-hadoop3.tgz
tar -xvzf spark-3.4.1-bin-hadoop3.tgz
rm spark-3.4.1-bin-hadoop3.tgz
```

Ajouter au `~/.bashrc` ou temporairement :

```bash
export SPARK_HOME=$(pwd)/spark-3.4.1-bin-hadoop3
export PATH=$PATH:$SPARK_HOME/bin
```

---

## 🔍 Elasticsearch & Kibana

### 1. Télécharger et copier depuis Windows vers WSL

```bash
cp /mnt/c/Users/<USER>/Downloads/elasticsearch-<ver>.tar.gz .
cp /mnt/c/Users/<USER>/Downloads/kibana-<ver>.tar.gz .
```

### 2. Décompresser

```bash
tar -xvzf elasticsearch-<ver>.tar.gz
tar -xvzf kibana-<ver>.tar.gz
rm *.tar.gz
```

### 3. Lancer Elasticsearch

```bash
cd elasticsearch-<ver>
bin/elasticsearch
```

### 4. Lancer Kibana

```bash
cd kibana-<ver>
bin/kibana
```

### 5. Suivre les instructions de vérification :

- Copier/coller le code d’enrollment
- Vérifier le token et code d’authentification

---

## 📊 Kibana - Dashboard

### Importer un dashboard `.ndjson`

1. Aller dans "Stack Management" > "Saved Objects" > Import
2. Sélectionner le fichier `.ndjson`
3. Aller dans "Dashboards" > ouvrir

---

## 📤 Exporter vers Windows

Dans le terminal WSL :

```bash
cp -r ~/Big-Data-Project /mnt/c/Users/<TON_USER>/Desktop/
```

---

## 📌 Exécution de l’indexation manuellement

```bash
cd indexing/
python3 indexing_kpi.py
```

# Elasticsearch + Kibana

Je précise que j'ai tout mis en fonction de mon User (Les premières commandes)

### Exemple avec mon emplacement de DL
C:\Users\marca\Downloads\elasticsearch-9.0.2-linux-x86_64.tar.gz
C:\Users\marca\Downloads\kibana-9.0.2-linux-x86_64.tar.gz

### Déplacer les dossier : Sur WSL ~/Big-Data-Project$ 
```Bash
cp /mnt/c/Users/marca/Downloads/elasticsearch-9.0.2-linux-x86_64.tar.gz ~/Big-Data-Project/
```
```Bash
cp /mnt/c/Users/marca/Downloads/kibana-9.0.2-linux-x86_64.tar.gz ~/Big-Data-Project/
```

### Dézipper les dossier : Sur WSL ~/Big-Data-Project$
```Bash
tar -xvzf elasticsearch-9.0.2-linux-x86_64.tar.gz
```
```Bash
tar -xvzf kibana-9.0.2-linux-x86_64.tar.gz
```
### Supprimer les dossier zippé : Sur WSL ~/Big-Data-Project$
```Bash
rm -rf ~/Big-Data-Project/elasticsearch-9.0.2-linux-x86_64.tar.gz
```
```Bash
rm -rf ~/Big-Data-Project/kibana-9.0.2-linux-x86_64.tar.gz
```

### Lancer Elasticsearch : Sur WSL ~/Big-Data-Project/elasticsearch-9.0.2$ 
Je te conseil d'ouvrir un nouveau terminal
```Bash
bin/elasticsearch
```
Tu reçois un MDP, prend le en note (Exemple du miens : R8=vg8aFslx9fySEIpGY) 
Il faudra modifier le MDP dans le fichier d'indexion.

### Lancer Kibana : Sur WSL ~/Big-Data-Project/kibana-9.0.2$
Je te conseil d'ouvrir un nouveau terminal
```Bash
bin/kibana
```

### Récupération d eEnrollment token : Sur WSL ~/Big-Data-Project/elasticsearch-9.0.2$
Enrollment token : 
```Bash
bin/elasticsearch-create-enrollment-token -s kibana
```

### Code de vérification : Sur WSL ~/Big-Data-Project/kibana-9.0.2$
Copy the code : 
```Bash
bin/kibana-verification-code
```

### Lancer Manuellement L'indexion : Sur WSL ~/Big-Data-Project/indexing$
```Bash
python3 indexing_kpi.py
```

### Sur Kibana
Username : elastic
Password : Ton MDP (Exemple du miens : R8=vg8aFslx9fySEIpGY) 

Barre de recherche : Visualise library

Create Data View
Nom : kpis
index patern : kpis
Save Data View to Kibana

Create New Visualisation
Lens : permet la création des éléments du Dashboard

### Import du Dashboard
📥 1️⃣ Accéder à la gestion des objets enregistrés
Va dans Kibana.

Clique sur "Stack Management".

Dans la section "Saved Objects", trouve l'option "Import".

🔄 2️⃣ Importer le fichier JSON
Clique sur "Import".

Sélectionne ton fichier JSON exporté.

Valide l'importation et assure-toi que tout est bien pris en compte.

🚀 3️⃣ Vérifier le dashboard
Après l'importation, va dans "Dashboards".

Ton dashboard importé devrait apparaître.

Ouvre-le et vérifie que les données sont correctes.