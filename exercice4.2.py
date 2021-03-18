import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

start = time.process_time()

A = (cv2.imread('./images/CAT.png', 0)).astype(np.float) # 0 cambia a escala de grises

kernelPrewittX = np.array([(-1, 0, 1), (-1,0,1), (-1, 0, 1)])
kernelPrewittY = np.array([(-1,-1,-1),(0,0,0), (1,1,1)])
RX = cv2.filter2D(A,-1, kernelPrewittX)
RY = cv2.filter2D(A, -1, kernelPrewittY)
R = np.sqrt(RX**2 + RY**2)
border = np.array([(0,1,1),(-1,0,1), (-1,-1,0)])
B = cv2.filter2D(A, -1, border)

plt.figure(figsize=(2,3))
plt.subplot(231)
plt.title('Original')
plt.imshow(A, cmap='gray')

plt.subplot(232)
plt.title('Derivada en X')
plt.imshow(RX, cmap='gray')

plt.subplot(233)
plt.title('Derivada en Y')
plt.imshow(RY, cmap='gray')

plt.subplot(234)
plt.title('R')
plt.imshow(R, cmap='gray')

plt.subplot(235)
plt.title('Border')
plt.imshow(B, cmap='gray')


plt.show()

print(time.process_time() - start)