import cv2
import os
import mysql.connector

name = input("Enter User Name: ")

path = f"datasets/known_faces/{name}"

os.makedirs(path, exist_ok=True)

cam = cv2.VideoCapture(0)

count = 0

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="face_detection_system"
)

cursor = connection.cursor()

while True:

    ret, frame = cam.read()

    cv2.imshow("Capture Images", frame)

    file_name = f"{path}/{count}.jpg"

    cv2.imwrite(file_name, frame)

    count += 1

    if count == 50:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cursor.execute(
    "INSERT INTO users(name, image_path) VALUES(%s,%s)",
    (name, path)
)

connection.commit()

cam.release()

cv2.destroyAllWindows()

print("User Registered Successfully")