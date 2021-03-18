#Hacer buscador de color

import numpy as np
import cv2
from enum import Enum

#Conversión de color
# imghsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# cv2.inRange(imghsv, rago, rango)

# cv2.bitwise_and()

# cv2.findContours()

class Colors(Enum):
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    EXIT = 5

class ColorSearcher:

    OPTION = 0

    def __init__(self):
        self.camera = cv2.VideoCapture(0)
    
    def options(self):
         while(self.OPTION != Colors.EXIT):
            print("---Color searcher---")
            print("RED: 1")
            print("GREEN: 2")
            print("YELLOW: 3")
            print("BLUE: 4")
            print("EXIT: 5")
            self.OPTION = int(input("Choose an option: "))

            if self.OPTION == Colors.EXIT.value:
                exit()
            else:
                print("Choosed option:", self.OPTION)
                self.__processColor()

    def __processColor(self): 

        if self.OPTION == Colors.RED.value:
            lower_red = np.array([160,20,70])
            upper_red = np.array([190,255,255])
            self.__showColor(lower_red, upper_red)

        elif self.OPTION == Colors.GREEN.value:
            lower_green = np.array([25, 52, 72])
            upper_green = np.array([102, 255, 255])
            self.__showColor(lower_green, upper_green)

        elif self.OPTION == Colors.YELLOW.value:
            lower_yellow = np.array([20,100,100])
            upper_yellow = np.array([30,255,255])
            self.__showColor(lower_yellow, upper_yellow)

        elif self.OPTION == Colors.BLUE.value:
            lower_blue = np.array([94, 80, 2])
            upper_blue = np.array([126, 255, 255])
            self.__showColor(lower_blue, upper_blue)

    
    def __showColor(self, lower, upper):
        print('Showing...')
        while True:
            ret, image = self.camera.read()
            imghsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(imghsv, lower, upper)

            color_found = cv2.bitwise_and(image, image, mask=mask)

            # color_found = cv2.bitwise_and(imghsv, image)
            
            cv2.imshow('Color detected',color_found)
            cv2.imshow('Video', image)
            if cv2.waitKey(1)==ord('q'):
                exit()
                break
if __name__ == '__main__':
    colorSearcher = ColorSearcher()
    colorSearcher.options()
