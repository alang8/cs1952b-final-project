from consent_system import ConsentSystem
from database import Database
from facial_recognition import FacialRecognition
from feedback_system import FeedbackSystem

# This file is the entry point of the application, streamlining interactions between all components.
if __name__ == "__main__":
    db = Database()
    fr = FacialRecognition("path/to/model")
    consent_system = ConsentSystem(db)
    feedback_system = FeedbackSystem(db)

    # Example scenario of registering and verifying an attendee
    attendee_info = {'id': '001', 'name': 'John Doe', 'photo': 'photo_path_of_John'}
    consent_system.request_consent(attendee_info)

    # Entry verification at an event
    input_face = 'photo_path_of_John'
    if consent_system.check_compliance(attendee_info['id']):
        match_result = fr.match_face(input_face, db.attendees)
        if match_result:
            print(f"Welcome, {db.attendees[match_result]['name']}!")
        else:
            print("Face match failed. Entry denied.")
    else:
        print("No valid consent. Entry denied.")

    # Feedback reception
    feedback_system.receive_feedback('001', "The entry process was smooth and respectful.")

