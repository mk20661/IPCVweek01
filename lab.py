import cv2
import numpy as np


image = cv2.imread('lsy2.jpg')


for y in range(0, image.shape[0]):  
      for x in range(0, image.shape[1]): 
              pixelBlue = image[y, x, 0]
              pixelGreen = image[y, x, 1]
              pixelRed = image[y, x, 2]
             
              image[y, x, 0] = pixelBlue
              image[y, x, 1] = pixelBlue
              image[y, x, 2] = pixelBlue
             

cv2.imshow('Processed Image1', image)
cv2.waitKey(0)
cv2.destroyAllWindows() 

cv2.imwrite("fixedPic0.jpg", image)