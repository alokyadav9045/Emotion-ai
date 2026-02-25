import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Navigate up from src/ to root, then to models/
MODEL_PATH = os.path.join(BASE_DIR, "../models/emotion_model.h5")

EMOTIONS = [
    'Angry', 'Disgust', 'Fear',
    'Happy', 'Neutral', 'Sad', 'Surprise'
]

# Hindi translations for Indian context
EMOTIONS_HI = {
    'Angry': 'Gussa',
    'Disgust': 'Ghrina',
    'Fear': 'Darr',
    'Happy': 'Khushi',
    'Neutral': 'Shaant',
    'Sad': 'Dukhi',
    'Surprise': 'Hairani'
}

# Voice responses in Hindi
VOICE_RESPONSES = {
    'Angry': 'Aap gussa lag rahe hain, shaant ho jaiye.',
    'Disgust': 'Aap ghrina mahsoos kar rahe hain.',
    'Fear': 'Aap dare hue lag rahe hain, sab theek hai.',
    'Happy': 'Aap bahut khush dikh rahe hain, accha laga!',
    'Neutral': 'Aap bilkul shaant lag rahe hain.',
    'Sad': 'Aap dukhi lag rahe hain, himmat rakhiye.',
    'Surprise': 'Aap kaafi hairan lag rahe hain!'
}

IMG_SIZE = 48
SMOOTH_WINDOW = 8

# Voice Settings
VOICE_RATE = 150
VOICE_VOLUME = 1.0
PREFERRED_VOICE_GENDER = 'female'
