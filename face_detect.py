import cv2

cap = cv2.VideoCapture(0) # 0 là ID của camera mặc định

while True:
    # Lấy từng frame của camera
    ret, frame = cap.read()

    # Hiển thị frame lên màn hình
    cv2.imshow('Camera', frame)

    # Nếu nhấn phím 'q' thì thoát khỏi vòng lặp
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên và đóng cửa sổ hiển thị hình ảnh
cap.release()
cv2.destroyAllWindows()
