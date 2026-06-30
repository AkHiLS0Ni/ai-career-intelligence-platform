import pandas as pd

from service import load_jobs_data
from config import PROCESSED_DATA_PATH


def clean_jobs_data(df):
    """
    Clean and preprocess the Global AI Jobs dataset.
    """

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Standardize column names
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Convert salary columns to numeric (if they exist)
    salary_columns = [
        "salary_usd",
        "bonus_usd",
        "salary_percentile",
    ]

    for column in salary_columns:

        if column in df.columns:

            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    return df


def save_processed_data(df):
    """
    Save processed dataset.
    """

    df.to_csv(
        PROCESSED_DATA_PATH,
        index=False
    )

    print("✅ Processed Global AI Jobs dataset saved successfully!")


def main():

    df = load_jobs_data()

    if df is None:
        return

    clean_df = clean_jobs_data(df)

    save_processed_data(clean_df)

    print("\n📊 Dataset Preview")
    print("=" * 80)

    print(clean_df.head())

    print("\n")
    print("=" * 80)
    print(f"Total Rows : {len(clean_df)}")
    print(f"Total Columns : {len(clean_df.columns)}")


if __name__ == "__main__":
    main()
