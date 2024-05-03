class Database:
    def __init__(self):
        self.attendees = {}  # Stores attendee data including consent and face data

    def store_attendee_data(self, attendee_id, data):
        self.attendees[attendee_id] = data

    def retrieve_attendee_data(self, attendee_id):
        return self.attendees.get(attendee_id, None)

    def delete_attendee_data(self, attendee_id):
        if attendee_id in self.attendees:
            del self.attendees[attendee_id]
