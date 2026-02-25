import pyttsx3
import threading
from src.config import VOICE_RESPONSES, VOICE_RATE, VOICE_VOLUME, PREFERRED_VOICE_GENDER

# Initialize engine
engine = pyttsx3.init()

def setup_voice():
    """Setup voice properties, preferring female/Indian voices."""
    try:
        engine.setProperty('rate', VOICE_RATE)
        engine.setProperty('volume', VOICE_VOLUME)
        
        voices = engine.getProperty('voices')
        selected_voice = None
        
        # Try to find a female Indian voice or any female voice
        for voice in voices:
            v_name = voice.name.lower()
            if PREFERRED_VOICE_GENDER in v_name:
                selected_voice = voice.id
                # Indian English voices often sound better for Hindi than US/UK ones if native Hindi is missing
                if 'india' in v_name or 'heera' in v_name or 'veena' in v_name:
                    selected_voice = voice.id
                    break
        
        if selected_voice:
            engine.setProperty('voice', selected_voice)
    except Exception as e:
        print(f"Voice setup error: {e}")

setup_voice()
last_emotion = ""

def _speak_thread(text):
    """Function to run in a separate thread."""
    try:
        engine.say(text)
        engine.runAndWait() 
    except Exception:
        pass

def speak(emotion):
    global last_emotion
    if emotion != last_emotion:
        last_emotion = emotion
        # Get Hindi response from config
        text = VOICE_RESPONSES.get(emotion, f"Aap {emotion} lag rahe hain.")
        
        # Run in a separate thread to avoid blocking the main UI loop
        thread = threading.Thread(target=_speak_thread, args=(text,))
        thread.daemon = True
        thread.start()
