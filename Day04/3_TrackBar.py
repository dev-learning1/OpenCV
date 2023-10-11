import cv2
import sys
import numpy as np

def on_change(pos): # 트랙바 위치
    print(pos)
    value = pos * 16
    if value >= 255:
        value = 255

    img[:] = value
    cv2.imshow('image', img)

img = np.zeros((480, 640), np.uint8)

cv2.namedWindow('image')
cv2.createTrackbar('level', 'image', 0, 16, on_change)    # 이벤트 발생시 자동 함수 실행

cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()