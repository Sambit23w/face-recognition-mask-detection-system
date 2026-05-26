import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="face_detection_system"
)

cursor = connection.cursor()