import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('DATA/minions.png', cv2.IMREAD_COLOR)

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.subplot(121)
plt.imshow(img)

plt.subplot(122)
plt.imshow(img2)

plt.show()
