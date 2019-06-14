import numpy as np
import cv2

img = cv2.imread('../DATA/opencv.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, mask1 = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY)
img = cv2.bitwise_and(img, img, mask=mask1)

kernel = np.ones((3,3), np.uint8)

grad = cv2.morphologyEx(mask1, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(mask1, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(mask1, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow('original', mask1)
cv2.imshow('grad', grad)
cv2.imshow('tophat', tophat)
cv2.imshow('blackhat', blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
