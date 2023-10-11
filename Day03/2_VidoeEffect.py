import cv2
import sys
import numpy as np

cap1 = cv2.VideoCapture('Jellyfish.mp4')
cap2 = cv2.VideoCapture('Blossoms.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('동영상을 열 수 없습니다.')
    sys.exit()

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))  # 영상 수
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))  # 영상 수

#fps1 = round(cap1.get(cv2.CAP_PROP_FPS)) # 초당 몇 프레임인지
#fps2 = round(cap2.get(cv2.CAP_PROP_FPS)) # 초당 몇 프레임인지
# 두 초당 프레임 같다고 가정
fps = round(cap1.get(cv2.CAP_PROP_FPS))
effect_frames = int(fps * 2)

delay = round(1000 / fps)

print('frame1:', frame_cnt1)
print('frame2:', frame_cnt2)
print('fps:', fps)
print('effect:', effect_frames)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

out = cv2.VideoWriter('effect.avi', fourcc, fps, (w, h))

# 첫 번째 동영상 마지막 2초 제거
for i in range(frame_cnt1 - effect_frames):
    ret1, frame1 = cap1.read()

    if not ret1:
        print('프레임을 읽을 수 없습니다')
        sys.exit()

    out.write(frame1)

    cv2.imshow('output', frame1)

    if cv2.waitKey(delay) == 27:
        break

# 2초 동안 애니메이션 밀기 구현
for i in range(effect_frames):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        print('프레임을 읽을 수 없습니다')
        sys.exit()

    dx = int(w / effect_frames) * i

    frame = np.zeros((h, w, 3), dtype=np.uint8)
    frame[:, 0:dx, :] = frame2[:, 0:dx, :]  # 영상너비가 점점 커진다
    frame[:, dx:w, :] = frame1[:, dx:w, :]  # 영상너비가 점점 작아진다

    out.write(frame)

    cv2.imshow('output', frame)

    if cv2.waitKey(delay) == 27:
        break

# 두 번째 동영상 앞에서 2초 제거후 실행
for i in range(effect_frames, frame_cnt2):
    ret2, frame2 = cap2.read()

    if not ret2:
        print('프레임을 읽을 수 없습니다')
        sys.exit()

    out.write(frame2)

    cv2.imshow('output',frame2)

    if cv2.waitKey(delay) == 27:
        break

cap1.release()
cap2.release()
out.release()
cv2.destroyAllwindows()
