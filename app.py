import streamlit as st
import cv2
import pandas as pd
import numpy as np
from PIL import Image
import os

try:
    from src.webcam import get_faces
    from src.predictor import predict_face
    from src.smoothing import EmotionSmoother
    from src.voice import speak
    from src.config import EMOTIONS, EMOTIONS_HI
except ImportError as e:
    st.error(f"Error importing modules: {e}")
    st.stop()

# Page configuration
st.set_page_config(
    layout="wide", 
    page_title="AI Emotion Detection | Future UI",
    page_icon="🧠",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Premium UI
st.markdown("""
<style>
    /* Import Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Orbitron:wght@400;700&display=swap');

    /* Global styles */
    :root {
        --primary-glow: #00f2fe;
        --secondary-glow: #4facfe;
        --glass-bg: rgba(255, 255, 255, 0.05);
        --glass-border: rgba(255, 255, 255, 0.1);
    }

    .stApp {
        background: radial-gradient(circle at top right, #0a0e17, #000000);
        font-family: 'Inter', sans-serif;
        color: #ffffff;
    }

    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Header Styling */
    .main-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 3rem;
        background: linear-gradient(90deg, #00f2fe, #4facfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding-top: 2rem;
        margin-bottom: 0.5rem;
        letter-spacing: 2px;
    }
    
    .subtitle {
        text-align: center;
        color: #a0a0a0;
        margin-bottom: 3rem;
        font-weight: 300;
        font-size: 1.1rem;
    }

    /* Glassmorphism Cards */
    .glass-card {
        background: var(--glass-bg);
        backdrop-filter: blur(10px);
        border: 1px solid var(--glass-border);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }

    /* Emotion Labels */
    .emotion-tag {
        display: inline-block;
        padding: 5px 15px;
        border-radius: 30px;
        background: linear-gradient(45deg, #00f2fe, #4facfe);
        color: black;
        font-weight: 600;
        margin-top: 10px;
        font-family: 'Orbitron', sans-serif;
        font-size: 1.2rem;
    }

    /* Customizing sidebar */
    .stSidebar {
        background: rgba(10, 14, 23, 0.95);
        border-right: 1px solid var(--glass-border);
    }

    /* Hide horizontal deployment banner */
    .st-emotion-cache-18ni7ve { display: none; }
    
    /* Responsive Adjustments */
    @media (max-width: 768px) {
        .main-title { font-size: 2rem; }
    }
</style>
""", unsafe_allow_html=True)

# App Title & Subtitle
st.markdown('<h1 class="main-title">AI EMOTION ENGINE</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Experience Real-time Sentiment Intelligence</p>', unsafe_allow_html=True)

# Sidebar settings with Lucide icons (simulated in text)
st.sidebar.markdown("""
<div style='text-align: center; padding: 20px;'>
    <h3 style='font-family: Orbitron; color: #00f2fe;'>CONTROL CENTER</h3>
</div>
""", unsafe_allow_html=True)

voice_on = st.sidebar.toggle("🔊 Voice Feedback (Hindi)", value=True)
show_stats = st.sidebar.toggle("📊 Show Analytics", value=True)
sensitivity = st.sidebar.slider("⚙️ Smoothing Value", 1, 15, 8)

# Initialize smoother with user sensitivity
smoother = EmotionSmoother(size=sensitivity)

# Main layout using columns
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("📷 Vision Analytics")
    
    tab1, tab2 = st.tabs(["Webcam Live", "Image Upload"])
    
    with tab1:
        run = st.checkbox("Initialize Engine", value=False)
        frame_window = st.image([])
        
    with tab2:
        uploaded = st.file_uploader("Drop Image Here", type=['jpg', 'png', 'jpeg'])
        if uploaded:
            img = Image.open(uploaded)
            frame = np.array(img)
            frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            st.image(frame, caption="Uploaded Data")

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("🧠 Detected Insight")
    
    emotion_display = st.empty()
    hindi_display = st.empty()
    prob_display = st.empty()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Emotion Icon Mapping
EMOTION_ICONS = {
    'Happy': '😊', 'Sad': '😢', 'Angry': '😠', 
    'Fear': '😨', 'Disgust': '🤢', 'Surprise': '😲', 'Neutral': '😐'
}

# Detection Logic
if run:
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Error: Could not access camera.")
    else:
        while run:
            ret, frame = cap.read()
            if not ret: break
            
            gray, faces = get_faces(frame)
            
            for (x, y, w, h) in faces:
                face = gray[y:y+h, x:x+w]
                emotion, prob = predict_face(face)
                
                # Smooth the result
                smooth_emotion = smoother.update(emotion)
                hindi_emotion = EMOTIONS_HI.get(smooth_emotion, "Pata Nahi")
                
                # Update UI
                icon = EMOTION_ICONS.get(smooth_emotion, "❓")
                emotion_display.markdown(f"### Current: **{smooth_emotion}** {icon}")
                hindi_display.markdown(f"<div class='emotion-tag'>{hindi_emotion}</div>", unsafe_allow_html=True)
                
                if show_stats:
                    df = pd.DataFrame(prob, index=EMOTIONS, columns=["Confidence"])
                    prob_display.bar_chart(df, height=200)

                if voice_on:
                    speak(smooth_emotion)

                # Visual rectangle
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 242, 254), 2)
                cv2.putText(frame, smooth_emotion, (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 242, 254), 2)

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_window.image(frame_rgb)
            
        cap.release()

elif uploaded:
    # Process uploaded image
    gray, faces = get_faces(frame_bgr)
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]
            emotion, prob = predict_face(face)
            
            hindi_emotion = EMOTIONS_HI.get(emotion, "Pata Nahi")
            icon = EMOTION_ICONS.get(emotion, "❓")
            
            emotion_display.markdown(f"### Result: **{emotion}** {icon}")
            hindi_display.markdown(f"<div class='emotion-tag'>{hindi_emotion}</div>", unsafe_allow_html=True)
            
            if show_stats:
                df = pd.DataFrame(prob, index=EMOTIONS, columns=["Confidence"])
                prob_display.bar_chart(df)
            
            if voice_on:
                speak(emotion)
    else:
        st.warning("No faces identified in the image.")
