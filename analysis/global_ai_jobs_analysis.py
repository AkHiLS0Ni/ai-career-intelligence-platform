import os
import pandas as pd

# ==========================================================
# Load Dataset
# ==========================================================

df = pd.read_csv("data/processed/global_ai_jobs/jobs.csv")

print("✅ Global AI Jobs dataset loaded successfully!\n")

# ==========================================================
# Basic Information
# ==========================================================

print("=" * 80)
print("Dataset Information")
print("=" * 80)

print(df.info())

print("\n")

print("=" * 80)
print("Statistical Summary")
print("=" * 80)

print(df.describe())

# ==========================================================
# Total Jobs
# ==========================================================

print("\n")
print("=" * 80)
print("Total AI Jobs")
print("=" * 80)

print(len(df))

# ==========================================================
# Top Countries
# ==========================================================

print("\n")
print("=" * 80)
print("Top Hiring Countries")
print("=" * 80)

print(df["country"].value_counts().head(10))

# ==========================================================
# Top AI Roles
# ==========================================================

print("\n")
print("=" * 80)
print("Top AI Roles")
print("=" * 80)

print(df["job_role"].value_counts().head(10))

# ==========================================================
# AI Specializations
# ==========================================================

print("\n")
print("=" * 80)
print("AI Specializations")
print("=" * 80)

print(df["ai_specialization"].value_counts().head(10))

# ==========================================================
# Work Mode
# ==========================================================

print("\n")
print("=" * 80)
print("Work Mode")
print("=" * 80)

print(df["work_mode"].value_counts())

# ==========================================================
# Education
# ==========================================================

print("\n")
print("=" * 80)
print("Education Required")
print("=" * 80)

print(df["education_required"].value_counts())

# ==========================================================
# Company Size
# ==========================================================

print("\n")
print("=" * 80)
print("Company Size")
print("=" * 80)

print(df["company_size"].value_counts())

# ==========================================================
# Average Salary by Country
# ==========================================================

print("\n")
print("=" * 80)
print("Average Salary by Country")
print("=" * 80)

salary_country = (
    df.groupby("country")["salary_usd"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print(salary_country)

# ==========================================================
# Highest Paying AI Roles
# ==========================================================

print("\n")
print("=" * 80)
print("Highest Paying AI Roles")
print("=" * 80)

salary_role = (
    df.groupby("job_role")["salary_usd"]
    .mean()
    .sort_values(ascending=False)
)

print(salary_role)

# ==========================================================
# Employee Satisfaction
# ==========================================================

print("\n")
print("=" * 80)
print("Top Employee Satisfaction")
print("=" * 80)

print(
    df.groupby("job_role")["employee_satisfaction"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

# ==========================================================
# Career Growth
# ==========================================================

print("\n")
print("=" * 80)
print("Career Growth")
print("=" * 80)

print(
    df.groupby("job_role")["career_growth_score"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

# ==========================================================
# Export Clean CSV
# ==========================================================

os.makedirs("output", exist_ok=True)

df.to_csv(
    "output/global_ai_jobs.csv",
    index=False
)

print("\n✅ Global AI Jobs CSV exported successfully!")
