import cv2
import numpy as np

resim = cv2.imread("nowhite.png")

resim[50,30] = [255,255,255]   

"""
Yukarıdaki satır ile yapılan şudur: Resmin sol üst köşesi baz alınarak piksel hesapları yapılır. Burada [50,30] 
ile soldan 50 piksel aşağıya ve 30 piksel sağa gidilmiştir. Geldiğimiz noktadaki piksele, [255,255,255] değerleri 
verilerek beyaz renkte olması sağlanmıştır.
Böylece istediğimiz pikselin rengini, istediğimiz renk ile değiştirebilmemiz mümkündür.

Çıktıda nowhite.png resminde [50,30] konumundaki pikselin rengi değiştirilerek [255,255,255] değerlerinden dolayı 
beyaz renge boyanmıştır. Ve dikkat ederseniz, çıktıda [50,30] konumunda küçük bir beyaz nokta göreceksiniz.

"""

#Bir pikselden ziyade belli bir alana kadar boyanmasını istersek yapmamız gerekenler:

for i in range(100):    #Bir pikselden bir piksele kadar boyamak için for döngüsü kullanırız.
    resim[70,i] = [134,56,190] 

"""
For döngüsü ile yapılan şudur: Resmin sol üst köşesi baz alınarak 70 piksel aşağıya ve i piksel kadar 
sağa gelindiğinde buradaki piksel beyaza boyanır. Burada i, 1 ile 100 aralığındaki değerleri alır.
"""

cv2.imshow("KARE",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()