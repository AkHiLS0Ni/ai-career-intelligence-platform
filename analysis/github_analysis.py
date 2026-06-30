import os
import pandas as pd

# ==========================================================
# Load Processed GitHub Data
# ==========================================================

df = pd.read_json("data/processed/github/repositories.json")

print("✅ GitHub data loaded successfully!\n")

# ==========================================================
# First 5 Rows
# ==========================================================

print("=" * 70)
print("First 5 Repositories")
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
# Repository Names
# ==========================================================

print("\n")
print("=" * 70)
print("Repository Names")
print("=" * 70)

print(df["repository"])

# ==========================================================
# Owner and Stars
# ==========================================================

print("\n")
print("=" * 70)
print("Owner and Stars")
print("=" * 70)

print(df[["owner", "stars"]])

# ==========================================================
# Top 10 Starred Repositories
# ==========================================================

print("\n")
print("=" * 70)
print("Top 10 Starred Repositories")
print("=" * 70)

top_starred = df.sort_values(
    by="stars",
    ascending=False
)

print(
    top_starred[
        [
            "repository",
            "owner",
            "stars"
        ]
    ].head(10)
)

# ==========================================================
# Top 10 Forked Repositories
# ==========================================================

print("\n")
print("=" * 70)
print("Top 10 Forked Repositories")
print("=" * 70)

top_forked = df.sort_values(
    by="forks",
    ascending=False
)

print(
    top_forked[
        [
            "repository",
            "owner",
            "forks"
        ]
    ].head(10)
)

# ==========================================================
# Programming Languages
# ==========================================================

print("\n")
print("=" * 70)
print("Programming Languages")
print("=" * 70)

print(df["language"].value_counts())

# ==========================================================
# Top Owners
# ==========================================================

print("\n")
print("=" * 70)
print("Top Owners")
print("=" * 70)

print(df["owner"].value_counts().head(10))

# ==========================================================
# Recently Updated Repositories
# ==========================================================

print("\n")
print("=" * 70)
print("Recently Updated Repositories")
print("=" * 70)

recent = df.sort_values(
    by="updated_at",
    ascending=False
)

print(
    recent[
        [
            "repository",
            "owner",
            "updated_at"
        ]
    ].head(10)
)

# ==========================================================
# Top Python Repositories
# ==========================================================

print("\n")
print("=" * 70)
print("Top Python Repositories")
print("=" * 70)

python_repos = df[df["language"] == "Python"]

print(
    python_repos[
        [
            "repository",
            "owner",
            "stars"
        ]
    ].sort_values(
        by="stars",
        ascending=False
    )
)

# ==========================================================
# Export CSV
# ==========================================================

os.makedirs("output", exist_ok=True)

df.to_csv(
    "output/github_repositories.csv",
    index=False
)

print("\n✅ GitHub CSV exported successfully!")
