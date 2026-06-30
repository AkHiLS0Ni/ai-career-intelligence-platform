import os
import pandas as pd

# ==========================================================
# Load Processed JSearch Data
# ==========================================================

df = pd.read_json("data/processed/jsearch/jobs.json")

print("✅ Data loaded successfully!\n")

# ==========================================================
# First 5 Rows
# ==========================================================

print("=" * 70)
print("First 5 Jobs")
print("=" * 70)

print(df.head())

# ==========================================================
# Dataset Information
# ==========================================================

print("\n")
print("=" * 70)
print("Dataset Information")
print("=" * 70)

df.info()

# ==========================================================
# Statistical Summary
# ==========================================================

print("\n")
print("=" * 70)
print("Statistical Summary")
print("=" * 70)

print(df.describe())

# ==========================================================
# Job Titles
# ==========================================================

print("\n")
print("=" * 70)
print("Job Titles")
print("=" * 70)

print(df["job_title"])

# ==========================================================
# Company and Salary
# ==========================================================

print("\n")
print("=" * 70)
print("Company and Salary")
print("=" * 70)

print(df[["company", "salary_min", "salary_max"]])

# ==========================================================
# Top Hiring Companies
# ==========================================================

print("\n")
print("=" * 70)
print("Top Hiring Companies")
print("=" * 70)

print(df["company"].value_counts().head(10))

# ==========================================================
# Remote vs On-site Jobs
# ==========================================================

print("\n")
print("=" * 70)
print("Remote vs On-site Jobs")
print("=" * 70)

print(df["remote"].value_counts())

# ==========================================================
# Employment Type
# ==========================================================

print("\n")
print("=" * 70)
print("Employment Types")
print("=" * 70)

print(df["employment_type"].value_counts())

# ==========================================================
# Top Cities
# ==========================================================

print("\n")
print("=" * 70)
print("Top Hiring Cities")
print("=" * 70)

print(df["city"].value_counts().head(10))

# ==========================================================
# Highest Paying Jobs
# ==========================================================

print("\n")
print("=" * 70)
print("Highest Paying Jobs")
print("=" * 70)

salary_df = df.dropna(subset=["salary_max"])

if not salary_df.empty:
    salary_df = salary_df.sort_values(
        by="salary_max",
        ascending=False
    )

    print(
        salary_df[
            ["job_title", "company", "salary_min", "salary_max"]
        ]
    )
else:
    print("No salary information available.")

# ==========================================================
# Export Jobs CSV
# ==========================================================

os.makedirs("output", exist_ok=True)

df.to_csv(
    "output/jsearch_jobs.csv",
    index=False
)

print("\n✅ Job CSV exported successfully!")

# ==========================================================
# AI Skills Analysis
# ==========================================================

print("\n")
print("=" * 70)
print("AI Skills Analysis")
print("=" * 70)

skills = [
    "Python",
    "SQL",
    "AWS",
    "Azure",
    "Spark",
    "Docker",
    "Kubernetes",
    "TensorFlow",
    "PyTorch",
    "LangChain",
    "LLM",
    "RAG",
    "Airflow",
    "Snowflake",
    "Pandas",
    "NumPy",
    "FastAPI",
    "Machine Learning",
    "Deep Learning",
]

skill_count = {skill: 0 for skill in skills}

for description in df["description"]:

    if pd.isna(description):
        continue

    description = description.lower()

    for skill in skills:

        if skill.lower() in description:
            skill_count[skill] += 1

skills_df = pd.DataFrame(
    list(skill_count.items()),
    columns=["Skill", "Count"]
)

skills_df = skills_df.sort_values(
    by="Count",
    ascending=False
)

print(skills_df)

# ==========================================================
# Export Skills CSV
# ==========================================================

skills_df.to_csv(
    "output/ai_skills_report.csv",
    index=False
)

print("\n✅ AI Skills Report exported successfully!")
