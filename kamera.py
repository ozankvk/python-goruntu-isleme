import cv2
import numpy as np


camera=cv2.VideoCapture(0)

while True:
    ret, foto=camera.read()
    hsv=cv2.cvtColor(foto,cv2.COLOR_BGR2HSV)
    lower_blue=np.array([100,60,60])
    upper_blue=np.array([140,255,255])



    maske=cv2.inRange(hsv, lower_blue, upper_blue)
    sonfoto=cv2.bitwise_and(foto, foto, mask=maske)
    cv2.imshow('orjinal foto', foto)
    cv2.imshow('maske foto', maske)
    cv2.imshow('son foto', sonfoto)


    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
camera.release()
cv2.destroyAllWindows()



laplace=cv2.Laplacian(foto,cv2.cv_64F)
sobelX= cv2.Sobel(foto,cv2.CV_64F,1,0,ksize=5)
sobelY= cv2.Sobel(foto,cv2.CV_64F,0,1,ksize=5)



edges=cv2.Canny(foto,100,200)
cv2.imshow('Canny',edges)


