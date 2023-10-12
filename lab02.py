import cv2
import numpy as np


image = cv2.imread('mandrill2.jpg')
outImage =cv2.imread('mandrill2.jpg')


for y in range(0, image.shape[0]):  
      for x in range(0, image.shape[1]): 
              pixelBlue = image[y, x, 0]
              pixelGreen = image[y, x, 1]
              pixelRed = image[y, x, 2]
             
              outImage[y, x, 0] = 255 - pixelBlue 
              outImage[y, x, 1] = 255 - pixelGreen
              outImage[y, x, 2] = 255 - pixelRed 

cv2.imshow('Processed Image2', outImage)
cv2.waitKey(0)
cv2.destroyAllWindows() 

cv2.imwrite("fixedPic2.jpg", outImage)