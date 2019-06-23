import numpy as np
import cv2

img = cv2.imread('../DATA/remote.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thr = cv2.threshold(imgray, 127, 255, 0)
contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 0, 255), 1)
cv2.imshow('thresh', thr)
cv2.imshow('contour', img)

cv2.waitKey(0)
cv2.destoryAllWindows()
