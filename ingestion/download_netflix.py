import os
import zipfile
from datetime import datetime
from kaggle.api.kaggle_api_extended import KaggleApi

def download_and_extract_netflix_dataset():
    dataset_ref = "octopusteam/full-netflix-dataset"
    download_dir = "data/raw/netflix"
    os.makedirs(download_dir, exist_ok=True)

    today_str = datetime.today().strftime("%y-%m-%d")
    output_csv = os.path.join(download_dir, f"netflix_{today_str}.csv")

    # Supprimer les .zip existants
    for f in os.listdir(download_dir):
        if f.endswith(".zip"):
            os.remove(os.path.join(download_dir, f))

    api = KaggleApi()
    api.authenticate()

    print(f"Téléchargement de {dataset_ref} dans {download_dir}...")
    api.dataset_download_files(dataset_ref, path=download_dir, unzip=False, quiet=False, force=True)

    zip_files = [f for f in os.listdir(download_dir) if f.endswith(".zip")]
    if not zip_files:
        raise FileNotFoundError("Aucun fichier ZIP trouvé après téléchargement.")
    zip_filepath = os.path.join(download_dir, zip_files[0])

    print("Extraction...")
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        zip_ref.extractall(download_dir)
    os.remove(zip_filepath)
    print("Extraction terminée et fichier zip supprimé.")

    # Renommer le .csv principal
    extracted_csv = [f for f in os.listdir(download_dir) if f.endswith(".csv")]
    if extracted_csv:
        original_path = os.path.join(download_dir, extracted_csv[0])
        os.rename(original_path, output_csv)
        print(f"Fichier CSV renommé en : {output_csv}")

        # Supprimer les autres .csv
        for f in os.listdir(download_dir):
            f_path = os.path.join(download_dir, f)
            if f.endswith(".csv") and f_path != output_csv:
                os.remove(f_path)
    else:
        print("Aucun fichier CSV trouvé après extraction.")

if __name__ == "__main__":
    download_and_extract_netflix_dataset()
