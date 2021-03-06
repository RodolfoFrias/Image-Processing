import cv2
import numpy as np
from matplotlib import pyplot as plt
class Histogram:

    OPTION = 0
    SUMA = 1
    RESTA = 2
    MULTIPLICACION = 3
    DIVISION = 4
    NORMAL = 5
    EXIT = 6
    VALUE = 10

    def __init__(self):
        self.image_ = cv2.imread('./images/foto.png', 0)
        self.image = cv2.cvtColor(self.image_, cv2.COLOR_BGR2RGB)

    def options(self):
        while(self.OPTION != self.EXIT):
            print("---HISTOGRAM---")
            print("Suma: 1")
            print("Resta: 2")
            print("Multiplicacón: 3")
            print("División: 4")
            print("Normal: 5")
            print("Exit: 6")
            self.OPTION = int(input("Elige un opción: "))

            if self.OPTION == self.EXIT:
                exit()
            elif self.OPTION == self.NORMAL:
                self.show()
            else:
                self.VALUE = int(input("Valor: "))

                print("Opción elegida:", self.OPTION)
                self.process_option()

    def process_option(self):
        for i in range(len(self.image)):
            for j in range(len(self.image[i])):
                self.image[i][j] = self.operation(self.image[i][j])
        print('Mostrando histograma...')
        self.show()
        

    def show(self):
        hist, bins = np.histogram(self.image.flatten(), 256, [0, 256])
        plt.plot(hist)
        plt.show()
        self.show_image()
    
    def show_image(self):
        plt.imshow(self.image)
        plt.show()

    def operation(self, image):
        if self.OPTION == self.SUMA:
            return image + self.VALUE
        elif self.OPTION == self.RESTA:
            return image - self.VALUE
        elif self.OPTION == self.MULTIPLICACION:
            return image * self.VALUE
        elif self.OPTION == self.DIVISION:
            return image / self.VALUE

if __name__ == '__main__':
    histo = Histogram()
    histo.options()
