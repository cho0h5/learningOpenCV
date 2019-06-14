import numpy as np
import cv2

img = cv2.imread('../DATA/noise.png')
#img = cv2.imread('../DATA/chang2.png')

blur3 = cv2.medianBlur(img, 11)
blur4 = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow('original', img)
cv2.imshow('blur_Median', blur3)
cv2.imshow('blur_Bilateral', blur4)

cv2.waitKey(0)
cv2.destroyAllWindows()
