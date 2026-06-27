import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Jobs API Configuration
JOBS_API_URL = os.getenv("JOBS_API_URL")
JOBS_LIMIT = int(os.getenv("JOBS_LIMIT"))


print("URL:", JOBS_API_URL)
print("LIMIT:", JOBS_LIMIT)


