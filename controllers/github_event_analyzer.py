"""
github_event_analyzer.py

A Python module providing the GitHubEventsAnalyzer and GitHubEventsAnalyzerCLI classes.

This module contains the `GitHubEventsAnalyzer` class, which is responsible for fetching GitHub events and performing event analysis.
It also includes the `GitHubEventsAnalyzerCLI` class, which extends the `GitHubEventsAnalyzer` functionality to provide a command-line interface.

Author: Takrim Rahman Albi
"""

from controllers.base.github_api import GitHubAPI
from controllers.base.event_analyzer import EventAnalyzer
from utils.custom_exception import InvalidInputException


class GitHubEventsAnalyzer(GitHubAPI, EventAnalyzer):
    """
    A class for fetching GitHub events and performing event analysis.

    This class inherits from GitHubAPI and EventAnalyzer, combining their functionality to analyze GitHub events.

    Methods:
        fetch_events(repo_owner, repo_name, page=1):
            Fetches GitHub events for the specified repository.
            Args:
                repo_owner (str): The owner of the repository.
                repo_name (str): The name of the repository.
                page (int): The page number of the events to fetch.
            Returns:
                list: The list of fetched events.

        display_events(events):
            Displays the provided events.
            Args:
                events (list): The list of events to be displayed.

        filter_events(events, event_type):
            Filters the provided events based on the specified event type.
            Args:
                events (list): The list of events to be filtered.
                event_type (str): The type of events to include in the filter.
            Returns:
                list: The filtered list of events.

        calculate_event_statistics(events):
            Calculates event statistics based on the provided events.
            Args:
                events (list): The list of events to be used for calculating statistics.
            Returns:
                dict: A dictionary containing event types as keys and their respective counts as values.

        identify_most_active_user(events):
            Identifies the most active user based on the provided events.
            Args:
                events (list): The list of events to be analyzed.
            Returns:
                str: The username of the most active user.

    """

    def fetch_events(self, repo_owner, repo_name, page=1):
        """
        Fetches GitHub events for the specified repository.

        Args:
            repo_owner (str): The owner of the repository.
            repo_name (str): The name of the repository.
            page (int): The page number of the events to fetch.

        Returns:
            list: The list of fetched events.

        Raises:
            InvalidInputException: If both repo_owner and repo_name are not provided.
        """
        endpoint = ""
        if repo_owner and not repo_name:
            raise InvalidInputException("Both Repo Owner and Repo Name are required!")
        elif not repo_owner and repo_name:
            raise InvalidInputException("Both Repo Owner and Repo Name are required!")
        elif repo_owner and repo_name:
            endpoint = f"repos/{repo_owner}/{repo_name}/"

        endpoint += f"events?page={page}"
        return self.fetch(endpoint)

    def display_events(self, events):
        """
        Displays the provided events.

        Args:
            events (list): The list of events to be displayed.
        """
        for event in events:
            print(f"Event: {event['type']}")
            print(f"User: {event['actor']['login']}")
            print(f"Timestamp: {event['created_at']}")
            print("-------------------------------------------")

    def filter_events(self, events, event_type):
        """
        Filters the provided events based on the specified event type.

        Args:
            events (list): The list of events to be filtered.
            event_type (str): The type of events to include in the filter.

        Returns:
            list: The filtered list of events.
        """
        filtered_events = [event for event in events if event['type'] == event_type]
        return filtered_events

    def calculate_event_statistics(self, events):
        """
        Calculates event statistics based on the provided events.

        Args:
            events (list): The list of events to be used for calculating statistics.

        Returns:
            dict: A dictionary containing event types as keys and their respective counts as values.
        """
        event_counts = {}
        for event in events:
            event_type = event['type']
            event_counts[event_type] = event_counts.get(event_type, 0) + 1
        return event_counts

    def identify_most_active_user(self, events):
        """
        Identifies the most active user based on the provided events.

        Args:
            events (list): The list of events to be analyzed.

        Returns:
            str: The username of the most active user.
        """
        user_counts = {}
        for event in events:
            username = event['actor']['login']
            user_counts[username] = user_counts.get(username, 0) + 1

        most_active_user = max(user_counts, key=user_counts.get)
        return most_active_user


class GitHubEventsAnalyzerCLI(GitHubEventsAnalyzer):
    """
    A class that extends GitHubEventsAnalyzer to provide a command-line interface for analyzing GitHub events.

    This class inherits from GitHubEventsAnalyzer and provides additional methods for fetching and displaying events
    along with event statistics.

    Methods:
        fetch_and_display_events(repo_owner, repo_name, event_type=None, page=1, sort_order='chronological'):
            Fetches GitHub events, filters them based on event type, and displays them along with event statistics.
            Args:
                repo_owner (str): The owner of the repository.
                repo_name (str): The name of the repository.
                event_type (str): The type of events to filter (optional).
                page (int): The page number of the events to fetch.
                sort_order (str): The sort order of the events ('chronological' or 'reverse-chronological').

    """

    def fetch_and_display_events(self, repo_owner, repo_name, event_type=None, page=1, sort_order='chronological'):
        """
        Fetches GitHub events, filters them based on event type, and displays them along with event statistics.

        Args:
            repo_owner (str): The owner of the repository.
            repo_name (str): The name of the repository.
            event_type (str): The type of events to filter (optional).
            page (int): The page number of the events to fetch.
            sort_order (str): The sort order of the events ('chronological' or 'reverse-chronological').
        """
        events = self.fetch_events(repo_owner, repo_name, page)
        if event_type:
            events = self.filter_events(events, event_type)

        if sort_order == 'reverse-chronological':
            events = sorted(events, key=lambda event: event['created_at'], reverse=True)
        else:
            events = sorted(events, key=lambda event: event['created_at'])

        self.display_events(events)

        event_statistics = self.calculate_event_statistics(events)
        print("Event Statistics:")
        for event_type, count in event_statistics.items():
            print(f"{event_type}: {count}")

        most_active_user = self.identify_most_active_user(events)
        print(f"Most Active User: {most_active_user}")

