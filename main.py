from consent_system import ConsentSystem
from database import Database
from facial_recognition import FacialRecognition
from feedback_system import FeedbackSystem
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    db = Database()
    fr = FacialRecognition("path/to/model")
    consent_system = ConsentSystem(db)
    feedback_system = FeedbackSystem(db)

    # Use a try-except block to handle potential exceptions
    try:
        # Example scenario of registering and verifying an attendee
        attendee_info = {'id': '001', 'name': 'John Doe', 'photo': 'photo_path_of_John'}
        consent_system.request_consent(attendee_info)

        # Entry verification at an event
        input_face = 'photo_path_of_John'
        if consent_system.check_compliance(attendee_info['id']):
            match_result = fr.match_face(input_face, db.attendees)
            if match_result:
                logging.info(f"Welcome, {db.attendees[match_result]['name']}!")
            else:
                logging.error("Face match failed. Entry denied.")
        else:
            logging.warning("No valid consent. Entry denied.")

        # Feedback reception
        feedback_system.receive_feedback('001', "The entry process was smooth and respectful.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        feedback_system.handle_complaints("A system error occurred during the entry process.")
