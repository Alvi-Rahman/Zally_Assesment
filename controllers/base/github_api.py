"""
github_api.py

A Python module providing a wrapper for the GitHub API.

This module contains the `GitHubAPI` class, which allows fetching data from various endpoints of the GitHub API.

Author: Takrim Rahman Albi

"""

import requests


class GitHubAPI:
    """
    A Python wrapper for the GitHub API.

    This class provides methods to interact with the GitHub API and fetch data from various endpoints.

    Attributes:
        base_url (str): The base URL of the GitHub API.

    Methods:
        __init__(base_url="https://api.github.com"):
            Initializes a new instance of the GitHubAPI class.
            Args:
                base_url (str, optional): The base URL of the GitHub API. Defaults to "https://api.github.com".

        fetch(endpoint):
            Fetches data from the specified API endpoint.
            Args:
                endpoint (str): The API endpoint to fetch data from.
            Returns:
                dict: The JSON response received from the API endpoint.
            Raises:
                Exception: If the API request fails or returns a non-200 status code.

    Example Usage:
        # Create an instance of GitHubAPI
        api = GitHubAPI()

        # Fetch data from a specific API endpoint
        events = api.fetch("repos/owner/repo/events")

        # Process the fetched data
        for event in events:
            # Perform actions on each event
            print(event)

    """

    def __init__(self, base_url="https://api.github.com"):
        """
        Initializes a new instance of the GitHubAPI class.

        Args:
            base_url (str, optional): The base URL of the GitHub API. Defaults to "https://api.github.com".
        """
        self.base_url = base_url

    def fetch(self, endpoint):
        """
        Fetches data from the specified API endpoint.

        Args:
            endpoint (str): The API endpoint to fetch data from.

        Returns:
            dict: The JSON response received from the API endpoint.

        Raises:
            Exception: If the API request fails or returns a non-200 status code.
        """
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch data from {url}. Error: {response.text}")
