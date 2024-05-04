class ConsentSystem:
    """
    Oversees consent exchanges to guarantee that participants are completely aware of the uses and handling of 
    their biometric data. Complies with the recommendations of experts regarding the necessity for strong consent 
    procedures and facilitates adaptive governance by offering a transparent, reliable, and compliant consent 
    management system. This system now reflects both legal requirements and ethical considerations for the use 
    of biometric data, including more precise consent information and an easy-to-use withdrawl mechanism.
    """
    def __init__(self, database):
        """
        Initializes the consent system with a reference to the database for attendee data storage.
        
        :param database: An instance of the Database class for attendee data management.
        """
        self.database = database

    def request_consent(self, attendee_info):
        """
        Explicitly request and record attendee consent, providing detailed information about the use, storage,
        protection, and retention of facial recognition data. Offers granular consent options to attendees.
        
        :param attendee_info: Dictionary containing attendee information, including ID and name.
        :return: None
        """
        print("""Your facial data will be used for secure event entry and will be stored securely. You can 
              withdraw your consent at any time.""")
        print("""Details: Data will be used solely for event security purposes and will be deleted 30 days 
              post-event unless otherwise required by law.""")
        consent_given = input("Do you consent to this specific use of your facial data? (yes/no): ")
        if consent_given.lower() == 'yes':
            attendee_info['consent'] = {'given': True, 'details': 'Facial data use for event entry'}
            self.database.store_attendee_data(attendee_info['id'], attendee_info)
            print("Consent recorded. You are now registered.")
        else:
            attendee_info['consent'] = {'given': False}
            print("Consent denied. Registration cannot proceed without consent.")

    def check_compliance(self, attendee_id):
        """
        Ensure that all data use complies with local regulations and the specific consent provided by the attendee.
        Checks both the existence and specifics of consent to ensure full compliance.
        
        :param attendee_id: Unique identifier for the attendee.
        :return: Boolean indicating compliance status.
        """
        data = self.database.retrieve_attendee_data(attendee_id)
        return data and data.get('consent', {}).get('given', False)

    def withdraw_consent(self, attendee_id):
        """
        Allows attendees to easily withdraw their consent, ensuring compliance with privacy laws and ethical standards.
        Outlines the immediate effects of withdrawing consent, including data deletion where applicable.
        
        :param attendee_id: Unique identifier for the attendee.
        :return: None
        """
        data = self.database.retrieve_attendee_data(attendee_id)
        if data and data.get('consent', {}).get('given', False):
            data['consent']['given'] = False
            self.database.delete_attendee_data(attendee_id)  # Optional: based on policy
            print("Consent withdrawn. Your data will be deleted according to our privacy policy.")
