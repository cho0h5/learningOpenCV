import numpy as np
import cv2

img = cv2.imread('../DATA/bigbig.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

rows, cols = img.shape[:2]

_, thr = cv2.threshold(img_gray, 127, 255, 1)
contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contour = contours[0]

(x, y), r = cv2.minEnclosingCircle(contour)
center, r = (int(x), int(y)), int(r)
cv2.circle(img, center, r, (0, 0, 255), 2)

ellipse = cv2.fitEllipse(contour)
cv2.ellipse(img, ellipse, (0, 255, 0), 2)

[vx, vy, x, y] = cv2.fitLine(contour, cv2.DIST_L2, 0, 0.01, 0.01)
#ly = int((-x*vy/vx) + y)
#ry = int(((cols-x)*vy/vx) + y)
#cv2.line(img, (cols-1, ry), (0, ly), (255, 0, 0), 2)

#xi = int(-y*vx/vy + x)
#yi = int(-x*vy/vx + y)
#print(xi, yi)
#cv2.line(img, (0, yi), (xi, 0), (255, 0, 0), 2)

print((int(x), int(y)), (100*int(x+vx), 100*int(y+vy)))
cv2.line(img, (int(x), int(y)), (100*int(x+vx), 100*int(y+vy)), (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
