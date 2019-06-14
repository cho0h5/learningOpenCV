import numpy as np
import cv2

img = cv2.imread('../DATA/chang2.png')

#kernel = np.ones((5, 5), np.float32)/25
#blur = cv2.filter2D(img, -1, kernel)

blur1 = cv2.blur(img, (5, 5))
blur2 = cv2.GaussianBlur(img, (5, 5), 0)
blur3 = cv2.medianBlur(img, 5)

cv2.imshow('original', img)
cv2.imshow('blur_Avg', blur1)
cv2.imshow('blur_Gaussian', blur2)
cv2.imshow('blur_Median', blur3)

cv2.waitKey(0)
cv2.destroyAllWindows()
