import numpy as np
import cv2

b = np.uint8([[[255, 0, 0]]])
g = np.uint8([[[0, 255, 0]]])
r = np.uint8([[[0, 0, 255]]])

hsv_b = cv2.cvtColor(b, cv2.COLOR_BGR2HSV)
hsv_g = cv2.cvtColor(g, cv2.COLOR_BGR2HSV)
hsv_r = cv2.cvtColor(r, cv2.COLOR_BGR2HSV)

print(hsv_b)
print(hsv_g)
print(hsv_r)
