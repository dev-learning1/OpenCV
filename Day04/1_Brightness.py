import cv2
import sys

# 그레이스케일 영상
src = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('영상을 불러 올 수 없습니다')
    sys.exit()

# 원본 각 픽셀값에 100을 더해줌
dst = cv2.add(src, 100)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

# 컬러 영상
src = cv2.imread('cat.bmp')

if src is None:
    print('영상을 불러 올 수 없습니다')
    sys.exit()

# 각 픽셀값(b, g, r) 100 더해줌. 0은 채널 의미
dst = cv2.add(src, (100, 100, 100, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()