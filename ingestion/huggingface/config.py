import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Hugging Face Configuration
HF_API_URL = os.getenv("HF_API_URL")
HF_LIMIT = int(os.getenv("HF_LIMIT"))
