import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

def download_and_extract_netflix_dataset():
    # Chemins
    dataset_ref = "octopusteam/full-netflix-dataset"
    download_dir = "data/raw/netflix"
    zip_filename = "full-netflix-dataset.zip"
    zip_filepath = os.path.join(download_dir, zip_filename)

    # Initialiser l'API Kaggle
    api = KaggleApi()
    api.authenticate()

    print(f"Téléchargement de {dataset_ref} dans {download_dir}...")
    # Télécharger le dataset
    api.dataset_download_files(dataset_ref, path=download_dir, unzip=False, quiet=False)

    # Extraire le zip
    print("Extraction des fichiers...")
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        zip_ref.extractall(download_dir)

    # Supprimer le fichier zip
    os.remove(zip_filepath)
    print("Extraction terminée et fichier zip supprimé.")

if __name__ == "__main__":
    download_and_extract_netflix_dataset()
