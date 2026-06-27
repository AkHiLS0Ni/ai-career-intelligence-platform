import requests

from logger import logger
from config import JOBS_API_URL


def fetch_jobs_data():
    """
    Fetch AI jobs from the Jobs API.
    Returns JSON data if successful.
    Returns None if the request fails.
    """

    logger.info("Fetching jobs data...")

    try:
        response = requests.get(JOBS_API_URL, timeout=10)

        response.raise_for_status()

        logger.info("Jobs data fetched successfully.")

        return response.json()

    except requests.exceptions.Timeout:
        logger.error("Request timed out.")

    except requests.exceptions.ConnectionError:
        logger.error("Unable to connect to Jobs API.")

    except requests.exceptions.HTTPError as error:
        logger.error(f"HTTP Error: {error}")

    except requests.exceptions.RequestException as error:
        logger.error(f"Unexpected Error: {error}")

    return None
