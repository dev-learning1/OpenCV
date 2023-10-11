# 스케치북(켄버스) 만들기

import cv2
import numpy as np

oldx = oldy = -1    # 초기값으로 없는 값 설정

def on_mouse(event, x, y, flags, param):
    global oldx, oldy   # 전역변수를 사용할 수 있도록 설정

    if event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 마우스 버튼이 눌릴 때
        oldx, oldy = x, y
        print('왼쪽 버튼 클릭: %d, %d' %(x, y))
    elif event == cv2.EVENT_LBUTTONUP:  # 왼쪽 마우스 버튼을 땠을 때
        print('왼쪽 버튼 땜: %d, %d' %(x, y))
    elif event == cv2.EVENT_MOUSEMOVE:  # 마우스가 움직일 때
        if flags & cv2.EVENT_FLAG_LBUTTON:  # 마우스를 누르고(flags) 있으면서(&) 왼쪽 버튼을 눌렀을 때(cv2.EVENT_FLAG_LBUTTON)
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 4, cv2.LINE_AA)
            cv2.imshow('image', img)
            oldx, oldy = x, y

img = np.ones((480, 640, 3), dtype=np.uint8) * 255

cv2.namedWindow('image')
cv2.setMouseCallback('image', on_mouse, img)    # 이벤트 발생시 자동 함수 실행

cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()