import cv2
from matplotlib import pyplot as plt
import numpy as np

A = cv2.imread('./images/opencv.png')
B = cv2.imread('./images/CAT.png')

(umbral, Cbw) = cv2.threshold(B, 254, 255, cv2.THRESH_BINARY)

Cnot = cv2.bitwise_not(Cbw, None)
T1 = cv2.bitwise_and(B, Cnot, None)
T2 = cv2.bitwise_and(A, Cbw, None)
R = cv2.bitwise_or(T1, T2, None)

cv2.imshow('C en BW', Cbw)
cv2.imshow('C not', Cnot)
cv2.imshow('T1', T1)
cv2.imshow('T2', T2)
cv2.imshow('Res', R)

cv2.waitKey(0)