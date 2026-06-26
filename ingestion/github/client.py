import json
from service import fetch_github_data


def save_raw_data(data):
    """
    Save raw GitHub API response to a JSON file.
    """

    with open("data/raw/github/github_api.json", "w") as file:
        json.dump(data, file, indent=4)

    print("✅ Raw data saved successfully!")


def extract_repository_data(data):
    """
    Extract only the required repository fields.
    """

    clean_data = []

    for repo in data["items"]:

        repository = {
            "repository": repo["name"],
            "owner": repo["owner"]["login"],
            "description": repo["description"],
            "language": repo["language"],
            "stars": repo["stargazers_count"],
            "forks": repo["forks_count"],
            "updated_at": repo["updated_at"]
        }

        clean_data.append(repository)

    return clean_data


def save_processed_data(clean_data):
    """
    Save cleaned repository data to a JSON file.
    """

    with open("data/processed/github/repositories.json", "w") as file:
        json.dump(clean_data, file, indent=4)

    print("✅ Processed data saved successfully!")


def main():
    """
    Main entry point of the GitHub ingestion pipeline.
    """

    data = fetch_github_data()

    if data is None:
        return

    # Save raw GitHub API response
    save_raw_data(data)

    # Transform raw data
    clean_data = extract_repository_data(data)

    # Save processed data
    save_processed_data(clean_data)

    # Display processed repositories
    print("\n📦 Top AI Repositories")
    print("=" * 80)

    for repo in clean_data:
        print(f"{repo['repository']} ({repo['stars']} ⭐)")


if __name__ == "__main__":
    main()
