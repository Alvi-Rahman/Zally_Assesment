"""
GitHub Events API Analyzer

This module contains the GitHubEventAnalyzer class that serves as the entry point for Even Analysis process.

Classes:
- GitHubEventAnalyzer

"""
import argparse

from controllers.event_analyzer import GitHubEventsAnalyzerCLI
from utils.custom_exception import InvalidInputException


class GitHubEventAnalyzer:
    """
    GitHubEventAnalyzer serves as the entry point for the Analysis process.

    Methods:
        event_analyzer_entry_point():
            Executes the privacy policy word counting process.

    """

    @staticmethod
    def event_analyzer_entry_point(owner, repo, event_type, page, sort_order):
        """
        Executes the process.

        Returns:
            None

        """
        event_controller = GitHubEventsAnalyzerCLI()
        event_controller.fetch_and_display_events(owner, repo, event_type, page, sort_order)


if __name__ == "__main__":
    """
    Entry point of the Zally Github API Analyzer.
    """

    parser = argparse.ArgumentParser(description="GitHub Events API Analyzer")
    parser.add_argument("--owner", help="GitHub repository owner")
    parser.add_argument("--repo", help="GitHub repository name")
    parser.add_argument("--event_type", default=None, help="Filter events by type")
    parser.add_argument("--page", type=int, default=1, help="Page number for pagination")
    parser.add_argument(
        "--sort_order", choices=["chronological", "reverse-chronological"], default="chronological",
        help="Sort order for events"
    )
    args = parser.parse_args()

    try:
        analyzer = GitHubEventAnalyzer()
        analyzer.event_analyzer_entry_point(args.owner, args.repo, args.event_type, args.page, args.sort_order)
    except InvalidInputException as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
