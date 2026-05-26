from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="face_detection_system"
)

cursor = connection.cursor(
    dictionary=True
)

@app.route('/')
def dashboard():

    cursor.execute(
        '''
        SELECT *
        FROM attendance_logs
        ORDER BY created_at DESC
        '''
    )

    logs = cursor.fetchall()

    total_logs = len(logs)

    return render_template(
        'index.html',
        logs=logs,
        total_logs=total_logs
    )

@app.route('/users')
def users():

    cursor.execute(
        'SELECT * FROM users'
    )

    users = cursor.fetchall()

    return render_template(
        'users.html',
        users=users
    )

@app.route('/attendance')
def attendance():

    cursor.execute(
        '''
        SELECT *
        FROM attendance_logs
        ORDER BY created_at DESC
        '''
    )

    logs = cursor.fetchall()

    return render_template(
        'attendance.html',
        logs=logs
    )

if __name__ == '__main__':

    app.run(debug=True)