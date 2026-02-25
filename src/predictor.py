import cv2
import numpy as np
import os
from tensorflow.keras.models import load_model
from src.config import MODEL_PATH, IMG_SIZE, EMOTIONS

model = None

if os.path.exists(MODEL_PATH):
    try:
        model = load_model(MODEL_PATH)
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")
else:
    print(f"Warning: Model not found at {MODEL_PATH}. Please run src/train.py first.")

def predict_face(gray_face):
    if model is None:
        return "Model Missing", np.zeros(len(EMOTIONS))

    face = cv2.resize(gray_face, (IMG_SIZE, IMG_SIZE))
    face = face / 255.0
    face = face.reshape(1, IMG_SIZE, IMG_SIZE, 1)

    pred = model.predict(face, verbose=0)[0]
    
    emotion = EMOTIONS[np.argmax(pred)]

    return emotion, pred
