import cv2
import numpy as np

image = cv2.imread('mandrill.jpg')

image[image >= 128] = 255
image[image < 128 ] = 0
cv2.imshow('Processed Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("thr1.jpg", image)