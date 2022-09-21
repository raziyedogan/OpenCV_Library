import re
import cv2
import numpy as np

resim = cv2.imread("adilenasit.jpg")

#Aynalama işlemi:
aynalananResim = cv2.copyMakeBorder(resim,75,75,125,125,cv2.BORDER_REFLECT)

#Resmi uzatma işlemi:
uzatilanResim = cv2.copyMakeBorder(resim, 120, 120, 120, 120, cv2.BORDER_REPLICATE)

#Resmi tekrar ettirme işlemi:
tekrarResim = cv2.copyMakeBorder(resim,100,100,100,100, cv2.BORDER_WRAP)

#Resmin etrafına sarma yapmak istersek yapılması gerekenler şu şekildedir:

#Sarma işlemi ile kenara bir border yapılır. Mesela bir renkli çerçeve tarzında bir şey yapılabilir.

sarilanResim = cv2.copyMakeBorder(resim,50, 50, 50, 50, cv2.BORDER_CONSTANT, value=(75,150,255))

#1.parametre: Hangi resme sarma işlemi uygulanacak bilgisidir.
#2.parametre: top (üst) boyutu belirleriz.
#3.parametre: bottom (alt) boyutu belirleriz.
#4.parametre: left (sol) boyutu belirleriz.
#5.parametre: right (sağ) boyutu belirleriz.
#6.parametre: Sarma işleminde cv2.BORDER_CONSTANT kullanılır. CONSTANT sabit demektir.
#7.parametre: value=(75,150,255) şeklinde ekleyeceğimiz çerçevenin rengini ayarlarız.
# Blue tonu değeri 75, green tonu değeri 150 ve red tonu değeri 255 olarak belirledik. Böylece
#kenarlığa renk vermiş olduk.

#!!!!! Eğer "sarilanResim = cv2.copyMakeBorder(resim,50, 50, 50, 50, cv2.BORDER_CONSTANT)"" şeklinde
#olsaydı yani value değeri belirlemeseydik çerçeveye deafult olarak siyah rengi verilirdi.

cv2.imshow("Aynalanan Adile Nasit",aynalananResim)
cv2.imshow("Uzatılan Adile Nasit", uzatilanResim)
cv2.imshow("Tekrarlanan Adile Nasit",tekrarResim)
cv2.imshow("Sarilan Adile Nasit", sarilanResim)

cv2.waitKey(0)
cv2.destroyAllWindows() 