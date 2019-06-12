import numpy as np
import cv2

cap = cv2.VideoCapture('../DATA/rgbObjects.mp4')

while True:
    
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_b = np.array([110, 100, 100])
    higher_b = np.array([130, 255, 255])

    lower_g = np.array([50, 100, 100])
    higher_g = np.array([70, 255, 255])

    lower_r = np.array([10, 100, 100])
    higher_r = np.array([-10, 255, 255])

    mask_b = cv2.inRange(hsv, lower_b, higher_b)
    mask_g = cv2.inRange(hsv, lower_g, higher_g)
    mask_r = cv2.inRange(hsv, lower_r, higher_r)

    res1 = cv2.bitwise_and(frame, frame, mask=mask_b)
    res2 = cv2.bitwise_and(frame, frame, mask=mask_g)
    res3 = cv2.bitwise_and(frame, frame, mask=mask_r)

    cv2.imshow('original', frame)
    cv2.imshow('blue', res1)
    cv2.imshow('green', res2)
    cv2.imshow('red', res3)

    k = cv2.waitKey(1) & 0&FF
    if k == ord('q'):
        break

cv2.destroyAllWindows()
