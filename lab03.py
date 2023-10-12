import cv2
import numpy as np


image = cv2.imread('mandrill3.jpg')
outImage  = cv2.cvtColor(image,cv2.COLOR_HSV2BGR)
cv2.imshow('Processed Image3', outImage)
cv2.waitKey(0)
cv2.destroyAllWindows() 
cv2.imwrite("fixedPic3.jpg", outImage)