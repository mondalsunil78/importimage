import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Tree image.jpg', 0)
img = cv2.resize(img, (500, 500))
equ = cv2.equalizeHist(img)

cv2.imshow('Input Image', img)
cv2.imshow('Output Image', equ)

print('input contrast :', np.max(img) - np.min(img))
print('histeq contrast :', np.max(equ) - np.min(equ))

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.hist(img.ravel(), bins=256, range=[0, 256])
plt.title("Histogram of Input Image")
plt.subplot(1, 2, 2)
plt.hist(equ.ravel(), bins=256, range=[0, 256])
plt.title("Histogram of Output Image")
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
