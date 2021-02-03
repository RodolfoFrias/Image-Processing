import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('foto.jpeg')
image2 = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

red_image   = image2[:,:,0]
green_image = image2[:,:,1]
blue_image  = image2[:,:,1]

# cv2.waitKey()

plt.figure(figsize=(1,3)) #filas columnas
plt.subplot(311)
plt.title('Blue')
plt.imshow(blue_image, cmap="gray")

plt.subplot(312)
plt.title('Red')
plt.imshow(red_image, cmap='gray')

plt.subplot(313)
plt.title('Green')
plt.imshow(green_image, cmap='gray')

plt.show()