import sys
import cv2

cap = cv2.VideoCapture(0)   #카메라 인덱스 번호

if not cap.isOpened():
    print('카메라를 열 수 없습니다')
    sys.exxit()

print('가로 사이즈:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('가로 사이즈:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

while True:
    # ret : 객체, 성공하면 True, 실패하면 False
    # frame : 현재 프레임(영상), numpy.ndarray
    ret, frame = cap.read()

    if not ret:
        break

    inversed = ~frame   # 색상 반전

    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)

    if cv2.waitKey(10) == 27:   # ESC 키
        break

cap.release()   # 메모리 사용 중지
cv2.destroyAllwindows()