import re
import cv2
import numpy as np

resim = cv2.imread("adilenasit.jpg")

#Aynalama:
aynalananResim = cv2.copyMakeBorder(resim,75,75,125,125,cv2.BORDER_REFLECT)

uzatilanResim = cv2.copyMakeBorder(resim, 120, 120, 120, 120, cv2.BORDER_REPLICATE)
#cv2.copyMakeBorder() fonksiyonunu kullanırız çünkü aynalama işleminde olduğu gibi yine sınırla bir işlem yapacağız.
#1.parametre: Hangi resme uzatma işlemi yapacağımızın bilgisidir.
#2.parametre: top (üst) boyutu belirleriz.
#3.parametre: bottom (alt) boyutu belirleriz.
#4.parametre: left (sol) boyutu belirleriz.
#5.parametre: right (sağ) boyutu belirleriz.
#6.parametre: cv2.BORDER_REPLICATE ile tekrarlama yapılır yani uzatıcağımız için tekrarla dedik.

cv2.imshow("Aynalanan Adile Nasit",aynalananResim) #aynalanan resmi görebilmek için ilgili değişken çağrılmıştır.
cv2.imshow("Uzatılan Adile Nasit", uzatilanResim) #uzatılan resmi görebilmek için ilgili değişken çağrılmıştır.

cv2.waitKey(0)
cv2.destroyAllWindows()