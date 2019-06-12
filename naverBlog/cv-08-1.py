import numpy as np
import cv2

img1 = cv2.imread('../DATA/minions.png')[0:400, 0:1400]
img2 = cv2.imread('../DATA/frozen.png')[0:400, 0:1400]

#cv2.imshow('img1', img1)
#cv2.imshow('img2', img2)

add_img_a = img1+img2
add_img_b = cv2.add(img1, img2)

cv2.imshow('add_img_a', add_img_a)
cv2.imshow('add_img_b', add_img_b)

cv2.waitKey(0)
cv2.destroyAllWindows()
