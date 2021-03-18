import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

start = time.process_time()

A = (cv2.imread('./images/CAT.png', 0)).astype(np.float) # 0 cambia a escala de grises
rows, columns = A.shape

R = np.zeros(A.shape, dtype=float)
for x in range(1,rows - 1):
    for y in range(1,columns - 1):
         R[x,y] = (A[x-1, y-1] + A[x, y-1] + A[x-1, y] + A[x,y])/4

plt.figure(figsize=(2,1))
plt.subplot(211)
plt.imshow(A, cmap='gray')
plt.subplot(212)
plt.imshow(R.astype(np.uint8), cmap='gray')
plt.show()

print(time.process_time() - start)