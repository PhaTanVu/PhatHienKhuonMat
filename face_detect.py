import streamlit as st
import numpy as np
import cv2 as cv

st.subheader('Phát hiện khuôn mặt')
FRAME_WINDOW = st.image([])
deviceId = 0
cap = cv.VideoCapture(deviceId)

if not cap.isOpened():
    st.warning('Không tìm thấy camera. Vui lòng kiểm tra lại thiết bị và thử lại.')
else:
    while True:
        hasFrame, frame = cap.read()
        if not hasFrame:
            st.warning('Không thể đọc khung hình từ camera. Vui lòng kiểm tra lại thiết bị và thử lại.')
            break
        
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        
        # Phát hiện khuôn mặt
        detector = cv.FaceDetectorYN.create(
            'face_detection_yunet_2022mar.onnx',
            "",
            (320, 320),
            0.9,
            0.3,
            5000
        )

        tm = cv.TickMeter()
        frameWidth = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        frameHeight = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        detector.setInputSize([frameWidth, frameHeight])
        
        # Inference
        tm.start()
        faces = detector.detect(frame) # faces is a tuple
        tm.stop()

        # Vẽ kết quả trên ảnh input
        if faces[1] is not None:
            for idx, face in enumerate(faces[1]):
                # print('Face {}, top-left coordinates: ({:.0f}, {:.0f}), box width: {:.0f}, box height {:.0f}, score: {:.2f}'.format(idx, face[0], face[1], face[2], face[3], face[-1]))

                coords = face[:-1].astype(np.int32)
                cv.rectangle(frame, (coords[0], coords[1]), (coords[0]+coords[2], coords[1]+coords[3]), (0, 255, 0), 2)
                cv.circle(frame, (coords[4], coords[5]), 2, (255, 0, 0), 2)
                cv.circle(frame, (coords[6], coords[7]), 2, (0, 0, 255), 2)
                cv.circle(frame, (coords[8], coords[9]), 2, (0, 255, 0), 2)
                cv.circle(frame, (coords[10], coords[11]), 2, (255, 0, 255), 2)
                cv.circle(frame, (coords[12], coords[13]), 2, (0, 255, 255), 2)
        cv.putText(frame, 'FPS: {:.2f}'.format(tm.getFPS()), (1, 16), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Hiển thị kết quả
        FRAME_WINDOW.image(frame, channels='RGB')
        
        # Dừng khi nhấn nút Stop
        if st.button('Stop'):
            break

    # Giải phóng tài nguyên camera
    cap.release()
