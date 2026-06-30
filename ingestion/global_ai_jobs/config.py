import os

RAW_DATA_PATH = "data/raw/global_ai_jobs/global_ai_jobs.csv"

PROCESSED_DATA_PATH = "data/processed/global_ai_jobs/jobs.csv"

OUTPUT_DIRECTORY = "data/processed/global_ai_jobs"

os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)
