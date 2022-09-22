#Bir resim ile diğer resmi üst üste ekleme işlemleri gerçekleştirilmiştir. Bu işlem için her iki resmin boyutları 
#aynı olmalıdır. Çünkü üst üste ekleneceği için tüm piksellerin örtüşmesi gerekmektedir.

import cv2
import numpy as np

resim1 = cv2.imread("kemal_sunal.jpg")
resim2 = cv2.imread("tarik_akan.jpg")

cv2.imshow("KEMAL SUNAL",resim1)
cv2.imshow("TARIK AKAN",resim2)

toplam = cv2.add(resim1,resim2) #add fonksiyonu ile resim1 ve resim2 değişkenleri üst üste toplanır.
#toplam sonucu 'toplam' isimli değişkene atanır. Yeni bir değişkene atanma sebebi, bunlar üst üste 
#bindiği zaman yeni bir resim oluşmasıdır.

#toplam değişkenine atanan resmi görelim:
cv2.imshow("Toplanmis Resimler",toplam)

cv2.waitKey(0)
cv2.allDestryorWindows()