#Numpy modülü ile metin kutusu oluşturabilmemiz mümkündür.

import cv2
import numpy as np

#Öncelikle yüksekliğini, genişliğini, kanal sayısını belirlediğimiz ve data type'ını belirlediğimiz
#bir yapı oluşturacağız. Daha sonra bunun üzerinde metin kutusu oluşturucağız.

resim = np.zeros((500,500,3),dtype="uint8")

#Bir metin kutusu oluşturalım:
cv2.putText(resim,"RAZIYE DOGAN",(100,200),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)
#metin kutusu oluşturmak için putText() fonksiyonunu kullanırız.
#1.parametre: Hangi resmi kullancağımız bilgisidir.
#2.parametre: Metin olarak ne yazacağımızın belirlendiği parametredir.
#3.parametre: Bu parametre ile yazımızın başlangıç pikseli belirlenir. Yani metnin nereden başlayacağı bilgisi belirlenir.
#4.parametre: Yazı tipi özelliği belirlenir.
#5.parametre: Yazının boyutu ayarlanır.
#6.parametre: Renk ataması yapılır. 
#7.parametre: Kalınlık ayarı yapılır.

cv2.imshow("deneme",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()

#! Normal parantezde (x,y) sıralamasında değer verilir.
