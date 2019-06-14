import numpy as np
import cv2

img = cv2.imread('../DATA/sudoku.jpg')
h, w = img.shape[:2]

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

pts3 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
pts4 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])

M1 = cv2.getAffineTransform(pts1, pts2)
M2 = cv2.getPerspectiveTransform(pts3, pts4)

img2 = cv2.warpAffine(img, M1, (w, h))
img3 = cv2.warpPerspective(img, M2, (w, h))

cv2.imshow('original', img)
cv2.imshow('Affine-Transform', img2)
cv2.imshow('Perspective-Transform', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
