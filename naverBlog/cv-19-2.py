import numpy as np
import cv2

img = cv2.imread('../DATA/bigbig.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thr = cv2.threshold(img_gray, 127, 255, 1)
contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contour = contours[0]

x, y, w, h = cv2.boundingRect(contour)
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)

rect = cv2.minAreaRect(contour)
box = cv2.boxPoints(rect)
box = np.int0(box)

cv2.drawContours(img, [box], -1, (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
