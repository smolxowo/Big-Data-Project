from pyspark.sql import SparkSession
from datetime import datetime
import os
from pyspark.sql.functions import col

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

# Casting des colonnes importantes
df_clean = df_clean.withColumn("vote_average", col("vote_average").cast("float")) \
                   .withColumn("vote_count", col("vote_count").cast("int")) \
                   .withColumn("revenue", col("revenue").cast("long")) \
                   .withColumn("runtime", col("runtime").cast("int")) \
                   .withColumn("budget", col("budget").cast("long")) \
                   .withColumn("popularity", col("popularity").cast("float"))

# Écriture en Parquet
df_clean.write.mode("overwrite").parquet(output_path)

print(f"TMDB formatté écrit dans : {output_path}")
spark.stop()
