import requests

from logger import logger
from config import (
    JSEARCH_API_KEY,
    JSEARCH_API_HOST,
    JSEARCH_API_URL,
    JSEARCH_QUERY,
    JSEARCH_COUNTRY,
    JSEARCH_NUM_PAGES,
)


def fetch_jobs_data():
    """
    Fetch jobs from the JSearch API.
    """

    headers = {
        "X-RapidAPI-Key": JSEARCH_API_KEY,
        "X-RapidAPI-Host": JSEARCH_API_HOST,
    }

    params = {
        "query": JSEARCH_QUERY,
        "country": JSEARCH_COUNTRY,
        "num_pages": JSEARCH_NUM_PAGES,
    }

    logger.info("Fetching jobs from JSearch API...")

    try:
        response = requests.get(
            JSEARCH_API_URL,
            headers=headers,
            params=params,
            timeout=20,
        )

        response.raise_for_status()

        logger.info("Jobs fetched successfully.")

        return response.json()

    except requests.exceptions.Timeout:
        logger.error("Request timed out.")

    except requests.exceptions.ConnectionError:
        logger.error("Unable to connect to JSearch API.")

    except requests.exceptions.HTTPError as error:
        logger.error(f"HTTP Error: {error}")

    except requests.exceptions.RequestException as error:
        logger.error(f"Unexpected Error: {error}")

    return None
