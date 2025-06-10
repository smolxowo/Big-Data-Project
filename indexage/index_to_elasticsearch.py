from elasticsearch import Elasticsearch
from pyspark.sql import SparkSession
from datetime import datetime

def index_movies_to_elasticsearch():
    try:
        es = Elasticsearch("http://localhost:9200")
        
        if not es.ping():
            print("Elasticsearch is not reachable.")
            return
        
        if not es.indices.exists(index="movies"):
            es.indices.create(index="movies")

        spark = SparkSession.builder.appName("IndexToElasticsearch").getOrCreate()
        today = datetime.today().strftime("%y-%m-%d")
        input_path = f"data/combined/movies_combined_{today}.parquet"
        df = spark.read.parquet(input_path)
        records = df.limit(10000).toPandas().fillna("").to_dict(orient="records")

        for i, record in enumerate(records):
            es.index(index="movies", id=i, document=record)

        print(f"{len(records)} documents indexés.")
        spark.stop()
    except Exception as e:
        print("Erreur lors de l'indexation :", e)
