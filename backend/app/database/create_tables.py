from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql+psycopg2://postgres:root@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:

    result = conn.execute(text("SELECT datname FROM pg_database"))

    print("Databases:\n")

    for row in result:
        print(row[0])
