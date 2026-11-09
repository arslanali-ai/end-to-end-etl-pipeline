from .extract import extract_data
from .transform import transform_data
from .load import load_data


def run_pipeline():

    print("ETL Pipeline Started")

    # Extract
    raw_data = extract_data()

    # Transform
    clean_data = transform_data(raw_data)

    # Load
    load_data(clean_data)

    print("ETL Pipeline Completed Successfully!")


if __name__ == "__main__":
    run_pipeline()