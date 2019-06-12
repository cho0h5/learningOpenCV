import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    global lower, higher

    if event == cv2.EVENT_LBUTTONDOWN:
        h = param.item(y, x, 0)
        s = param.item(y, x, 1)
        v = param.item(y, x, 2)
        lower = np.array([h-5, s-60, v-100])
        higher = np.array([h+5, s+60, v+100])

cv2.namedWindow('original')

lower = np.array([0, 0, 0])
higher = np.array([255, 255, 255])

cap = cv2.VideoCapture('../DATA/rgbObjects.mp4')

while cap.isOpened():
    
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    mask = cv2.inRange(hsv, lower, higher)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    frame = cv2.resize(frame, dsize=(0, 0), fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
    res = cv2.resize(res, dsize=(0, 0), fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
    hsv = cv2.resize(hsv, dsize=(0, 0), fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)

    cv2.imshow('original', frame)
    cv2.imshow('seleted', res)

    cv2.setMouseCallback('original', onMouse, param=hsv)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

cv2.destroyAllWindows()
