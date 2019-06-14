import numpy as np
import cv2

img = cv2.imread('../DATA/minions.png')

img2 = cv2.resize(img, None, fx=0.5, fy=1, interpolation=cv2.INTER_AREA)
img3 = cv2.resize(img, None, fx=1, fy=0.5, interpolation=cv2.INTER_AREA)
img4 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

cv2.imshow('original', img)
cv2.imshow('0.5 1', img2)
cv2.imshow('1 0.5', img3)
cv2.imshow('0.5 0.5', img4)

cv2.waitKey(0)
cv2.destroyAllWindows()
