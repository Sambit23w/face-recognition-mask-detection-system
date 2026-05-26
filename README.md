# Face Recognition + Mask Detection System

## Developed By
Sambit Pattanaik

GitHub Repository:  
https://github.com/Sambit23w/face-recognition-mask-detection-system

---

# Project Overview

This is a real-time AI-based Face Recognition and Mask Detection System developed using:

- Python
- OpenCV
- TensorFlow
- Flask
- MySQL
- face_recognition
- Keras

The system can:
- Detect human faces
- Recognize registered users
- Detect Mask / No Mask
- Store attendance logs in MySQL
- Show attendance records in Flask Dashboard
- Trigger voice alerts for no-mask detection

---

# Features

## Face Recognition
- Real-time face detection
- Multi-user recognition
- Unknown face detection

## Mask Detection
- Detects Mask / No Mask
- TensorFlow + Keras based model

## Flask Dashboard
- Attendance logs
- User records
- Database visualization

## MySQL Integration
- Stores users
- Stores attendance logs

## Voice Alert
- Alerts user when mask is not detected

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main Programming Language |
| OpenCV | Image Processing |
| TensorFlow | AI/ML Model |
| Keras | Deep Learning |
| Flask | Dashboard |
| MySQL | Database |
| face_recognition | Face Recognition |
| pyttsx3 | Voice Alerts |

---

# Minimum System Requirements

| Component | Minimum Requirement |
|-----------|--------------------|
| OS | Windows 10 |
| RAM | 4 GB |
| Processor | Intel i3 / Ryzen 3 |
| Storage | 10 GB Free Space |
| Python | Python 3.10 |
| Webcam | Required |
| Internet | Required for package installation |

---

# Recommended System Requirements

| Component | Recommended |
|-----------|--------------|
| OS | Windows 10/11 |
| RAM | 8 GB or Higher |
| Processor | Intel i5 / Ryzen 5 |
| Storage | SSD Recommended |
| GPU | Optional NVIDIA GPU |
| Python | Python 3.10.11 |
| Webcam | HD Webcam Recommended |

---

# Project Folder Structure

```bash
face_recognition_mask_detection/
│
├── datasets/
│   ├── known_faces/
│   └── unknown_faces/
│
├── models/
│   ├── face_mask_detector.h5
│   └── encodings.pickle
│
├── database/
│   └── db_connection.py
│
├── utils/
│   ├── face_encoding.py
│   ├── recognition.py
│   └── mask_detector.py
│
├── templates/
│   ├── index.html
│   ├── users.html
│   └── attendance.html
│
├── static/
├── screenshots/
├── logs/
│
├── app.py
├── main.py
├── register_user.py
├── requirements.txt
└── README.md
```

---

# Step-by-Step Setup Guide

---

# Step 1 — Install Python

Download Python 3.10.11:

https://www.python.org/downloads/release/python-31011/

During installation:
- Check "Add Python to PATH"

Verify installation:

```bash
python --version
```

Expected:

```bash
Python 3.10.11
```

---

# Step 2 — Install MySQL

Download MySQL Community Server:

https://dev.mysql.com/downloads/mysql/

Verify:

```bash
mysql --version
```

---

# Step 3 — Install Git

Download Git:

https://git-scm.com/download/win

Verify:

```bash
git --version
```

---

# Step 4 — Clone Repository

```bash
git clone https://github.com/Sambit23w/face-recognition-mask-detection-system.git
```

---

# Step 5 — Enter Project Folder

```bash
cd face-recognition-mask-detection-system
```

---

# Step 6 — Create Virtual Environment

```bash
py -3.10 -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

# Step 7 — Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

# Step 8 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Step 9 — Install Compatible Versions

## TensorFlow

```bash
pip install tensorflow==2.10.1
```

## Keras

```bash
pip install keras==2.10.0
```

## NumPy

```bash
pip install numpy==1.23.5
```

## OpenCV

```bash
pip install opencv-python==4.7.0.72
```

---

# Step 10 — Install Visual Studio Build Tools

Required for:
- dlib
- face_recognition

Download:

https://visualstudio.microsoft.com/visual-cpp-build-tools/

Install:
- Desktop Development with C++

---

# Step 11 — Install dlib

```bash
pip install dlib
```

---

# Step 12 — Install face_recognition

```bash
pip install face_recognition
```

---

# Step 13 — Download Mask Detection Model

Download:

https://github.com/chandrikadeb7/Face-Mask-Detection

Copy model file into:

```bash
models/
```

Rename model to:

```bash
face_mask_detector.h5
```

---

# Step 14 — Create MySQL Database

Open MySQL:

```bash
mysql -u root -p
```

Run:

```sql
CREATE DATABASE face_detection_system;

USE face_detection_system;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    image_path VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE attendance_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    person_name VARCHAR(100),
    mask_status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# Step 15 — Configure MySQL Password

Update password inside:
- app.py
- main.py
- register_user.py
- database/db_connection.py

Replace:

```python
password="YOUR_PASSWORD"
```

with your actual MySQL password.

---

# Step 16 — Register User

```bash
python register_user.py
```

Enter user name:

```bash
Ruchika Panday
```

The webcam will capture face images.

---

# Step 17 — Generate Face Encodings

```bash
python utils/face_encoding.py
```

Expected Output:

```bash
Encoding Completed
```

This creates:

```bash
models/encodings.pickle
```

---

# Step 18 — Run Main Application

```bash
python main.py
```

Features:
- Webcam detection
- Face recognition
- Mask detection
- Voice alerts
- Database logging

---

# Step 19 — Run Flask Dashboard

Open new terminal:

```bash
venv\Scripts\activate
```

Run:

```bash
python app.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

# Troubleshooting

## TensorFlow Error

Install compatible versions:

```bash
pip install tensorflow==2.10.1
pip install keras==2.10.0
pip install numpy==1.23.5
```

---

## OpenCV Compatibility Error

```bash
pip install opencv-python==4.7.0.72
```

---

## dlib Installation Error

Install:
- Visual Studio Build Tools
- Desktop Development with C++

---

## Webcam Not Opening

Check:
- Camera permissions
- Webcam drivers
- Camera not used by another application

---

# Future Improvements

- Email Alerts
- Mobile Notifications
- Cloud Deployment
- JWT Authentication
- DeepFace Integration
- CCTV Integration

---

# License

This project is developed for:
- Educational Purposes
- Portfolio Projects
- AI/ML Learning

---

# Author

Sambit Pattanaik

GitHub:  
https://github.com/Sambit23w