import os
import pandas as pd

# Read processed JSearch data
df = pd.read_json("data/processed/jsearch/jobs.json")

print("✅ Data loaded successfully!\n")

print("=" * 70)
print("First 5 Jobs")
print("=" * 70)

print(df.head())

print("\n")

print("=" * 70)
print("Dataset Information")
print("=" * 70)

df.info()

print("\n")

print("=" * 70)
print("Statistical Summary")
print("=" * 70)

print(df.describe())

print("\n")

print("=" * 70)
print("Job Titles")
print("=" * 70)

print(df["job_title"])

print("\n")

print("=" * 70)
print("Company and Salary")
print("=" * 70)

print(df[["company", "salary_min", "salary_max"]])

os.makedirs("output", exist_ok=True)

df.to_csv(
    "output/jsearch_jobs.csv",
    index=False
)

print("\n✅ CSV exported successfully!")
