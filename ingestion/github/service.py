import requests


def fetch_github_data():
    """
    Fetch AI repositories from the GitHub Search API.
    Returns a Python dictionary if successful.
    Returns None if the request fails.
    """

    url = (
        "https://api.github.com/search/repositories"
        "?q=topic:artificial-intelligence"
        "&sort=stars"
        "&order=desc"
    )

    print("🚀 Fetching GitHub data...")

    response = requests.get(url)

    if response.status_code == 200:
        print("✅ GitHub data fetched successfully!")
        return response.json()

    print(f"❌ Error: {response.status_code}")
    return None
