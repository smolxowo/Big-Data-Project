from pyspark.sql import SparkSession
from datetime import datetime
import os

# Initialiser Spark
spark = SparkSession.builder.appName("CombineNetflixTMDB").getOrCreate()

today = datetime.today().strftime("%y-%m-%d")

# Chemins d'entrée
netflix_path = f"data/formatted/netflix/netflix_{today}.parquet"
tmdb_path = f"data/formatted/tmdb/tmdb_{today}.parquet"
output_path = f"data/combined/movies_combined_{today}.parquet"

# Lecture des datasets
df_netflix = spark.read.parquet(netflix_path).alias("netflix")
df_tmdb = spark.read.parquet(tmdb_path).alias("tmdb")

# Jointure sur le titre
df_joined = df_netflix.join(df_tmdb, df_netflix["title"] == df_tmdb["title"], "inner")

# Sélection avec des alias pour éviter toute ambiguïté
df_result = df_joined.select(
    df_netflix["title"].alias("title"),
    df_netflix["releaseYear"].alias("netflix_release_year"),
    df_netflix["genres"].alias("netflix_genres"),
    df_tmdb["genres"].alias("tmdb_genres"),
    df_tmdb["popularity"],
    df_tmdb["vote_average"]
).dropDuplicates()

# Écriture
df_result.write.mode("overwrite").parquet(output_path)
print(f"Fichier combiné écrit dans : {output_path}")
spark.stop()
