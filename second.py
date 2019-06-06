import numpy as np
import cv2
import matplotlib.pyplot as plt

blank_img1 = np.zeros(shape=(300, 300), dtype = np.int8)
blank_img2 = np.zeros(shape=(300, 300), dtype = np.int8)

cv2.rectangle(blank_img1, (20, 20), (150, 150), 255, -1)
cv2.circle(blank_img2, (150, 150), 150, 255, -1)

plt.subplot(511)
plt.imshow(blank_img1, cmap = 'gray')

plt.subplot(512)
plt.imshow(blank_img2, cmap = 'gray')

plt.subplot(513)
blend_and = cv2.bitwise_and(blank_img1, blank_img2)
plt.imshow(blend_and, cmap = 'gray')

plt.subplot(514)
blend_or = cv2.bitwise_or(blank_img1, blank_img2)
plt.imshow(blend_or, cmap = 'gray')

plt.subplot(515)
blend_not = cv2.bitwise_not(blank_img2)
plt.imshow(blend_not, cmap = 'gray')

plt.show()


