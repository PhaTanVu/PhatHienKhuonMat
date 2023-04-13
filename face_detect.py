import streamlit as st
import cv2

st.title('Camera Stream')

# Khởi tạo camera
cap = cv2.VideoCapture(0)

# Kiểm tra xem camera đã mở chưa
if not cap.isOpened():
    st.error('Không thể mở camera.')
else:
    while True:
        # Đọc từng khung hình của camera
        ret, frame = cap.read()
        if not ret:
            st.error('Không thể đọc khung hình.')
            break

        # Hiển thị khung hình trên giao diện của Streamlit
        st.image(frame, channels="BGR")

        # Thêm một nút để dừng camera
        if st.button('Dừng Camera'):
            break

    # Giải phóng tài nguyên
    cap.release()
    cv2.destroyAllWindows()
