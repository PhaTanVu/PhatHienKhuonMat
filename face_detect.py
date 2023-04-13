import streamlit as st
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    st.error("Cannot open camera")

stop_button = st.button("Stop")
while not stop_button:
    ret, frame = cap.read()
    if not ret:
        st.error("Failed to grab frame")
        break

    cv2.imshow('Camera', frame)

    # Wait for a key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # Update the stop button state
    stop_button = st.session_state.stop_button

# Clean up
cap.release()
cv2.destroyAllWindows()
