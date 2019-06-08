import numpy as np
import cv2

img = cv2.imread('../DATA/minions.png', cv2.IMREAD_COLOR)

cv2.namedWindow('model', cv2.WINDOW_NORMAL)
cv2.imshow('model', img)

k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('c'):
    cv2.imwrite('minions_copy.png', img)
    cv2.destroyAllWindows()
