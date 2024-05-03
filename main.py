from consent_system import ConsentSystem
from database import Database
from facial_recognition import FacialRecognition
from feedback_system import FeedbackSystem

db = Database()
fr = FacialRecognition()
consent_system = ConsentSystem(db)
feedback_system = FeedbackSystem(db)

# Registering an attendee
attendee_info = {'id': '001', 'name': 'John Doe', 'photo': 'photo_path_of_John'}
consent_system.request_consent(attendee_info)

# At event entry, attempt to match face
input_face = 'photo_path_of_John'  # Simulated input for demonstration
if consent_system.check_compliance(attendee_info['id']):
    match_result = fr.match_face(input_face, db.attendees)
    if match_result:
        print(f"Welcome, {db.attendees[match_result]['name']}!")
    else:
        print("Face match failed. Entry denied.")
else:
    print("No valid consent. Entry denied.")

# Receiving feedback
feedback_system.receive_feedback('001', "The entry process was smooth and respectful.")
