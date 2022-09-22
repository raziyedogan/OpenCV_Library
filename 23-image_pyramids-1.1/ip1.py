"""
Yüz tanıma ya da herhangi bir nesne tanıma işlemi yapacağımız zaman her zaman nesne aynı boyutta olmayabiliyor. 
Resmin boyutu değiştiği zaman o resmi tanıyabilmemiz için belli pikselleri büyültme veya küçültme işlemleri 
yapabiliyoruz. Bu derstede bu işlemleri gerçekleştireceğiz. 2 kat büyültme ve 2 kat küçültme işlemini 
gerçekleştirciğimiz kodu yazalım.
"""

import cv2
import numpy as np

resim = cv2.imread("n.jpg")

#Resmi 2 kat büyütelim ve yeni resmi ikikat isimli değişkene atayalım:

ikikat = cv2.pyrUp(resim)

# Bu işlem için pyrUp() fonksiyonunu kullanırız.
#1.parametre: hangi resmi iki kat büyütmek istediğimizin bilgisidir.

#pyrUp() fonksiyonu genişliğinden iki kat, boyundan iki kat olmak üzere resmi büyültmektedir.

#İki resminde shape ile genişliğini, yüksekliğini, kanal sayısını elde edelim.
#2 kat genişlikten ve  2 kat yükseklikten büyüdüğünü görelim:
print("Orjinal resim",resim.shape)
print("iki kat büyütülen resim",ikikat.shape)

cv2.imshow("Orjinal resim",resim)
cv2.imshow("iki kat buyuk resim",ikikat)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
OUTPUT:
Orjinal resim (560, 420, 3)
iki kat büyütülen resim (1120, 840, 3)

!!!Herhangi bir grileştirme işlemi yapmadığımız için kanal sayısı aynı kalır. Genişlik ve yükseklik görüldüğü 
üzere 2 katına çıkmıştır.
"""