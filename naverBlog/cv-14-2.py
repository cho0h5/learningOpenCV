import numpy as np
import cv2
import matplotlib.pyplot as plt

img = np.zeros((1080, 1920), dtype=np.uint8)
cv2.rectangle(img, (300, 0), (800, 1080), 255, -1)

sobelx8u = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)
tmp = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel64f = np.absolute(tmp)
sobelx8u2 = np.uint8(sobel64f)

plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')
plt.title('original')

plt.subplot(1, 3, 2), plt.imshow(sobelx8u, cmap='gray')
plt.title('Sobel 8U')

plt.subplot(1, 3, 3), plt.imshow(sobelx8u2, cmap='gray')
plt.title('Sobel 64F')

plt.show()
