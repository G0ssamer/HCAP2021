import cv2 
import numpy as np

#Cargar la imagen a color 
IRGB = cv2.imread('002.jpg')
print(IRGB)
print(IRGB.shape)
<<<<<<< HEAD
print("modificacion")
=======
print("Lineas agregadas en rama 2")
IGS = cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)
print(IGS)
print(IGS.shape)
>>>>>>> rama2
