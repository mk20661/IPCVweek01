import cv2
import numpy as np

image = cv2.imread('mandrillRGB.jpg')


for y in range(0, image.shape[0]):  # go through all rows (or scanlines)
      for x in range(0, image.shape[1]):  # go through all columns
              pixelBlue = image[y, x, 0]
              pixelGreen = image[y, x, 1]
              pixelRed = image[y, x, 2]
              if (pixelBlue>200):
                      image[y, x, 0] = 255
                      image[y, x, 1] = 255
                      image[y, x, 2] = 255
              else:
                      image[y, x, 0] = 0
                      image[y, x, 1] = 0
                      image[y, x, 2] = 0

cv2.imshow('Processed Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("colourthr1.jpg", image)

