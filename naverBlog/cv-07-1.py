import numpy as np
import cv2

img = cv2.imread('../DATA/minions.png')
#px = img[740, 400]

b = img.item(740, 400, 0)
g = img.item(740, 400, 1)
r = img.item(740, 400, 2)

bgr = [b, g, r]

print(bgr)

print(img.shape)
print(img.dtype)
print(img.size)

cv2.imshow('original', img)

roi = img[300:700, 200:400]
cv2.imshow('roi', roi)

img[100:500, 0:200] = roi
cv2.imshow('sum', img)

cv2.waitKey()
cv2.destroyAllWindows()
