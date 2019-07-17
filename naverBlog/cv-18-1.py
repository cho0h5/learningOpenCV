import numpy as np
import cv2

img = cv2.imread('../DATA/name.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thr = cv2.threshold(img_gray, 127,255, 0)

kernel1 = np.ones((9, 9), np.uint8)
thr = cv2.erode(thr, kernel1, iterations=1)
kernel2 = np.ones((15, 15), np.uint8)
thr = cv2.dilate(thr, kernel2, iterations=1)

contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

'''
for contour in contours:
    mmt = cv2.moments(contour)
    cx, cy = int(mmt['m10']/mmt['m00']), int(mmt['m01']/mmt['m00'])
    img = cv2.circle(img, (cx, cy), 5, (0, 0, 255), -1)
'''

contour = contours[0]
mmt = cv2.moments(contour)
cx, cy = int(mmt['m10']/mmt['m00']), int(mmt['m01']/mmt['m00'])
img = cv2.circle(img, (cx, cy), 5, (0, 0, 255), -1)

img = cv2.drawContours(img, contours, -1, (0, 0, 255), 1)
area = cv2.contourArea(contour)
perimeter = cv2.arcLength(contour, True)

print(area)
print(perimeter)

cv2.imshow('contour', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
