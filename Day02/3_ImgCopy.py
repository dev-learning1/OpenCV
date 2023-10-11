import cv2

# img1 = cv2.imread('dog.jpg')
# img2 = img1 # 참조 : 주소값 연결
# img3 = img1.copy()  # 주소 다름

img1 = cv2.imread('dog.jpg')
img2 = img1[187:680, 389:690]   # [y:x+h, x:y+w]
img3 = img1[187:680, 389:690].copy()

img2.fill(0)    # 같은 주소를 갖고 있는 img1도 픽셀값 변경
# http://maschek.hu/imagemap/imgmap/    # 이미지 맵 좌표 추출 사이트
# 389,187,504,294
#  x   y   w   h

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllwindows()