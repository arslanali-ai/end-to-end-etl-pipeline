import requests
import json
from pathlib import Path

API_URL = "https://jsonplaceholder.typicode.com/users"

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent


def extract_data():

    response = requests.get(API_URL, timeout=30)
    response.raise_for_status()

    data = response.json()

    # Create raw data directory
    raw_folder = BASE_DIR / "data" / "raw"
    raw_folder.mkdir(parents=True, exist_ok=True)

    # Save API data
    file_path = raw_folder / "users.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"Extracted {len(data)} records successfully")

    return data


if __name__ == "__main__":
    extract_data()