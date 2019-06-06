import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('DATA/frozen.png')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread('DATA/frozen_logo.png')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

print(img1.shape)
print(img2.shape)

plt.subplot(311)
plt.imshow(img1)


img1 = cv2.resize(img1, (1300, 600))
img2 = cv2.resize(img2, (1300, 600))

print(img1.shape)
print(img2.shape)

plt.subplot(312)
plt.imshow(img1)

blended_img = cv2.addWeighted(src1 = img1, alpha = 0.7, src2 = img2, beta = 0.3, gamma = 0)

plt.subplot(313)
plt.imshow(blended_img)
plt.show()
