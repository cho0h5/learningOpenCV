import numpy as np
import cv2

img = cv2.imread('../DATA/minions.png')

#b, g, r = cv2.split(img)

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

#cv2.imshow('b', b)
#cv2.imshow('g', g)
#cv2.imshow('r', r)

re_img = cv2.merge((b, g, r))
cv2.imshow('re_img', re_img)

cv2.waitKey()
cv2.destroyAllWindows()
