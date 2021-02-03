import numpy as np
from matplotlib import pyplot as plt

matriz = np.array([[1,2,3,4],[3,4,5,6], [7,8,9,10]])

matriz2 = matriz * 100

print(matriz2)

plt.figure(figsize=(1,2)) #filas columnas

plt.subplot(311)
plt.title('Matriz 2')
plt.imshow(matriz2)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j])


plt.show()