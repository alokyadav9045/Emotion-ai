# 🧠 AI Emotion Detection System

A complete **Facial Emotion Detection** project powered by a **Convolutional Neural Network (CNN)** and deployed with **Streamlit**.

---

## 📁 Project Structure

```
emotion-ai/
│
├── models/
│     └── emotion_model.h5        # Trained CNN model
│
├── dataset/
│     └── fer2013.csv             # FER2013 dataset
│
├── src/
│     ├── __init__.py
│     ├── train.py                # Model training script
│     ├── predictor.py            # Emotion prediction module
│     ├── webcam.py               # Face detection engine
│     ├── smoothing.py            # Emotion smoothing AI
│     ├── voice.py                # Voice feedback system
│     └── config.py               # Central configuration
│
├── app.py                        # Streamlit dashboard
├── requirements.txt              # Python dependencies
└── README.md
```

---

## ⚙️ Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Prepare Dataset

Download the [FER2013 dataset](https://www.kaggle.com/datasets/msambare/fer2013) and place `fer2013.csv` inside the `dataset/` folder.

### 3. Train the Model

```bash
cd src
python train.py
```

This will create `emotion_model.h5` in the `models/` directory.

### 4. Launch the Dashboard

```bash
streamlit run app.py
```

---

## 🎯 Features

| Feature              | Description                                       |
|----------------------|---------------------------------------------------|
| **CNN Model**        | 3-layer Conv2D network trained on FER2013         |
| **Image Upload**     | Upload any image for emotion detection            |
| **Webcam Mode**      | Real-time emotion detection via webcam            |
| **Voice Feedback**   | Text-to-speech announces detected emotions        |
| **Emotion Smoothing**| Sliding window prevents prediction flickering     |
| **Multi-Face**       | Detects and labels multiple faces simultaneously  |
| **Dark Mode**        | Toggle dark theme from the sidebar                |

---

## 🧠 Supported Emotions

- 😠 Angry
- 🤢 Disgust
- 😨 Fear
- 😊 Happy
- 😢 Sad
- 😲 Surprise
- 😐 Neutral

---

## 🛠️ Tech Stack

- **TensorFlow / Keras** — CNN model
- **OpenCV** — Face detection (Haar Cascades)
- **Streamlit** — Web dashboard
- **pyttsx3** — Text-to-speech engine
- **NumPy / Pandas** — Data processing

---

## 📜 License

This project is open source and available for educational purposes.
