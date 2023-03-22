# import opencv
import cv2
# read the image
img = cv2.imread('image.jpeg', 0)
# image print
print(img)
# image show
cv2.imshow('Input Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
