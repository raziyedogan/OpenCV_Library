"""
Resim içerisinde belli bil bögeyi dikdörtgen içerisine almak istersek yapılması gerekenler şu şekildedir:
Öncelikle oluşturacağımız dikdörtgende sol alt köşeyi bulmalıyız. Bunun x ve y değerini bulmamız gerekiyor.
Önceden işlemleri y x şeklinde yapmıştık. y ile aşağıyı, x ile sağı kontrol ediyorduk. Burada ise sanki 
dikdörtgeni çizmişiz gibi düşündüğümüz için x y olarak düşünmeliyiz. X üstü, y solu ifade ediyor. Sonra da sağ üst 
köşeyi bulmalıyız. Aynı şekilde x y yi bulmalıyız. Sol altı ve sağ üst köşeyi bulduğumuz zaman aslında dikdörtgeni 
oluşturmuş oluyoruz.
Yani burda anlamamız gereken mantık şudur: bir dikdörtgen oluştururken önce sol alt köşesini, daha sonrasında 
sağ üst köşesini buluruz.


resim[:,:,0]=255  bu ifade ile 1. ve 2.parametreye bir şey yazmayarak tüm resmi kastettik ve BGR ın 0. değeri olan 
Blue tonuna 255 değerini verdik.
resim[50:100,230:310,0]=255 şeklinde köşeli parantez olduğunda ve bunu piksel bazında ayarladığımızda y x 
sıralamasında yaparız. 50:100 ile y ekseninde 50 pikselden 100.piksele kadar aşağı gider. 
230:310 ile x ekseninde 230.pikselden 310.piksele kadar sağar gider.
"""

import cv2
import numpy as np

resim = cv2.imread("h.jpg")

#bir resmin içerisinde bir dikdörtgen oluşturup bir alan almak istenmesi durumunda yapılması gerekenler:

cv2.rectangle(resim, (50,100), (150,30), [0,0,255],3)

#cv2.rectangle() ile bir dikdörtgen yapacağımızı belirtiyoruz.
#1.parametre: Hangi resmi kullanacağımızın bilgisidir.
#2.parametre: Sol alt köşeyi x y sıralamasında belirtiriz. 
#!!! () içerisinde değerler belirtilir. [] parantez kullansaydık y x sıralaması olurdu. Ama burada () kullanmamız 
#gerektiğinden x y sıralamasında değerler yazılır.
#3.parametre: Sağ üst köşeyi x y sıralamasında belirtiriz.
#4.parametre: Çizilecek dikdörtgene renk atanır. [B G R] şeklindedir.
#5.parametre: Çizilecek dikdörtgene kalınlık değeri verilir. 0 ile 9 arasındaki sayılar ile kalınlık değeri 
#belirtilir.


cv2.imshow("Hababam Sinifi",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()