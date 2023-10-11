import cv2

src = cv2.imread('field.bmp', cv2.IMREAD_COLOR)
batman = cv2.imread('batman.png', cv2.IMREAD_UNCHANGED) # .png파일은 IMREAD_UNCHANGED 사용(alpha(투명도) 추출) -> (h, w, (b,g,r,a))

# if src is None or batman is None:
#     print('영상을 불러올 수 없습니다')
#     sys.exit()
#
mask = batman[:, :, 3]  # 알파 값을 제외한 컬러 값만 가져옴 -> 배경은 0(흑)이여서 나두고 0이 아닌 색상은 모두 255(백)으로 바꿈
# batman = batman[:, :, :-1]  # batman은 b,g,r 3채널
# h, w = mask.shape[:2]
# crop = src[10:10+h, 10:10+w]    # batman, mask와 같은 크기의 부분 영상 추출
#
# cv2.copyTo(batman, mask, crop)
#
# cv2.imshow('src', src)
cv2.imshow('batman', batman)
cv2.imshow('mask', mask)
# cv2.imshow('crop', crop)
cv2.waitKey()
cv2.destroyAllwindows()