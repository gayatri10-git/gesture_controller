import cv2
import mediapipe as mp
import streamlit as st
import pyautogui
import time

st.set_page_config(
    page_title="YouTube Hand Gesture Controller",
    page_icon="✋",
    layout="centered"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #B0BEC5;
        font-family: Arial, sans-serif;
    }
    h1, h4 {
        color: #00FF7F;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center'>Gesture Controller</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center'>Control any site with hand gestures</h4>", unsafe_allow_html=True)


video_placeholder = st.empty()
gesture_placeholder = st.empty()

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=1)

def recognize_gesture(landmarks):
    if len(landmarks) < 21:
        return "🤚 Unknown"
    
    tips = [4, 8, 12, 16, 20]
    folded = [landmarks[tip].y > landmarks[tip - 2].y for tip in tips[1:]]
    thumb_up = landmarks[4].y < landmarks[3].y

    if not folded[0] and not folded[1] and folded[2] and folded[3]:
        return "✌️ Peace Sign"
    if not any(folded) and thumb_up:
        return "🖐 Open Palm"
    if thumb_up and all(folded):
        return "🔼 Volume Up"
    if thumb_up and not folded[0] and folded[1] and folded[2] and folded[3]:
        return "🔽 Volume Down"

    return "🤚 Unknown"


feedback = "Show a hand to start!"
last_action_time = 0
action_cooldown = 1  
current_gesture = None

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        st.error("⚠️ Cannot access webcam!")
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    gesture = "No hand detected"
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            gesture = recognize_gesture(hand_landmarks.landmark)
            if gesture != "🤚 Unknown":
                feedback = f"Detected Gesture: {gesture}"
                current_gesture = gesture

                current_time = time.time()
                if current_time - last_action_time > action_cooldown:
                    if gesture == "🖐 Open Palm":
                        pyautogui.press("space")  # Play/Pause
                        feedback = "▶️ Play/Pause"
                    elif gesture == "✌️ Peace Sign":
                        pyautogui.hotkey("shift", "n")  # Next Video
                        feedback = "⏭ Next Video"
                    elif gesture == "🔼 Volume Up":
                        pyautogui.press("up")
                        feedback = "🔊 Volume Up"
                    elif gesture == "🔽 Volume Down":
                        pyautogui.press("down")
                        feedback = "🔉 Volume Down"
                    last_action_time = current_time
            else:
                current_gesture = None

    frame_resized = cv2.resize(frame, (640, 360))  # width x height
    video_placeholder.image(cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB), use_container_width=False)

    gesture_placeholder.markdown(
        f"<h2 style='text-align:center; color:#00FF7F; margin-top:1rem;'>{feedback}</h2>",
        unsafe_allow_html=True
    )

cap.release()
cv2.destroyAllWindows()
