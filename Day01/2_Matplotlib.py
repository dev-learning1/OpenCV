import matplotlib.pyplot as plt
import cv2

imgBGR = cv2.imread('cat.bmp')  # 컬러 영상(순서: Blue, Green, Red)
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)    # BGR -> RGB

#plt.axis('off') #격자를 감춤
#plt.figure(1)
#plt.imshow(imgBGR)
#plt.figure(2)
#plt.imshow(imgRGB)
#plt.show()

imgGray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
# plt.axis('off') #격자를 감춤
# plt.imshow(imgGray, cmap='gray')
# plt.show()

plt.subplot(121)
plt.axis('off') #격자를 감춤
plt.imshow(imgRGB, cmap='gray')
plt.subplot(122)
plt.axis('off') #격자를 감춤
plt.imshow(imgGray, cmap='gray')
plt.show()

