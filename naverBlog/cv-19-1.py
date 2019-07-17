import numpy as np
import cv2

img = cv2.imread('../DATA/heart.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thr = cv2.threshold(img_gray, 127, 255, 1)
contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contour = contours[0]
#cv2.drawContours(img, [contour], -1, (0, 255, 0), 2)
check = cv2.isContourConvex(contour)
print(check)

if not check:
    hull = cv2.convexHull(contour)
    cv2.drawContours(img, [hull], 0, (0, 0, 255), 2)


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
