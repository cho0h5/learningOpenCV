import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../DATA/sudoku.jpg', cv2.IMREAD_GRAYSCALE)

_, thr1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
blur = cv2.GaussianBlur(img, (5, 5), 0)
_, thr2 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

titles = ['original noisy', 'Histogram', 'Otsu Thresholding',
          'Gaussian-filtered', 'Histogram', 'Otsu Thresholding']
images = [img, 0, thr1,
          blur, 0, thr2]

for i in range(2):
    plt.subplot(2, 3, i*3+1)
    plt.imshow(images[i*3], 'gray')
    plt.title(titles[i*3])
    
    plt.subplot(2, 3, i*3+2)
    plt.hist(images[i*3].ravel(), 256)
    plt.title(titles[i*3+1])
    
    plt.subplot(2, 3, i*3+3)
    plt.imshow(images[i*3+2], 'gray')
    plt.title(titles[i*3+2])
    
plt.show()
