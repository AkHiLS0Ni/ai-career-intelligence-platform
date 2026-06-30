import pandas as pd

from logger import logger
from config import RAW_DATA_PATH


def load_jobs_data():
    """
    Load the Global AI Jobs dataset from the CSV file.
    """

    logger.info("Loading Global AI Jobs dataset...")

    try:
        df = pd.read_csv(RAW_DATA_PATH)

        logger.info(f"Dataset loaded successfully. Total rows: {len(df)}")

        return df

    except FileNotFoundError:
        logger.error(f"File not found: {RAW_DATA_PATH}")

    except pd.errors.EmptyDataError:
        logger.error("CSV file is empty.")

    except Exception as error:
        logger.error(f"Unexpected Error: {error}")

    return None
