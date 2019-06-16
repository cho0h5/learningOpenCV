import numpy as np
import cv2
import matplotlib.pyplot as plt

#img = cv2.imread('../DATA/chang2.png')
#img = cv2.imread('../DATA/minions.png')
img = cv2.imread('../DATA/alp.png')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
edge1 = cv2.Canny(img, 50, 200)
edge2 = cv2.Canny(img, 100, 200)
edge3 = cv2.Canny(img, 170, 200)

plt.subplot(2, 2, 1)
plt.imshow(img)

plt.subplot(2, 2, 2)
plt.imshow(edge1, cmap='gray')

plt.subplot(2, 2, 3)
plt.imshow(edge2, cmap='gray')

plt.subplot(2, 2, 4)
plt.imshow(edge3, cmap='gray')

plt.show()
