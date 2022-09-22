import cv2
import numpy as np

resim = cv2.imread("n.jpg")

#Resmi 2 kat büyütelim ve yeni resmi ikikat isimli değişkene atayalım:
ikikatbuyuk = cv2.pyrUp(resim)

#Resmi küçültmek istersek şöyle yaparız:
#Orjinal resmi küçülttüğümüz için yeni bir resim oluşur ve bu yüzden yeni bir değişkene atarız.

ikikatkucuk = cv2.pyrDown(resim)

#1.parametre: hangi resmi iki kat küçültmek istediğimizin bilgisidir.
#!!! 1.parametreye 2 kat büyültme gerçekleştirilen resim de yazılabilir. Eğer orijinal resme 2 kat büyültme işlemi
#uygulanan resmi, pyrDown ile iki kat küçültme işlemi yaparsak orijinal resmi elde ederiz.
#Orijinal resmin iki kat küçük halini görmek istediğimiz için 1.parametreye resim değişkenini yazdık.
#ikikatkucuk = cv2.pyrDown(resim) satırı ile yapılan: Orijinal resmi tutan resim değişkenini al,
#resmi iki kat küçült ve ikikatkucuk isimli değişkene at.

print("Orjinal resim",resim.shape)
print("iki kat buyutulen resim",ikikatbuyuk.shape)
print("iki kat kucultulen resim",ikikatkucuk.shape)

cv2.imshow("Orjinal resim",resim)
cv2.imshow("iki kat buyuk resim",ikikatbuyuk)
cv2.imshow("iki kat kucuk resim",ikikatkucuk)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
OUTPUT:
Orjinal resim (560, 420, 3)
iki kat buyutulen resim (1120, 840, 3)
iki kat kucultulen resim (280, 210, 3)

!!! Resimler renkli olduğu için 3 kanallıdır.
"""