import re
import cv2
import numpy as np

resim = cv2.imread("adilenasit.jpg")

#Aynalama işlemi:
aynalananResim = cv2.copyMakeBorder(resim,75,75,125,125,cv2.BORDER_REFLECT)

#Resmi uzatma işlemi:
uzatilanResim = cv2.copyMakeBorder(resim, 120, 120, 120, 120, cv2.BORDER_REPLICATE)

#Resmi tekrar ettirmek istersek yapılması gerekenler şu şekildedir:

tekrarResim = cv2.copyMakeBorder(resim,100,100,100,100, cv2.BORDER_WRAP)

#1.parametre: Hangi resme tekrar etme işlemi uygulanacak bilgisidir.
#2.parametre: top (üst) boyutu belirleriz.
#3.parametre: bottom (alt) boyutu belirleriz.
#4.parametre: left (sol) boyutu belirleriz.
#5.parametre: right (sağ) boyutu belirleriz.
#6.parametre: cv2.BORDER_WRAP ile yapılan: WRAP paketleme demektir. Paketleyip üste alta sola sağa
#aynı şekilde paketleyip gösterecektir.
#2.,3.,4.,5. parametrelere 100 değerini verdiğimiz için yukarı, aşağı, sola, sağa 100 birimlik alan verir.


cv2.imshow("Aynalanan Adile Nasit",aynalananResim) 
cv2.imshow("Uzatilan Adile Nasit", uzatilanResim)
cv2.imshow("Tekrarlanan Adile Nasit",tekrarResim)

cv2.waitKey(0)
cv2.destroyAllWindows()