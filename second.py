import numpy as np
import cv2
import matplotlib.pyplot as plt

blank_img = np.zeros(shape=(700, 700, 3), dtype = np.int8)

cv2.rectangle(blank_img, (200, 300), (400, 400), (255, 0, 0), 10)
cv2.circle(blank_img, (150, 150), 100, (0, 255, 0), 10)

plt.imshow(blank_img)
plt.show()


