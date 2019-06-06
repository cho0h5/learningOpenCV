import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('DATA/minions.png')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img3 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
roi = img2[300:600, 400:650]

cv2.rectangle(img, (200, 300), (400, 400), (255, 0, 0), 10)
cv2.rectangle(img2, (200, 300), (400, 400), (255, 0, 0), 10)

plt.subplot(321)
plt.imshow(img)

plt.subplot(322)
plt.imshow(img2)

plt.subplot(323)
plt.imshow(img3, cmap = 'gray')

plt.subplot(324)
plt.imshow(roi)

plt.subplot(325)
gray_roi = cv2.cvtColor(roi, cv2.COLOR_RGB2GRAY)
img2[300:600, 400:650] = gray_roi[:, :, None]
plt.imshow(img2)

plt.show()
