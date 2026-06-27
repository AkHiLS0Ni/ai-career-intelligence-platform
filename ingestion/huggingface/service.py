import requests

from logger import logger
from config import HF_API_URL, HF_LIMIT


def fetch_huggingface_data():
    """
    Fetch trending models from the Hugging Face API.
    """

    url = f"{HF_API_URL}?limit={HF_LIMIT}"

    logger.info("Fetching Hugging Face models...")

    try:
        response = requests.get(url, timeout=10)

        response.raise_for_status()

        logger.info("Hugging Face data fetched successfully.")

        return response.json()
    except requests.exceptions.Timeout:
        logger.error("Request timed out.")
    except requests.exceptions.ConnectionError:
        logger.error("Unable to connect to Hugging Face.")
    except requests.exceptions.HTTPError as error:
        logger.error(f"HTTP Error: {error}")
    except requests.exceptions.RequestException as error:
        logger.error(f"Unexpected Error: {error}")
    return None                
    