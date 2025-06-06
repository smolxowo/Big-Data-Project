from pyspark.sql import SparkSession
from datetime import datetime
import os

# Initialiser Spark
spark = SparkSession.builder.appName("FormatTMDB").getOrCreate()

# Chemin d'entrée (raw)
today = datetime.today().strftime("%y-%m-%d")
input_path = f"data/raw/tmdb/tmdb_{today}.csv"
output_path = f"data/formatted/tmdb/tmdb_{today}.parquet"

# Lire le CSV brut
df = spark.read.option("header", True).option("inferSchema", True).csv(input_path)

# Nettoyage minimal : suppression des colonnes vides
df_clean = df.dropna(how="all")

# Écriture en Parquet
df_clean.write.mode("overwrite").parquet(output_path)

print(f"TMDB formatté écrit dans : {output_path}")
spark.stop()
