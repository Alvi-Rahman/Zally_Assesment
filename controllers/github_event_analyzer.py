from controllers.base.github_api import GitHubAPI
from controllers.base.event_analyzer import EventAnalyzer
from utils.custom_exception import InvalidInputException


class GitHubEventsAnalyzer(GitHubAPI, EventAnalyzer):
    def fetch_events(self, repo_owner, repo_name, page=1):
        endpoint = ""
        if repo_owner and not repo_name:
            raise InvalidInputException("Both Repo Owner and Repo Name is required!")
        elif not repo_owner and repo_name:
            raise InvalidInputException("Both Repo Owner and Repo Name is required!")
        elif repo_owner and repo_name:
            endpoint = f"repos/{repo_owner}/{repo_name}/"

        endpoint += f"events?page={page}"
        return self.fetch(endpoint)

    def display_events(self, events):
        for event in events:
            print(f"Event: {event['type']}")
            print(f"User: {event['actor']['login']}")
            print(f"Timestamp: {event['created_at']}")
            print("-------------------------------------------")

    def filter_events(self, events, event_type):
        filtered_events = [event for event in events if event['type'] == event_type]
        return filtered_events

    def calculate_event_statistics(self, events):
        event_counts = {}
        for event in events:
            event_type = event['type']
            event_counts[event_type] = event_counts.get(event_type, 0) + 1
        return event_counts

    def identify_most_active_user(self, events):
        user_counts = {}
        for event in events:
            username = event['actor']['login']
            user_counts[username] = user_counts.get(username, 0) + 1

        most_active_user = max(user_counts, key=user_counts.get)
        return most_active_user


class GitHubEventsAnalyzerCLI(GitHubEventsAnalyzer):
    def fetch_and_display_events(self, repo_owner, repo_name, event_type=None, page=1, sort_order='chronological'):
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

