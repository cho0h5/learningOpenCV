import numpy as np
import cv2

x, y = 10, 10

img1 = cv2.imread('../DATA/minions.png')
img2 = cv2.imread('../DATA/opencv.png')

rows, cols, _ = img2.shape
roi = img1[x:x+rows, y:y+cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 30, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
dst = img1_bg + img2_fg
img1[x:x+rows, y:y+cols] = dst

cv2.imshow('mask', mask)

cv2.imshow('img1', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


