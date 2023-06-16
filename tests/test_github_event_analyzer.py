import pytest
from unittest.mock import patch

from controllers.github_event_analyzer import GitHubEventsAnalyzer


class TestEventAnalyzerController:
    @pytest.fixture
    def event_controller(self):
        return GitHubEventsAnalyzer()

    @patch('requests.get')
    def test_fetch_events_success(self, mock_get, event_controller):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {'type': 'PushEvent', 'actor': {'login': 'user1'}, 'created_at': '2023-06-14T10:30:00Z'}]

        events = event_controller.fetch_events('user1', 'repo1')

        assert len(events) == 1
        assert events[0]['type'] == 'PushEvent'
        assert events[0]['actor']['login'] == 'user1'
        assert events[0]['created_at'] == '2023-06-14T10:30:00Z'

    def test_display_events(self, event_controller, capsys):
        events = [{'type': 'PushEvent', 'actor': {'login': 'user1'}, 'created_at': '2023-06-14T10:30:00Z'},
                  {'type': 'PullRequestEvent', 'actor': {'login': 'user2'}, 'created_at': '2023-06-14T11:30:00Z'}]

        event_controller.display_events(events)

        captured = capsys.readouterr()
        expected_output = ('Event: PushEvent\n'
                           'User: user1\n'
                           'Timestamp: 2023-06-14T10:30:00Z\n'
                           '-------------------------------------------\n'
                           'Event: PullRequestEvent\n'
                           'User: user2\n'
                           'Timestamp: 2023-06-14T11:30:00Z\n'
                           '-------------------------------------------\n')
        assert captured.out == expected_output

    def test_filter_events(self, event_controller):
        events = [{'type': 'PushEvent', 'actor': {'login': 'user1'}, 'created_at': '2023-06-14T10:30:00Z'},
                  {'type': 'PullRequestEvent', 'actor': {'login': 'user2'}, 'created_at': '2023-06-14T11:30:00Z'},
                  {'type': 'PushEvent', 'actor': {'login': 'user3'}, 'created_at': '2023-06-14T12:30:00Z'}]

        filtered_events = event_controller.filter_events(events, 'PushEvent')

        assert len(filtered_events) == 2
        assert filtered_events[0]['type'] == 'PushEvent'
        assert filtered_events[0]['actor']['login'] == 'user1'
        assert filtered_events[1]['type'] == 'PushEvent'
        assert filtered_events[1]['actor']['login'] == 'user3'

    def test_calculate_event_statistics(self, event_controller):
        events = [{'type': 'PushEvent'}, {'type': 'PullRequestEvent'}, {'type': 'PushEvent'}]

        event_counts = event_controller.calculate_event_statistics(events)

        assert event_counts.get('PushEvent') == 2
        assert event_counts.get('PullRequestEvent') == 1

    def test_identify_most_active_user(self, event_controller):
        events = [{'type': 'PushEvent', 'actor': {'login': 'user1'}},
                  {'type': 'PullRequestEvent', 'actor': {'login': 'user2'}},
                  {'type': 'PushEvent', 'actor': {'login': 'user1'}}]

        user_counts = event_controller.identify_most_active_user(events)

        assert user_counts == 'user1'
