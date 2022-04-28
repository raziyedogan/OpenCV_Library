"""
OpenCV'de her bir piksel BGR olarak yani Blue, Green, Red şeklinde çalışır.
Bir pikselde 3 renk kanalı vardır. Bunların kombinasyonlarıylada görüntümüz yani resmimiz oluşur.
Yani Blue, Green, Red şekline ana 3 rengimiz var. Bunların 0 ile 255 arasındaki ayarlamaları ile 
tüm tonları elde edebiliyoruz. 
Peki neden 0 ile 255 arasında değerler kullanıyoruz?:
Bunun sebebi aynı anda fazla bellek tüketmeden net bir görüntü elde etmek için yeterli çözünürlüğe 
sahip olduğundan 0 ile 255 aralığı yeterlidir. Hem çok fazla bir bellek tüketimi olmuyor,
hem de netliği yeterli seviyede bir görüntü elde edilebildiği için BGR 0 ile 255 arasında kullanılır.

Aslında resimdeki her bir piksel 8 bitten oluşuyor. Ve bilgisayarda da görüntüler dahil bir çok şey 
aslında binary sistemde matematiksel olarak çalışırlar.
Bir noktada (pikselde) 8 bit kullanabiliyoruz. O halde bir noktada maksimum 8 tane 1 yazarsak: 
11111111 = 255 elde edilir.
Bu durumda bir piksele verebileceğimiz maksimum değer 255 tir.
Aynı şekilde bir piksele verebileceğimiz minimum değer: 00000000 = 0 'dır ve bu durumda bir piksele 
verebileceğimiz minimum değer 0 dır.
"""

#Her bir pikselinde bir matris olduğunu düşünürsek, resimde kaç matris olduğunu yani kaç piksel olduğunu öğrenelim:

import cv2  
import numpy as np

resim = cv2.imread("image.jpg")  #image.jpg resmini okuyup resim isimli değişkene attık.  
cv2.imshow("Street Lamps",resim) #resim isimli değişkeni çağırarak resmin ekranda gösterilmesini sağladık.

print(resim)    #Bu satır ile her bir pikselin matris görünümü elde edilir. Yani piksel olarak renklerini verir.

#Resmimiz output'ta görünen matrislerin toplamından oluşuyor. Outputta her bir pikselin matris yapısını görüyoruz. 
#Yani, resmin matrissel görünümü için: print(resim) satırı kullanılır.

cv2.waitKey(0)  
cv2.destroyAllWindows()