import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

start = time.process_time()

A = cv2.imread('./images/CAT.png', 0) # 0 cambia a escala de grises

# kernel = np.array([(1,1),(1,1)])*(1/4)
# kernel = np.one([dim, dim], )
kernelPrewittX = np.array([(-1, 0, 1), (-1,0,1), (-1, 0, 1)])
# R = cv2.filter2D(A,-1, kernel)
R = cv2.filter2D(A,-1, kernelPrewittX)


plt.figure(figsize=(2,1))
plt.subplot(211)
plt.imshow(A, cmap='gray')
plt.subplot(212)
plt.imshow(R, cmap='gray')
plt.show()

print(time.process_time() - start)