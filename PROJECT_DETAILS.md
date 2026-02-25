# 🧠 AI Emotion Detection System - Technical Deep Dive

## 📘 Overview
This project is a high-performance, real-time emotion detection system integrated with a futuristic web interface and voice feedback. It utilizes deep learning (CNN) to analyze facial expressions and map them to specific emotional states.

---

## 🏗️ Architecture

### 1. Perception Layer (Vision)
- **Engine**: OpenCV (Haar Cascades)
- **Component**: `webcam.py`
- **Function**: Detects faces in video frames or uploaded images. It converts frames to grayscale for efficient processing.

### 2. Analysis Layer (Deep Learning)
- **Engine**: TensorFlow / Keras
- **Model**: Convolutional Neural Network (CNN)
- **File**: `models/emotion_model.h5`
- **Logic**: 
  - Takes a 48x48 pixel grayscale face image.
  - Passes it through multiple Conv2D and Pooling layers.
  - Outputs a probability distribution across 7 emotions.

### 3. Stability Layer (Smoothing AI)
- **Component**: `smoothing.py`
- **Function**: Implements a sliding window buffer (`EmotionSmoother`). This prevents "label flickering" by averaging predictions over recent frames, ensuring a stable UI experience.

### 4. Interactive Layer (Voice & UI)
- **UI**: Streamlit (Futuristic Glassmorphism Design)
- **Voice**: `voice.py` (via `pyttsx3`)
- **Localization**: supports Hindi voice feedback and labels for an localized user experience.

---

## 🛠️ Components Detail

### `app.py`
The central hub of the application. It handles:
- Premium CSS injection for the "Future UI" look.
- Sidebar controls for Voice, Sensitivity, and Analytics.
- Tabbed interface for Live Webcam vs. Image Upload.

### `src/config.py`
Centralized configuration for:
- Emotion mappings (English & Hindi).
- Voice response templates.
- Hyperparameters (Image size, smoothing window size).

### `src/voice.py`
Uses a non-blocking threading approach to ensure the UI doesn't freeze while the voice assistant is speaking.

---

## 📊 Model Specifications
- **Input Shape**: (48, 48, 1)
- **Optimizer**: Adam
- **Loss Function**: Categorical Crossentropy
- **Dataset**: FER2013 (35,000+ faces)

---

## 🚀 Future Roadmap
- [ ] Integration with Emotion-based Music Playlists.
- [ ] Multi-person emotional sentiment analysis for group settings.
- [ ] Mobile App deployment via Flutter.
