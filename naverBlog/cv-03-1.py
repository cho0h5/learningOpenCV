import numpy as np
import cv2

try:
    print('run camera')
    cap = cv2.VideoCapture(0)
except:
    print('fail')
