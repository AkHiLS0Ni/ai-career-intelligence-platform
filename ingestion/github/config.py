import os
from pathlib import Path
from dotenv import load_dotenv

# Get project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Load .env from project root
load_dotenv(BASE_DIR / ".env")

# GitHub Configuration
GITHUB_API_URL = os.getenv("GITHUB_API_URL")
GITHUB_TOPIC = os.getenv("GITHUB_TOPIC")
GITHUB_SORT = os.getenv("GITHUB_SORT")
GITHUB_ORDER = os.getenv("GITHUB_ORDER")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
