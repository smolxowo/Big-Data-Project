#!/bin/bash

# Active l'environnement virtuel
source airflow_venv/bin/activate

# Définit le dossier des DAGs pour ce projet uniquement
export AIRFLOW__CORE__DAGS_FOLDER=$(pwd)/dags

# Définir JAVA_HOME pour Spark
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

# Lance Airflow
airflow standalone
