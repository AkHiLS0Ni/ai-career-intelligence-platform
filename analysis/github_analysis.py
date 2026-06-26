import pandas as pd

# Read processed GitHub data
df = pd.read_json("data/processed/github/repositories.json")

print("✅ Data loaded successfully!\n")

print("=" * 60)
print("First 5 Rows")
print("=" * 60)

print(df.head())

print("\n")

print("=" * 60)
print("Dataset Information")
print("=" * 60)

df.info()

print("\n")

print("=" * 60)
print("Statistical Summary")
print("=" * 60)

print(df.describe())
print("\n")
print("=" * 60)
print("Repository Names")
print("=" * 60)

print(df["repository"])


print("\n")
print("=" * 60)
print("Repository and Stars")
print("=" * 60)

print(df[["repository", "stars"]])


print("\n")
print("=" * 60)
print("Python Repositories")
print("=" * 60)

python_repos = df[df["language"] == "Python"]

print(python_repos)


print("\n")
print("=" * 60)
print("Repositories with more than 50,000 Stars")
print("=" * 60)

popular_repos = df[df["stars"] > 50000]

print(popular_repos)
print("\n")
print("=" * 60)
print("Top 10 Repositories by Stars")
print("=" * 60)

top_10 = df.sort_values(by="stars", ascending=False).head(10)

print(top_10[["repository", "stars"]])


print("\n")
print("=" * 60)
print("Programming Languages")
print("=" * 60)

print(df["language"].value_counts())


print("\n")
print("=" * 60)
print("Exporting Data to CSV")
print("=" * 60)

df.to_csv("output/github_repositories.csv", index=False)

print("✅ CSV file created successfully!")
