from pyspark.sql import SparkSession
from datetime import datetime
import os
from pyspark.sql.functions import col

# Initialiser Spark
spark = SparkSession.builder.appName("FormatNetflix").getOrCreate()

# Chemin d'entrée (raw)
today = datetime.today().strftime("%y-%m-%d")
input_path = f"data/raw/netflix/netflix_{today}.csv"
output_path = f"data/formatted/netflix/netflix_{today}.parquet"

# Lire le CSV brut
df = spark.read.option("header", True).option("inferSchema", True).csv(input_path)

# Nettoyage minimal : suppression des colonnes vides
df_clean = df.dropna(how="all")

# Casting des colonnes importantes
df_clean = df_clean.withColumn("releaseYear", col("releaseYear").cast("int")) \
                   .withColumn("imdbAverageRating", col("imdbAverageRating").cast("float")) \
                   .withColumn("imdbNumVotes", col("imdbNumVotes").cast("int"))


# Écriture en Parquet
df_clean.write.mode("overwrite").parquet(output_path)

print(f"Netflix formatté écrit dans : {output_path}")
spark.stop()
