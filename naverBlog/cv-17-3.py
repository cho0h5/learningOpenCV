import numpy as np
import cv2

img = cv2.imread('../DATA/handNumber.jpg')
img = cv2.resize(img, dsize=(640, 480), interpolation=cv2.INTER_AREA)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thr = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)

kernel1 = np.ones((9, 9), np.uint8)
thr = cv2.dilate(thr, kernel1, iterations=1)
kernel2 = np.ones((5, 5), np.uint8)
thr = cv2.erode(thr, kernel2, iterations=1)

contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 0, 255), 1)
cv2.imshow('thresh', thr)
cv2.imshow('contour', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
