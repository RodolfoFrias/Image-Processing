import numpy as np
import cv2
from matplotlib import pyplot as plt

imagen = cv2.imread('./images/circulo.png', 0)
# ElemStruct = np.ones((4,4), np.uint8)
ElemStruct = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20,20))
plt.imshow(ElemStruct)
plt.show()

imageEro = cv2.erode(imagen, ElemStruct, iterations=3)
imageDila = cv2.dilate(imagen, ElemStruct, iterations=3)

cv2.imshow('Original', imagen)
cv2.imshow('Erosionada', imageEro)
cv2.imshow('Dilatada', imageDila)
cv2.waitKey(0)