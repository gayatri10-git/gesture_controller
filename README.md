# 🤚 Hand Gesture Controller

Control YouTube hands-free using **OpenCV**, **MediaPipe**, and **Streamlit**!  
This project lets you play/pause videos, skip to the next one, and control volume — all through **simple hand gestures** 🖐️✌️👍.

---

## 🎬 Demo

Use your webcam and control YouTube like magic:
| Gesture | Action |
|----------|---------|
| 🖐 Open Palm | Play / Pause |
| ✌ Peace Sign | Next Video |
| 🔼 Thumb Up | Volume Up |
| 🔽 Thumb + Index | Volume Down |

---

## 🧠 How It Works

- **MediaPipe** detects your hand landmarks in real-time.  
- **OpenCV** processes the video feed and draws the skeleton overlay.  
- **Streamlit** provides a clean, dark-mode web interface for display.  
- **PyAutoGUI** sends keyboard shortcuts to YouTube in your browser.

---

## 🧩 Tech Stack

| Library | Purpose |
|----------|----------|
| [OpenCV](https://opencv.org/) | Video capture & image processing |
| [MediaPipe](https://developers.google.com/mediapipe) | Real-time hand tracking |
| [Streamlit](https://streamlit.io/) | Interactive web interface |
| [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) | Keyboard automation for YouTube controls |

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/youtube-hand-gesture-controller.git
cd youtube-hand-gesture-controller
pip install -r requirements.txt
