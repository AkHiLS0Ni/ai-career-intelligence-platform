import json
from service import fetch_github_data


def save_raw_data(data):
    """
    Save raw GitHub API response to a JSON file.
    """

    with open("data/raw/github/github_api.json", "w") as file:
        json.dump(data, file, indent=4)

    print("✅ Raw data saved successfully!")


def main():
    """
    Main entry point of the GitHub ingestion pipeline.
    """

    data = fetch_github_data()

    if data is None:
        return

    save_raw_data(data)

    print("\n📦 Top AI Repositories")
    print("=" * 80)

    for repo in data["items"]:
        print(f"{repo['name']} ({repo['stargazers_count']} ⭐)")


if __name__ == "__main__":
    main()
