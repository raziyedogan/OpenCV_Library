import cv2
import numpy as np

kemalsunal = cv2.imread("saban.jpg")

#Resmin belirli bir kısmına efekt uygulamak için yapılması gerekenler:

kemalsunal[50:100,40:90,0]=255

"""
1.parametre y parametresidir. y parametresinde 50. pikselden 100.piksele kadar bulunan kısmı belirttik.
2.parametre x parametresidir. x parametresinde 40. pikselden 90.piksele kadar bulunan kısmı belirttik.
3.parametre BGR parametresidir. 0 değeri ile Blue olacağını belirttik ve Blue tonuna 255 değerini atadık.
Böylece belirttiğimiz kısma mavi efekt uygulamış olduk.
"""

cv2.imshow("SABAN",kemalsunal)

cv2.waitKey(0)
cv2.DestroyAllWindows()