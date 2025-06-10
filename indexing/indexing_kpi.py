import os
import json
from elasticsearch import Elasticsearch

# Connexion au cluster Elasticsearch (avec HTTPS et authentification)
es = Elasticsearch(
    ["https://localhost:9200"],
    basic_auth=("elastic", "R8=vg8aFslx9fySEIpGY"),
    verify_certs=False  # Mettre True si tu as configuré les certificats correctement
)

# Dossier contenant les fichiers KPI JSON
kpi_folder = "../data/kpis"

# Parcours tous les fichiers du dossier
for filename in os.listdir(kpi_folder):
    if filename.endswith(".json"):
        filepath = os.path.join(kpi_folder, filename)
        with open(filepath, "r") as f:
            kpi_data = json.load(f)

        # Indexation dans l'index 'kpis'
        response = es.index(index="kpis", document=kpi_data)
        print(f"Indexé {filename} avec id {response['_id']}")

# # Chemin vers ton fichier JSON
# file_path = "data/kpis/kpis_25-06-08.json"

# # Charger le contenu JSON
# with open(file_path, "r") as f:
#     kpi_data = json.load(f)

# # Indexer dans Elasticsearch
# response = es.index(index="kpis_summary", document=kpi_data)

# print("Document indexé, ID:", response["_id"])