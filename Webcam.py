import cv2
import numpy as np
import random

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: could not open camera")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: could not read frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    blockSize = 5
    sobelSize = 3
    k = 0.04
    harris = cv2.cornerHarris(gray, blockSize, sobelSize, k)

    harris = cv2.dilate(harris, None)

    corners = np.argwhere(harris > 0.08 * harris.max())

    for corner in corners:
        y, x = corner  # Note: OpenCV uses (y, x) format
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), color, 1)

    # image = np.zeros(frame.shape, np.uint8)

    cv2.imshow('Live camera with corners' , frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()