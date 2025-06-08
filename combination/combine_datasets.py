from pyspark.sql import SparkSession
from datetime import datetime
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("CombineNetflixTMDB").getOrCreate()

today = datetime.today().strftime("%y-%m-%d")

netflix_path = f"data/formatted/netflix/netflix_{today}.parquet"
tmdb_path = f"data/formatted/tmdb/tmdb_{today}.parquet"
output_path = f"data/combined/movies_combined_{today}.parquet"

df_netflix = spark.read.parquet(netflix_path).alias("netflix")
df_tmdb = spark.read.parquet(tmdb_path).alias("tmdb")

# Jointure sur le titre
joined = df_netflix.join(df_tmdb, df_netflix["title"] == df_tmdb["title"], "inner")

# Sélection de colonnes pertinentes
result = joined.select(
    df_netflix["title"].alias("title"),
    df_netflix["releaseYear"].alias("netflix_release_year"),
    df_netflix["genres"].alias("netflix_genres"),
    df_netflix["imdbAverageRating"],
    df_netflix["imdbNumVotes"],
    df_netflix["availableCountries"],
    df_tmdb["release_date"],
    df_tmdb["budget"],
    df_tmdb["revenue"],
    df_tmdb["vote_average"],
    df_tmdb["vote_count"],
    df_tmdb["popularity"],
    df_tmdb["runtime"],
    df_tmdb["genres"].alias("tmdb_genres"),
    df_tmdb["original_language"]
).dropDuplicates()

result.write.mode("overwrite").parquet(output_path)
print(f"Fichier combiné écrit dans : {output_path}")
spark.stop()
