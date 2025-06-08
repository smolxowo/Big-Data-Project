# scripts/cleanup_history.py

import os
import re
from datetime import datetime, timedelta

def cleanup_old_files():
    paths = [
        "data/formatted/netflix",
        "data/formatted/tmdb",
        "data/combined"
    ]

    cutoff_date = datetime.today() - timedelta(days=3)
    date_pattern = re.compile(r".*_(\d{4}-\d{2}-\d{2})\.parquet$")

    for folder in paths:
        if not os.path.exists(folder):
            continue

        for filename in os.listdir(folder):
            match = date_pattern.match(filename)
            if match:
                file_date_str = match.group(1)
                try:
                    file_date = datetime.strptime(file_date_str, "%Y-%m-%d")
                    if file_date < cutoff_date:
                        file_path = os.path.join(folder, filename)
                        print(f"Suppression de : {file_path}")
                        os.system(f"rm -r '{file_path}'")
                except ValueError:
                    print(f"Format de date non reconnu : {file_date_str}")
