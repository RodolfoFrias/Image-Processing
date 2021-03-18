import numpy as np
import cv2
from claseFFmpeg import FFmpegVideoCapture
w = 1280
h = 720
n=3
#cap = cv2.VideoCapture("CarsDrivingUnderBridge.mp4")
cap = FFmpegVideoCapture("CarsDrivingUnderBridge.mp4",w,h,"gray")
    #kernel = np.ones((n,n),np.float)/n
    #kernel = np.array([(1,4 ,6 ,4, 1),
#                  (4,16,24,16,4),
#                  (6,24,36,24,6),
#                  (4,16,24,16,4),
#                  (1,4 ,6 ,4, 1)])
while(True):
    ret, frame = cap.read()
  #  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  #  filtro = cv2.filter2D(gray,-1,kernel=kernel)
 #   filtro.astype(np.uint8)
    #ret, thresh = cv2.threshold(gray, 100, 200, 0)
    #contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contours, -1, (0,255,0), 3)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()