import cv2
import numpy as np


image = cv2.imread('lsy2.jpg')

outImage  = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)


              

cv2.imshow('Processed Image3', outImage)
cv2.waitKey(0)
cv2.destroyAllWindows() 

cv2.imwrite("lsy.jpg", outImage)