import numpy as np
import cv2
from random import shuffle
import math

B = [i for i in range(256)]
G = [i for i in range(256)]
R = [i for i in range(256)]

xx, yy = 0, 0
drawing, mode = False, False

def onMouse(event, x, y, flags, param):
    global xx, yy, drawing, mode, B, G, R
    if event == cv2.EVENT_LBUTTONDOWN:
        shuffle(B), shuffle(G), shuffle(R)
        xx, yy = x, y
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == False:
                cv2.rectangle(param, (xx, yy), (x, y), (B[0], G[0], R[0]), -1)
            elif mode == True:
                r = int(math.sqrt((x - xx) ** 2 + (y - yy) ** 2))
                cv2.circle(param, (xx, yy), r, (B[0], G[0], R[0]), -1)
        
    elif event == cv2.EVENT_LBUTTONUP:
            drawing = False


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('paint')
cv2.setMouseCallback('paint', onMouse, param=img)

while True:
    cv2.imshow('paint', img)
    k = cv2.waitKey(1) & 0xFF
    
    if k == 27:
        break
    elif k == ord('m'):
        mode = not mode

cv2.destroyAllWindows()
