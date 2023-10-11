import cv2
import numpy as np

src = cv2.imread('namecard.jpg')

# 명함 비율 : 90 * 50
w, h = 720, 400     # 8배
srcQuad = np.array([[346, 285], [1117, 225], [1270, 659], [326, 779]], np.float32)
dstQuad = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], np.float32)    # -1 : 이미지 가장자리를 콘솔창 가장자리와 떨어트리기 위해

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
# retval : 3x3 투시 변환 행렬

dst = cv2.warpPerspective(src, pers, (w, h))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()