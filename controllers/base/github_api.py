import requests


class GitHubAPI:
    def __init__(self, base_url="https://api.github.com"):
        self.base_url = base_url

    def fetch(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch data from {url}. Error: {response.text}")
