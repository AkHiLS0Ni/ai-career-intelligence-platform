import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
JSEARCH_API_KEY = os.getenv("JSEARCH_API_KEY")
JSEARCH_API_HOST = os.getenv("JSEARCH_API_HOST")
JSEARCH_API_URL = os.getenv("JSEARCH_API_URL")

# Search Parameters
JSEARCH_QUERY = os.getenv("JSEARCH_QUERY")
JSEARCH_COUNTRY = os.getenv("JSEARCH_COUNTRY")
JSEARCH_NUM_PAGES = int(os.getenv("JSEARCH_NUM_PAGES"))

print("API URL:", JSEARCH_API_URL)
print("Query:", JSEARCH_QUERY)
print("Country:", JSEARCH_COUNTRY)
