import numpy as np
import cv2

img = cv2.imread('../DATA/grad.png')

_, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, thr2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, thr3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, thr4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, thr5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('original', img)
cv2.imshow('binary', thr1)
cv2.imshow('binary_inv', thr2)
cv2.imshow('trunc', thr3)
cv2.imshow('tozero', thr4)
cv2.imshow('tozero_inv', thr5)

cv2.waitKey(0)
cv2.destroyAllWindows()
