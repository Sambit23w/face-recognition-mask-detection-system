import cv2
import mysql.connector
import pyttsx3

from datetime import datetime

from utils.recognition import recognize_face
from utils.mask_detector import detect_mask

engine = pyttsx3.init()

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="face_detection_system"
)

cursor = connection.cursor()

cam = cv2.VideoCapture(0)

cam.set(3, 640)
cam.set(4, 480)

while True:

    ret, frame = cam.read()

    small_frame = cv2.resize(
        frame,
        (0, 0),
        fx=0.5,
        fy=0.5
    )

    boxes, names = recognize_face(
        small_frame
    )

    for ((top, right, bottom, left), name) in zip(
        boxes,
        names
    ):

        top *= 2
        right *= 2
        bottom *= 2
        left *= 2

        face = frame[
            top:bottom,
            left:right
        ]

        try:

            mask_status = detect_mask(face)

        except:

            mask_status = "Unknown"

        color = (0, 255, 0)

        if mask_status == "No Mask":

            color = (0, 0, 255)

            engine.say(
                "Please wear mask"
            )

            engine.runAndWait()

        cv2.rectangle(
            frame,
            (left, top),
            (right, bottom),
            color,
            2
        )

        text = f"{name} - {mask_status}"

        cv2.putText(
            frame,
            text,
            (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            color,
            2
        )

        if name == "Unknown":

            cv2.imwrite(
                f"screenshots/{datetime.now().timestamp()}.jpg",
                frame
            )

        cursor.execute(
            '''
            INSERT INTO attendance_logs(
                person_name,
                mask_status
            )
            VALUES(%s,%s)
            ''',
            (name, mask_status)
        )

        connection.commit()

    cv2.imshow(
        "Face Recognition + Mask Detection",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()

cv2.destroyAllWindows()