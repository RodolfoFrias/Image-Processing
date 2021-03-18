import cv2
import numpy as np
from claseFFmpeg import FFmpegVideoCapture

capture = FFmpegVideoCapture('CarsDrivingUnderBridge.mp4', 1280,720, 'gray')
n = 2
# kernel = np.ones((n,n), np.float)/n

while(True):
    res, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # filtro = cv2.filter2D(gray,-1, kernel=kernel)
    # filtro.astype(np.uint8)
    cv2.imshow('Captura', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
