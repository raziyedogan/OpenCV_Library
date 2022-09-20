import cv2
import numpy as np

resim = cv2.imread("23nisan.jpg")


kesit = resim[30:100,80:200]

#kesit değişkeninde tutulan bölgeyi resmin üzerinde istenilen bir yere yapıştırmak için gereken işlemler:

resim[0:70,0:120] = kesit

#1.parametre y dir. 0:70 ile sol üst baz alınarak 0 dan aşağıya doğru 70.piksele kadar iner.
#2.parametre x dir. 0:120 ile 0 dan 120 piksele kadar sağa doğru gider.
#Bu iki parametre ile kesit'in resmin hangi konumuna yapıştırılacağı belirlenmiştir.
# "= kesit" ifadesi ile de kesit isimli değişkende tutulan resmin 0:70,0:120 koordinatına yapıştırılması sağlanmıştır.

cv2.imshow("23 Nisan",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()


#!!! Resim bir yere yapıştırılırken, yapıştırılan yerin koordinat aralığı yapıştırılacak resmin boyutuna uymalıdır. 
#Yani yapıştırmak istenilen resim 100-30=70 -> y=70 ve 200-80=120 -> x=120 boyutundadır. 
#Bu durumda "resim[0:70,0:120] = kesit" ile 0 dan 70 e kadarki alan y için ve 0 dan 120 ye kadarki
#alan x için belirlenmiştir. Böylece yapıştıılacak resmin boyutu ile tutarlı bir alan seçilmiştir.
