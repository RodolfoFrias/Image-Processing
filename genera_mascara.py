import cv2
import numpy as np
import sys
puntero = 50

def dibujarMascara(event,x,y,flag,param):
    global ix2,iy2,drawing, puntero
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix2,iy2 = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(Mascara,(x,y),puntero,(255,255,255),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing =False
        cv2.circle(Mascara,(x,y),puntero,(255,255,255),-1)
drawing = False   
alpha= 0.8
cap = cv2.imread('./images/foto.jpeg',0)
# captura = cv2.VideoCapture(sys.argv[1],0)
# ret, cap = captura.read()
Mascara = np.zeros(cap.shape,np.uint8)
cv2.namedWindow('Ventana')
cv2.setMouseCallback('Ventana',dibujarMascara)

overlay = cap.copy()
output =cap.copy()
cv2.addWeighted(overlay,alpha,Mascara,1-alpha,0,output)

while True:
    cv2.addWeighted(overlay,alpha,Mascara,1-alpha,0,output)
    cv2.imshow('Ventana',output)
    k = cv2.waitKey(1) & 0xff
    if k == ord('g'):
        cv2.imwrite('./images/imagen.jpg',Mascara)
        cv2.addWeighted(overlay,alpha,Mascara,1-alpha,0,output)
        break
cv2.destroyAllWindows()
captura.release()


