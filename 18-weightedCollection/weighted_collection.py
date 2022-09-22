#Burada ele almamız gereken asıl konu resimlerdeki piksellerdir. Bu pikseller üst süte bindiği zaman ağırlıkları 
#toplanacaktır. 

"""
Örneğin, 
Resim1=[200,100,50]
şeklinde bir tane piksel verilsin. Blue kanalı 200, green kanalı 100, red kanalı 50 olan bir pikseldir.
Birde
Resim2=[100,50,210] şeklinde bir piksel daha tanımlanmış olsun. 

Örneğin üst üste geçmiş iki resim olabilir ya da farklı iki pikselleri toplamak isteyebiliriz. Ama piksel bazlı 
düşünmemiz lazım. Çünkü bir resimde bir çok piksel var ve her bir pikselin kendi renkleri doğrultusunda kanalları 
var. Bu yüzden de her birini piksel piksel düşünmemiz lazım. 
Burada yapacağımız şey şudur:
Her bir kanalı kendi içinde toplayacağız.
Örneğin: Resim1 in Blue kanalını Resim2 nin Blue kanalı ile, Resim1 in Green kanalını Resim2 nin Green kanalı ile 
ve Resim1 in Red kanalını Resim2 nin Red kanalı ile toplarız ve sonucu elde ederiz. Böylece yeni bir blue değeri, 
yeni bir green değeri, yeni bir red değeri elde ederiz. Yani yine 3 kanallı yeni bir piksel elde etmiş oluruz. Bu 
iki pikselin üst üste binmesinden oluşan yeni bir piksel elde etmiş oluruz. Ve bu pikselin değeri 0 ile 255 
arasında olmalıdır.
!!! Her bir kanal 0 ile 255 arasında değer alır. Bu yüzden iki pikseli toplama işlemi yaptığımız zaman eğer sonuç 
255 devrini tamamladıysa başa dönmesi gerekecektir. Yani şu şekilde:
Blue kanalını toplayalım: 200+100=300 dür. 255 devrini atladığı için sayacın başa döndüğünü düşünürüz. 300 den 
255 i çıkardığım zaman aslında başa dönüp 45 e gelmiş oluyor. Fakat 45 değeri, bgr değeri 1 den başlasaydı olurdu. 
bgr değeri 0 ile 255 aralığında olduğundan değer 0 dan başlar ve bu yüzden 0 dan başladığı için değerimiz 44 olur.
Eğer 1 den başlasaydı 45 olurdu. Yeni pikselin blue değeri 44 olur.
Green kanalını toplayalım: 100+50=150 dir. Zaten 255 devrini tamamlamadığı için yeni pikselin green değeri 150 olur.
Red kanalını toplayalım: 50+210 = 260 dır. 255 son doygunluk seviyesi olduğu için 260-255= 5 olur. Ve bgr değeri 
0 dan başladığı için yeni pikselin red değeri 4 olur.
"""

"""
Şimdi şu işlemi koda dökelim: İki resimden birer piksel seçeceğiz. Her bir pikselin 3 kanalı vardır. Kanallar kendi 
aralarında toplanarak yeni bir piksel elde edilecek ve böylece ağırlıklı toplamlarını bulmuş olacağız. 
"""

import cv2
import numpy as np

resim1 = cv2.imread("emelSayin.jpg")
resim2 = cv2.imread("turkanSoray.jpg")

#Öncelikle piksel belirtip terminale yazdıralım:

print(resim1[100,200])  #100 piksel aşağı gider ve sonra 200 piksel sağa gider. Gelinen konumdaki piksel alınır.

#Koordinat belirtirken y x sıralamasında belirtiriz.

print(resim2[150,230])

cv2.imshow("Emel Sayin",resim1)
cv2.imshow("Turkan Soray",resim2)

#Piksellerin toplam sonucunu terminalde görmemiz gerek bu yüzden toplama işlemini print içerisinde yaparız:

print(resim1[100,200]+resim2[150,230])

#print(resim1[100,200]) ve print(resim2[150,230]) satırlarını yazmak zorunda değiliz.
#print(resim1[100,200]) ve print(resim2[150,230]) satırlarını yazmamızdaki amaç, aldığımız 
#piksellerin BGR değerlerini görmektir. 
#print(resim1[100,200]+resim2[150,230])  satır ile toplama işlemi gerçekleştirilir.
#print(resim1[100,200]+resim2[150,230]) bu satır ile yapılan işlemler: resim1 de 100 piksel aşağı ve 
#200 piksel sağa git, geldiğin yerdeki pikseli al. Aynı şekilde resim2 de 150 piksel aşağı in ve
#230 piksel sağa git, geldiğin yerdeki pikseli al. Sonra aldığın bu pikselleri topla ve yazdır.

cv2.waitKey(0)
cv2.destroyAllWindows()