import cv2
import numpy as np

resim = cv2.imread("23nisan.jpg")

kesit = resim[30:100,80:200]

resim[0:70,0:120] = kesit

#Resme efekt sadece 1 renkte uygulanabilir gibi bir durum söz konusu değildir.
#Hem green hemde red tonlarında efekt uygulanmak istenirse:

resim[: , : , 1] = 255
resim[: , : , 2] = 255

cv2.imshow("23 Nisan",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()