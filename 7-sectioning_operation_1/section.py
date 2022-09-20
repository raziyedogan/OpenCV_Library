import cv2
import numpy as np

resim = cv2.imread("23nisan.jpg")

#Bir resimden belirli bir bölüm alınmak istenirse yağılması gerekenler şu şekildedir:
#Resmin içerisinden bir bölge yani kesit alınacağı için yeni bir değişken tanımlanır. Ve tanımlanan 
#değişkene resimden alınan kısım atanır.

kesit = resim[30:100,80:200]

#Yukarıdaki satır ile ana resmin bir bölgesi kesit isimli değişken içerisine atanmıştır. Bu bölge resim isimli
# değişkende tutulan resim içerisindeki 50:150,300:400 konumundaki bölgedir. 50:150 kısmı y koordinatıdır ve
#300:400 kısmı x koordinatıdır.

cv2.imshow("Kesit Alani",kesit) #kesit alanının görünmesi için imshow metodu ile kesit isimli değişken çağrılmıştır.
cv2.imshow("23 Nisan",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()