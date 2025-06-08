from pyspark.sql import SparkSession
from datetime import datetime
import json
import os

# Crée une session Spark
spark = SparkSession.builder.appName("CheckCombinedParquet").getOrCreate()

# Date du jour
today = datetime.today().strftime("%y-%m-%d")

# Chemin vers le fichier parquet combiné
data_path = f"data/combined/movies_combined_{today}.parquet"

# Lecture du fichier
if os.path.exists(data_path):
    df = spark.read.parquet(data_path)

    # Affiche la structure des colonnes
    print("\nColonnes du fichier combiné :")
    df.printSchema()

    # Affiche les premières lignes
    print("\nAperçu des données :")
    df.show(10, truncate=False)
else:
    print(f"Fichier non trouvé : {data_path}")

# Chemin vers le fichier JSON des KPIs
kpis_path = f"data/kpis/kpis_{today}.json"

# Lecture et affichage des KPIs
if os.path.exists(kpis_path):
    print("\nKPIs générés :")
    with open(kpis_path, 'r') as f:
        kpis = json.load(f)
        for key, value in kpis.items():
            print(f"{key}: {value}")
else:
    print(f"Fichier KPI non trouvé : {kpis_path}")

# Fermer la session
spark.stop()
