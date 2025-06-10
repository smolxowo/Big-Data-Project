# combined_data_kpis.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, desc, split
from datetime import datetime
import json
import os

# Initialiser Spark
spark = SparkSession.builder.appName("KPIsCombinedMovies").getOrCreate()

# Lire le fichier le plus récent
today = datetime.today().strftime("%y-%m-%d")
combined_path = f"data/combined/movies_combined_{today}.parquet"

# Charger les données
try:
    df = spark.read.parquet(combined_path)
except Exception as e:
    print(f"Erreur lors de la lecture du fichier Parquet : {e}")
    exit(1)

# Nettoyage qualité :
# - exclude vote_count < 10
# - exclude budget <= 0
# - exclude runtime < 40

df_clean = df.dropna(subset=["title", "budget", "revenue", "runtime", "vote_count"]) \
             .filter((col("budget") > 0) & (col("vote_count") >= 10) & (col("runtime") >= 40))

# Calculs
kpis = {}

# Total
kpis["total_movies"] = df_clean.count()

# Moyennes
kpis["average_runtime"] = df_clean.select(avg("runtime")).first()[0]
kpis["average_tmdb_rating"] = df_clean.select(avg("vote_average")).first()[0]
kpis["average_imdb_rating"] = df_clean.select(avg("imdbAverageRating")).first()[0]

# ROI moyen
df_roi = df_clean.withColumn("roi", col("revenue") / col("budget"))
kpis["average_roi"] = df_roi.select(avg("roi")).first()[0]

# Top genres TMDB
top_genres_df = df_clean.withColumn("genre_array", split(col("tmdb_genres"), ",")) \
                   .withColumn("genre", col("genre_array")[0]) \
                   .groupBy("genre").count().orderBy(desc("count")).limit(5)
kpis["top_tmdb_genres"] = [row["genre"] for row in top_genres_df.collect() if row["genre"]]

# # Top genres TMDB avec le nombre de films par genre
# kpis["top_tmdb_genres"] = [{"genre": row["genre"], "count": row["count"]} for row in top_genres_df.collect() if row["genre"]]

# Langues principales
top_langs_df = df_clean.groupBy("original_language").count().orderBy(desc("count")).limit(5)
kpis["top_languages"] = [row["original_language"] for row in top_langs_df.collect() if row["original_language"]]

# # Langue principales avec compteur
# kpis["languages_distribution"] = [
#     {"language": row["original_language"], "count": row["count"]}
#     for row in top_langs_df.collect() if row["original_language"]
# ]

# Top ROI films
top_roi_df = df_roi.select("title", "roi").orderBy(desc("roi")).limit(5)
kpis["top_roi_movies"] = [{"title": row["title"], "roi": row["roi"]} for row in top_roi_df.collect()]

# Sauvegarder au format JSON
output_file = f"data/kpis/kpis_{today}.json"
os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, "w") as f:
    json.dump(kpis, f, indent=2)

print(f"KPIs sauvegardés dans : {output_file}")
spark.stop()
