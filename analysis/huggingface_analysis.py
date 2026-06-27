import os
import pandas as pd

# ==========================================================
# Read processed Hugging Face data
# ==========================================================

df = pd.read_json("data/processed/huggingface/models.json")

print("✅ Data loaded successfully!\n")

# ==========================================================
# First 5 Rows
# ==========================================================

print("=" * 60)
print("First 5 Rows")
print("=" * 60)

print(df.head())

# ==========================================================
# Dataset Information
# ==========================================================

print("\n")
print("=" * 60)
print("Dataset Information")
print("=" * 60)

df.info()

# ==========================================================
# Statistical Summary
# ==========================================================

print("\n")
print("=" * 60)
print("Statistical Summary")
print("=" * 60)

print(df.describe())

# ==========================================================
# Model Names
# ==========================================================

print("\n")
print("=" * 60)
print("Model Names")
print("=" * 60)

print(df["model_name"])

# ==========================================================
# Models and Downloads
# ==========================================================

print("\n")
print("=" * 60)
print("Models and Downloads")
print("=" * 60)

print(df[["model_name", "downloads"]])

# ==========================================================
# Popular Models (Downloads > 100000)
# ==========================================================

print("\n")
print("=" * 60)
print("Popular Models")
print("=" * 60)

popular_models = df[df["downloads"] > 100000]

print(popular_models[["model_name", "downloads"]])

# ==========================================================
# Top 10 Downloaded Models
# ==========================================================

print("\n")
print("=" * 60)
print("Top 10 Downloaded Models")
print("=" * 60)

top_downloaded = df.sort_values(
    by="downloads",
    ascending=False
)

print(top_downloaded[["model_name", "downloads"]].head(10))

# ==========================================================
# Task Distribution
# ==========================================================

print("\n")
print("=" * 60)
print("Task Distribution")
print("=" * 60)

print(df["task"].value_counts())

# ==========================================================
# Top Authors
# ==========================================================

print("\n")
print("=" * 60)
print("Top Authors")
print("=" * 60)

print(df["author"].value_counts().head(10))

# ==========================================================
# Top 10 Most Liked Models
# ==========================================================

print("\n")
print("=" * 60)
print("Top 10 Most Liked Models")
print("=" * 60)

top_liked = df.sort_values(
    by="likes",
    ascending=False
)

print(top_liked[["model_name", "likes"]].head(10))

# ==========================================================
# Export CSV
# ==========================================================

os.makedirs("output", exist_ok=True)

df.to_csv(
    "output/huggingface_models.csv",
    index=False
)

print("\n✅ CSV exported successfully!")
