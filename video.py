import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow('camera Foat', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break