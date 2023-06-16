class EventAnalyzer:
    def display_events(self, events):
        raise NotImplementedError("display_events() method must be implemented in child class")

    def filter_events(self, events, event_type):
        raise NotImplementedError("filter_events() method must be implemented in child class")

    def calculate_event_statistics(self, events):
        raise NotImplementedError("calculate_event_statistics() method must be implemented in child class")

    def identify_most_active_user(self, events):
        raise NotImplementedError("identify_most_active_user() method must be implemented in child class")
