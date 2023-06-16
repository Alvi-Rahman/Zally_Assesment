"""
github_event_analyzer.py

A Python module providing an EventAnalyzer base class.

This module contains the `EventAnalyzer` class, which serves as a base class for implementing event analysis functionality.
Specific event analyzers should inherit from this class and implement the abstract methods according to their specific requirements.

Author: Takrim Rahman Albi

"""


class EventAnalyzer:
    """
    A base class for implementing event analysis functionality.

    This class defines abstract methods that should be implemented by specific event analyzer subclasses.

    Methods:
        display_events(events):
            Displays the events in a specific format.
            Args:
                events (list): The list of events to be displayed.

        filter_events(events, event_type):
            Filters the events based on the specified event type.
            Args:
                events (list): The list of events to be filtered.
                event_type (str): The type of events to be included in the filter.

        calculate_event_statistics(events):
            Calculates statistics based on the provided events.
            Args:
                events (list): The list of events to be used for calculating statistics.

        identify_most_active_user(events):
            Identifies the most active user based on the provided events.
            Args:
                events (list): The list of events to be analyzed.

    """

    def display_events(self, events):
        """
        Displays the events in a specific format.

        This method should be implemented in the child class.

        Args:
            events (list): The list of events to be displayed.

        Raises:
            NotImplementedError: If the method is not implemented in the child class.
        """
        raise NotImplementedError("display_events() method must be implemented in child class")

    def filter_events(self, events, event_type):
        """
        Filters the events based on the specified event type.

        This method should be implemented in the child class.

        Args:
            events (list): The list of events to be filtered.
            event_type (str): The type of events to be included in the filter.

        Raises:
            NotImplementedError: If the method is not implemented in the child class.
        """
        raise NotImplementedError("filter_events() method must be implemented in child class")

    def calculate_event_statistics(self, events):
        """
        Calculates statistics based on the provided events.

        This method should be implemented in the child class.

        Args:
            events (list): The list of events to be used for calculating statistics.

        Raises:
            NotImplementedError: If the method is not implemented in the child class.
        """
        raise NotImplementedError("calculate_event_statistics() method must be implemented in child class")

    def identify_most_active_user(self, events):
        """
        Identifies the most active user based on the provided events.

        This method should be implemented in the child class.

        Args:
            events (list): The list of events to be analyzed.

        Raises:
            NotImplementedError: If the method is not implemented in the child class.
        """
        raise NotImplementedError("identify_most_active_user() method must be implemented in child class")
