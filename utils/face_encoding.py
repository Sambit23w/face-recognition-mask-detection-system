import face_recognition
import pickle
import cv2
import os

known_encodings = []
known_names = []

base_path = "datasets/known_faces"

for person_name in os.listdir(base_path):

    person_folder = os.path.join(base_path, person_name)

    for image_name in os.listdir(person_folder):

        image_path = os.path.join(
            person_folder,
            image_name
        )

        image = cv2.imread(image_path)

        rgb = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2RGB
        )

        boxes = face_recognition.face_locations(rgb)

        encodings = face_recognition.face_encodings(
            rgb,
            boxes
        )

        for encoding in encodings:

            known_encodings.append(encoding)

            known_names.append(person_name)

print("Encoding Completed")

data = {
    "encodings": known_encodings,
    "names": known_names
}

with open(
    "models/encodings.pickle",
    "wb"
) as file:

    pickle.dump(data, file)