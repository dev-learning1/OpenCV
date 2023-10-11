import cv2
import sys

cap = cv2.VideoCapture('Blossoms.mp4')

if not cap.isOpened():
    print('동영상을 열 수 없습니다.')
    sys.exit()

print('가로 사이즈:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('가로 사이즈:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('프레임 수:',int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))  # 영상 수

fps = cap.get(cv2.CAP_PROP_FPS) # 초당 몇 프레임인지
print('FPS:',fps)

delay = round(1000 / fps)
print('delay:', delay)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    inversed = ~frame

    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)

    if cv2.waitKey(delay) == 27:
        break

cap.release()
cv2.destroyAllwindows()
