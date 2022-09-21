import cv2
import numpy as np

resim = cv2.imread("23nisan.jpg")

kesit = resim[30:100,80:200]

resim[0:70,0:120] = kesit

#Spesifik bir alanın boyanması istenmesi durumunda yapılması gerekenler şu şekildedir:

resim[50:150, 60:120]=(0,150,255)

#y ekseninde 50.pikselden 150.piksele kadar gider. x ekseninde 60.pikselden 120.piksele kadar gider.
#(0,150,255) ifadesi ile 0 tonunda blue, 150 tonunda green ve 255 tonunda red karışımında bir renk belirtilmiştir.
#Ve bu renkler [50:150, 60:120] koordinatlarındaki alana atanmıştır.

cv2.imshow("23 Nisan",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()