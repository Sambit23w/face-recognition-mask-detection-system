import face_recognition
import pickle
import cv2

with open(
    "models/encodings.pickle",
    "rb"
) as file:

    data = pickle.load(file)

def recognize_face(frame):

    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    boxes = face_recognition.face_locations(rgb)

    encodings = face_recognition.face_encodings(
        rgb,
        boxes
    )

    names = []

    for encoding in encodings:

        matches = face_recognition.compare_faces(
            data["encodings"],
            encoding
        )

        name = "Unknown"

        if True in matches:

            matched_indexes = [
                i for (i, b)
                in enumerate(matches)
                if b
            ]

            counts = {}

            for i in matched_indexes:

                name = data["names"][i]

                counts[name] = counts.get(
                    name,
                    0
                ) + 1

            name = max(
                counts,
                key=counts.get
            )

        names.append(name)

    return boxes, names