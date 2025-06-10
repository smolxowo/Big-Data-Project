import os
import json
from elasticsearch import Elasticsearch

def indexing_kpis():
    es = Elasticsearch(["https://localhost:9200"], basic_auth=("elastic", "R8=vg8aFslx9fySEIpGY"), verify_certs=False)

    try:
        response = es.info()
        print("✅ Connexion à Elasticsearch réussie :", response)
    except Exception as e:
        print("❌ Erreur de connexion :", e)
        return

    kpi_folder = "data/kpis"

    for filename in os.listdir(kpi_folder):
        if filename.endswith(".json"):
            filepath = os.path.join(kpi_folder, filename)
            with open(filepath, "r") as f:
                kpi_data = json.load(f)

            # Indexation des films
            if "top_roi_movies" in kpi_data:
                for movie in kpi_data["top_roi_movies"]:
                    movie_doc = {"title": movie["title"], "roi": float(movie["roi"])}
                    es.index(index="kpis", document=movie_doc)

            # Indexation des langues
            if "languages_distribution" in kpi_data:
                for lang in kpi_data["languages_distribution"]:
                    lang_doc = {"language": lang["language"], "count": int(lang["count"])}
                    es.index(index="kpis", document=lang_doc)

            # Indexation des genres
            if "top_tmdb_genres" in kpi_data:
                for genre in kpi_data["top_tmdb_genres"]:
                    # genre_doc = {"genre": genre["genre"], "count": int(genre["count"])}
                    # es.index(index="kpis", document=genre_doc)
                    if isinstance(genre, dict) and "genre" in genre and "count" in genre:
                        genre_doc = {"genre": genre["genre"], "genre_count": int(genre["count"])}
                        response = es.index(index="kpis_genres", document=genre_doc)
                        print(f"Indexé {genre['genre']} avec ID {response['_id']}")

