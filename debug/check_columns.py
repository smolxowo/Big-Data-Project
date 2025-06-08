from pyspark.sql import SparkSession
from datetime import datetime

spark = SparkSession.builder.appName("CheckDatasetColumns").getOrCreate()

today = datetime.today().strftime("%y-%m-%d")
netflix_path = f"data/formatted/netflix/netflix_{today}.parquet"
tmdb_path = f"data/formatted/tmdb/tmdb_{today}.parquet"

df_netflix = spark.read.parquet(netflix_path)
df_tmdb = spark.read.parquet(tmdb_path)

print("Colonnes Netflix :")
df_netflix.printSchema()

print("\nColonnes TMDB :")
df_tmdb.printSchema()

# Vérifier si des colonnes spécifiques sont présentes
required_netflix_cols = ["title", "releaseYear", "genres"]
required_tmdb_cols = ["title", "genres", "popularity", "vote_average"]

print("\n🔎 Vérification des colonnes...")

missing_netflix = [col for col in required_netflix_cols if col not in df_netflix.columns]
missing_tmdb = [col for col in required_tmdb_cols if col not in df_tmdb.columns]

if not missing_netflix and not missing_tmdb:
    print("✅ Toutes les colonnes nécessaires sont présentes.")
else:
    if missing_netflix:
        print("❌ Colonnes manquantes dans Netflix:", missing_netflix)
    if missing_tmdb:
        print("❌ Colonnes manquantes dans TMDB:", missing_tmdb)

spark.stop()
