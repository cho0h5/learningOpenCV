import numpy as np
import cv2

img = cv2.imread('../DATA/frozen.png')
tmp = img.copy()

win_titles = ['org', 'level1', 'level2', 'level3']
g_down = []
g_down.append(img)

for i in range(3):
    tmp1 = cv2.pyrDown(tmp)
    g_down.append(tmp1)
    tmp = tmp1

for i in range(4):
    cv2.imshow(win_titles[i], g_down[i])

cv2.waitKey(0)
cv2.destroyAllWindows()
