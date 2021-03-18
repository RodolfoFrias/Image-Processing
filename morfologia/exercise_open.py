import numpy as np
import cv2 

se = np.ones((9,9), np.uint8) #Elemento estructurante

image = cv2.imread('image.jpg', 0)
dila = cv2.morphologyEx(image, cv2.MORPH_DILATE, se)
ero =  cv2.morphologyEx(image, cv2.MORPH_ERODE, se)
open_ = cv2.morphologyEx(image, cv2.MORPH_OPEN, se)
close_ = cv2.morphologyEx(image, cv2.MORPH_CLOSE, se)

cv2.imshow('Close', close_)
cv2.imshow('Open', open_)
cv2.imshow('Dila', dila)
cv2.imshow('Ero', ero)
cv2.imshow('Original', image)
cv2.waitKey(0)