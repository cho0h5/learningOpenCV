import numpy as np
import cv2

img = cv2.imread('../DATA/opencv.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, mask1 = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY)
img = cv2.bitwise_and(img, img, mask=mask1)

kernel = np.ones((3,3), np.uint8)

#opening = cv2.erode(mask1, kernel, iterations=1)
#opening = cv2.dilate(opening, kernel, iterations=1)

#closing = cv2.dilate(mask1, kernel, iterations=1)
#closing = cv2.erode(closing, kernel, iterations=1)

opening = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(mask1, cv2.MORPH_CLOSE, kernel)

cv2.imshow('original', mask1)
cv2.imshow('opening', opening)
cv2.imshow('closing', closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
