import cv2
import numpy as np


image = cv2.imread('mandrill1.jpg')
outImage =cv2.imread('mandrill1.jpg')


for y in range(0, image.shape[0]):  
      for x in range(0, image.shape[1]): 
              pixelBlue = image[y, x, 0]
              pixelGreen = image[y, x, 1]
              pixelRed = image[y, x, 2]
             
              outImage[y, x, 0] = pixelBlue
              outImage[y, x, 1] = pixelGreen
              outImage[(y+30)%image.shape[0], (x+30)%image.shape[1], 2] = pixelRed
for y in range(0, 30):  
      for x in range(0, image.shape[1]): 
              pixelBlue = outImage[y, x, 0]
              pixelGreen = outImage[y, x, 1]
              pixelRed = outImage[y, x, 2]
             
              outImage[y, x, 0] = pixelBlue
              outImage[y, x, 1] = pixelGreen
              outImage[y, x, 2] = (pixelRed - 20)%256



cv2.imshow('Processed Image1', outImage)
cv2.waitKey(0)
cv2.destroyAllWindows() 

cv2.imwrite("fixedPic1.jpg", outImage)