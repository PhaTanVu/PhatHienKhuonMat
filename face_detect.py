import streamlit as st
import numpy as np
import cv2 as cv

st.subheader('Phát hiện khuôn mặt')
FRAME_WINDOW = st.image([])
deviceId = 0
cap = cv.VideoCapture(deviceId)

while True:
    hasFrame, frame = cap.read()
    if not hasFrame:
        print('No frames grabbed!')
        break

    FRAME_WINDOW.image(frame, channels='BGR')
