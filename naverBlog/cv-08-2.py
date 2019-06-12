import numpy as np
import cv2

def onMouse(x):
    pass

img1 = cv2.imread('../DATA/minions.png')[0:400, 0:1400]
img2 = cv2.imread('../DATA/frozen.png')[0:400, 0:1400]

cv2.namedWindow('imgPane')
cv2.createTrackbar('mixing', 'imgPane', 0, 100, onMouse)

while True:
    mix = cv2.getTrackbarPos('mixing', 'imgPane')

    img = cv2.addWeighted(img1, (100-mix)/100, img2, mix/100, 0)
    cv2.imshow('imgPane', img)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break



cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows()
