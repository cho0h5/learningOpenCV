import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)
cv2.rectangle(img, (100, 100), (200, 200), (255, 255, 255), -1)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thr = cv2.threshold(imgray, 127, 255, 0)

#contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
cv2.imshow('thresh', thr)
cv2.imshow('contour', img)
print(contours)

cv2.waitKey(0)
cv2.destroyAllWindows()
