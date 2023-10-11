import cv2

src = cv2.imread('cat.bmp')

cp = (src.shape[1] / 2, src.shape[0] / 2)   # src.shape[1] : 가로
rot = cv2.getRotationMatrix2D(cp, 20, 0.5)  # 0.5 : 크기 반으로 줄임

dst = cv2.warpAffine(src, rot, (0, 0))  # (0, 0) : 입력 이미지의 사이즈를 그대로 사용

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()