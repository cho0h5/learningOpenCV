import numpy as np
import cv2

def onChange(x):
    pass

img = np.zeros((200, 512, 3), np.uint8)
cv2.namedWindow('color_palette')

cv2.createTrackbar('b', 'color_palette', 0, 255, onChange)
cv2.createTrackbar('g', 'color_palette', 0, 255, onChange)
cv2.createTrackbar('r', 'color_palette', 0, 255, onChange)

cv2.createTrackbar('0: Off\n1: On', 'color_palette', 0, 1, onChange)

while True:
    cv2.imshow('color_palette', img)
    k = cv2.waitKey(1) & 0xFF

    if k == 27:
        break

    b = cv2.getTrackbarPos('b', 'color_palette')
    g = cv2.getTrackbarPos('g', 'color_palette')
    r = cv2.getTrackbarPos('r', 'color_palette')
    s = cv2.getTrackbarPos('0: Off\n1: On', 'color_palette')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()
