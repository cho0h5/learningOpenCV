import numpy as np
import cv2

img = cv2.imread('../DATA/minions.png')
h,w = img.shape[:2]

M = np.float32([[1, 0, 100], [0, 1, 50]])

img2 = cv2.warpAffine(img, M, (w, h))

cv2.imshow('shifted', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
