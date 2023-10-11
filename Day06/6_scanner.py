import numpy as np
import cv2
import sys

def onMouse(event, x, y, flags, param):
    global srcQuad, dragSrc, ptOld, src

    if event == cv2.EVENT_LBUTTONDOWN:
        for i in range(4):
            if cv2.norm(srcQuad[i] - (x, y)) < 25:  # norm : 정규분포
                dragSrc[i] = True
                ptOld = (x, y)
                break

    if event == cv2.EVENT_LBUTTONUP:
        for i in range(4):
            dragSrc[i] = False

    if event == cv2.EVENT_MOUSEMOVE:
        for i in range(4):
            if dragSrc[i]:
                dx = x - ptOld[0]
                dy = y - ptOld[1]

                srcQuad[i] += (dx, dy)

                cpy = drawROI(src, srcQuad)
                cv2.imshow('img', cpy)
                ptOld = (x, y)
                break


def drawROI(img, corners):
    cpy = img.copy()
    c1 = (192, 192, 255)    # 각 꼭짓점 근처 점들의 색상
    c2 = (128, 128, 255)    # 점들을 이동시킬 때 선 색상

    for pt in corners:
        cv2.circle(cpy, tuple(pt.astype(int)), 25, c1, -1, cv2.LINE_AA) # 25:반지름, c1:색상, -1:안에 색상 채우는 것, cv2.LINE_AA:선 종류

    cv2.line(cpy, tuple(corners[0].astype(int)), tuple(corners[1].astype(int)), c2, 2, cv2.LINE_AA) # 2:선 두께
    cv2.line(cpy, tuple(corners[1].astype(int)), tuple(corners[2].astype(int)), c2, 2, cv2.LINE_AA)  # 2:선 두께
    cv2.line(cpy, tuple(corners[2].astype(int)), tuple(corners[3].astype(int)), c2, 2, cv2.LINE_AA)  # 2:선 두께
    cv2.line(cpy, tuple(corners[3].astype(int)), tuple(corners[0].astype(int)), c2, 2, cv2.LINE_AA)  # 2:선 두께

    # 이미지1, alpha, 이미지2, 이미지2 가중치, dtype:0(동일한 타입)
    disp = cv2.addWeighted(img, 0.3, cpy, 0.7, 0)   # 0.3, 0.7 : 투명도(alpha) / img:바탕, cpy:바탕위에 얹어놓음 /

    return disp


src = cv2.imread('scanned.jpg')

h, w = src.shape[:2]
dw = 500
# A4용지 크기 : 210 x 297 cm
dh = round(dw * 297 / 210)

srcQuad = np.array([[30, 30], [30, h-30], [w-30, h-30], [w-30, 30]], np.float32)    # 맨 처음 생성되는 각 꼭짓점 근처 점의 위치
dstQuad = np.array([[0, 0], [0, dh-1], [dw-1, dh-1], [dw-1, 0]], np.float32)
dragSrc = [False, False, False, False]

# 이미지에 꼭짓점 근처 점 4개 생성
disp = drawROI(src, srcQuad)

cv2.imshow('img', disp)
cv2.setMouseCallback('img', onMouse)    # 마우스 이벤트 발생시 onMouse 함수 실행

while True:
    key = cv2.waitKey()
    if key == 13:   # enter 눌렀을 때
        break
    elif key == 27:    # esc 눌렀을 때
        cv2.destroyWindow('img')
        sys.exit()

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (dw, dh), flags=cv2.INTER_CUBIC)

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()