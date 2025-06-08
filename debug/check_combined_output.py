from pyspark.sql import SparkSession

# Crée une session Spark
spark = SparkSession.builder.appName("CheckCombinedParquet").getOrCreate()

# Chemin vers le fichier parquet combiné
parquet_path = "data/combined/movies_combined_25-06-06.parquet"

# Lecture du fichier
df = spark.read.parquet(parquet_path)

# Affiche la structure des colonnes
print("📋 Colonnes du fichier combiné :")
df.printSchema()

# Affiche les premières lignes
print("\n🔍 Aperçu des données :")
df.show(10, truncate=False)

# Fermer la session
spark.stop()
