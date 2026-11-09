
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def transform_data(data):
    # JSON data ko DataFrame mein convert karein
    df = pd.json_normalize(data)

    # Required columns select karein
    df = df[
        [
            "id",
            "name",
            "username",
            "email",
            "phone",
            "website",
            "address.city",
            "company.name"
        ]
    ]

    # Column names change karein
    df.columns = [
        "user_id",
        "name",
        "username",
        "email",
        "phone",
        "website",
        "city",
        "company"
    ]

    # Duplicate records remove karein
    df = df.drop_duplicates(subset=["user_id"])

    # Text columns clean karein
    text_columns = [
        "name", "username", "email",
        "phone", "website", "city", "company"
    ]

    for col in text_columns:
        df[col] = df[col].astype("string").str.strip()

    # Email lowercase karein
    df["email"] = df["email"].str.lower()

    # Missing required values remove karein
    df = df.dropna(subset=["user_id", "email"])

    # User ID integer banayein
    df["user_id"] = df["user_id"].astype(int)

    # Processed folder create karein
    processed_folder = BASE_DIR / "data" / "processed"
    processed_folder.mkdir(parents=True, exist_ok=True)

    # Clean data CSV mein save karein
    output_file = processed_folder / "cleaned_users.csv"
    df.to_csv(output_file, index=False)

    print("Data transformed successfully")
    print(df.head())

    return df
