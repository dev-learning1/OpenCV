import sys
import cv2
import glob # 이미지를 한번에 불러오는 라이브러리

imgFiles = glob.glob('images\\*.jpg')
#print(imgFiles)

if not imgFiles:
    print('영상을 불러올 수 없습니다.')
    sys.exit()

idx = 0
while True:
    img = cv2.imread(imgFiles[idx])

    if img is None:
        print('영상을 불러올 수 없습니다.')
        break

    cv2.imshow('Cosmos', img)
    if cv2.waitKey(1000) >= 0:  # 키보드 입력이 없을 시 1초 후 다음 사진으로 넘어감
        break

    idx += 1
    if idx >= len(imgFiles):
        idx = 0

cv2.destroyAllWindows()