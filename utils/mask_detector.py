from tensorflow.keras.models import load_model
import numpy as np
import cv2

model = load_model(
    "models/face_mask_detector.h5"
)

def detect_mask(face_frame):

    resized = cv2.resize(
        face_frame,
        (224, 224)
    )

    resized = resized / 255.0

    resized = np.expand_dims(
        resized,
        axis=0
    )

    prediction = model.predict(
        resized
    )[0]

    if prediction[0] > prediction[1]:
        return "Mask"

    else:
        return "No Mask"