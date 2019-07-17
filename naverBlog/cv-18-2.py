import numpy as np
import cv2

img = cv2.imread('../DATA/name.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thr = cv2.threshold(img_gray, 127,255, 0)

kernel1 = np.ones((9, 9), np.uint8)
thr = cv2.erode(thr, kernel1, iterations=1)
kernel2 = np.ones((15, 15), np.uint8)
thr = cv2.dilate(thr, kernel2, iterations=1)

contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contour = contours[4]
cv2.drawContours(img, [contour], 0, (0, 0, 255), 1)

mmt = cv2.moments(contour)

length = cv2.arcLength(contour, True)
epsilon1 = length * 0.1
epsilon2 = length * 0.01

approx1 = cv2.approxPolyDP(contour, epsilon1, True)
approx2 = cv2.approxPolyDP(contour, epsilon2, True)

#cv2.drawContours(img, [approx1], 0, (0, 255, 0), 2)
cv2.drawContours(img, [approx2], 0, (255, 0, 0), 2)

cv2.imshow('contour', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
