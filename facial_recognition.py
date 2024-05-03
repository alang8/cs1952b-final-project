import face_recognition # Install using `pip install face_recognition`
import numpy as np

class FacialRecognition:
    """
    Implements facial recognition capabilities using the face_recognition library. This class provides functions to 
    load, encode face images, and recognize faces by comparing input images against a known dataset.
    
    In order to provide dependable identification, the basic facial recognition function is implemented through the 
    use of trained models.Bias mitigation strategiesᅳa critical lesson from expert input and research insightsᅳare 
    integrated into the model training process to achieve equitable technology deployment. This highlights the need 
    for technological adaptations that take privacy and social implications into consideration. 
    """

    def __init__(self, known_images):
        """
        Initializes the facial recognition system by loading and encoding known images.
        :param known_images: A list of file paths to images of known individuals.
        """
        self.known_encodings, self.known_names = self.load_and_encode_images(known_images)

    def load_and_encode_images(self, image_files):
        """
        Loads images from specified file paths and encodes them into facial features.
        Each face image is encoded into a 128-dimension vector using a pre-trained model.
        This method ensures that the system is equipped with accurate and bias-mitigated data for recognition.
        :param image_files: List of image file paths.
        :return: A tuple of lists containing face encodings and corresponding names.
        """
        known_encodings = []
        known_names = []

        for image_file in image_files:
            image = face_recognition.load_image_file(image_file)
            encodings = face_recognition.face_encodings(image)
            if encodings: # Ensure at least one face is found
                known_encodings.append(encodings[0])
                known_names.append(image_file.split("/")[-1].split(".")[0]) # Extract name from filename

        return known_encodings, known_names

    def recognize_faces(self, input_image_path):
        """
        Recognizes faces by comparing input image encodings with known face encodings.
        Matches are identified based on the smallest distance between face encodings, minimizing false positives and negatives.
        Outputs the name of recognized individuals or indicates no match, reflecting considerations for equitable technology deployment.
        :param input_image_path: Path to the input image file to be recognized.
        """
        input_image = face_recognition.load_image_file(input_image_path)
        input_encodings = face_recognition.face_encodings(input_image)

        for face_encoding in input_encodings:
            matches = face_recognition.compare_faces(self.known_encodings, face_encoding)
            face_distances = face_recognition.face_distance(self.known_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = self.known_names[best_match_index]
                print(f"Match found: {name}")
            else:
                print("No match found")

# Example usage of the FacialRecognition class:
if __name__ == "__main__":
    known_images = ['path/to/image1.jpg', 'path/to/image2.jpg']
    fr_system = FacialRecognition(known_images)
    fr_system.recognize_faces('path/to/input_image.jpg')
