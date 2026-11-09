import os
from sqlalchemy import create_engine
from dotenv import load_dotenv


load_dotenv()


def load_data(df):

    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    connection_string = (
        f"postgresql+psycopg2://"
        f"{db_user}:{db_password}@"
        f"{db_host}:{db_port}/{db_name}"
    )

    engine = create_engine(connection_string)

    df.to_sql(
        name="users",
        con=engine,
        if_exists="append",
        index=False
    )

    print("Data loaded into PostgreSQL successfully!")

    engine.dispose()