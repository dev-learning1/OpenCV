import sys
import numpy as np
import cv2

src = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('영상을 읽을 수 없습니다')
    sys.exit()

cv2.imshow('src', src)

# 마스크 값이 커질수록 더 뿌옇게됨
for ksize in (3, 5, 7):
    dst = cv2.blur(src, (ksize, ksize))

    desc = 'Mean : {}x{}'.format(ksize, ksize)
    cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 0, 1, cv2.LINE_AA)

    cv2.imshow('dst', dst)
    cv2.waitKey()

cv2.destroyAllWindows