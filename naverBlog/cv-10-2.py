import numpy as np
import cv2

img = cv2.imread('../DATA/sudoku.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
thr2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
thr3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 2)
thr4 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 33, 2)
thr5 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 63, 2)
thr6 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 93, 2)
thr7 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 123, 2)

titles = ['original', 'Global Thresholding(v-127)', 'Adaptive MEAN', 'Adaptive GAUSSIAN3', 'Adaptive GAUSSIAN7', 'Adaptive GAUSSIAN11', 'Adaptive GAUSSIAN15', 'Adaptive GAUSSIAN19']
images = [img, thr1, thr2, thr3, thr4, thr5, thr6, thr7]

for i in range(8):
    cv2.imshow(titles[i], images[i])

cv2.waitKey(0)
cv2.destroyAllWindows()
