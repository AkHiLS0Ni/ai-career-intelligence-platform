from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql+psycopg2://postgres:root@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:

        print("✅ Connected!")

        result = conn.execute(text("SELECT datname FROM pg_database"))

        print("\nDatabases:")

        for row in result:
            print(row[0])

except Exception as e:
    print(e)
