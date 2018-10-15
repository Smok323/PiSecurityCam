import cv2

# Will have to be modified to Access Raspberry Pi Camera Module

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    cv2.imshow('Pi Sec Cam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
