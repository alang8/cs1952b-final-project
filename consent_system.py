class ConsentSystem:
    def __init__(self, database):
        self.database = database

    def request_consent(self, attendee_info):
        # Provide details about data use and consent withdrawal
        print("Your facial data will be used for secure event entry. You can withdraw consent at any time.")
        consent_given = input("Do you consent to this use of your data? (yes/no): ")
        if consent_given.lower() == 'yes':
            attendee_info['consent'] = True
            self.database.store_attendee_data(attendee_info['id'], attendee_info)
            print("Consent recorded. You are now registered.")
        else:
            attendee_info['consent'] = False
            print("Consent denied. Registration cannot proceed without consent.")

    def check_compliance(self, attendee_id):
        # Check if the use of data complies with local regulations
        data = self.database.retrieve_attendee_data(attendee_id)
        return data and data.get('consent', False)
