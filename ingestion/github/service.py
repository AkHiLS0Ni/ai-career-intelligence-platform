import requests
from logger import logger
from config import (
    GITHUB_API_URL,
    GITHUB_TOPIC,
    GITHUB_SORT,
    GITHUB_ORDER,
)


def fetch_github_data():
    """
    Fetch AI repositories from the GitHub Search API.
    Returns a Python dictionary if successful.
    Returns None if the request fails.
    """

    url = (
        f"{GITHUB_API_URL}"
        f"?q=topic:{GITHUB_TOPIC}"
        f"&sort={GITHUB_SORT}"
        f"&order={GITHUB_ORDER}"
    )

    logger.info("Fetching GitHub data...")

    try:
        response = requests.get(url, timeout=10)

        response.raise_for_status()

        logger.info("GitHub data fetched successfully.")

        return response.json()

    except requests.exceptions.Timeout:
        logger.error("Request timed out.")

    except requests.exceptions.ConnectionError:
        logger.error("Unable to connect to GitHub.")

    except requests.exceptions.HTTPError as error:
        logger.error(f"HTTP Error: {error}")

    except requests.exceptions.RequestException as error:
        logger.error(f"Unexpected Error: {error}")

    return None
