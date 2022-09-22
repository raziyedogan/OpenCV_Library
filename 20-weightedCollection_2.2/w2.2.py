import cv2
import numpy as np

#Resimleri belirli bir oranda ağırlıklı toplamak istersek, yapılması gerekenler şu şekildedir:

resim1 = cv2.imread("kemal_sunal.jpg")
resim2 = cv2.imread("tarik_akan.jpg")

cv2.imshow("KEMAL SUNAL",resim1)
cv2.imshow("TARIK AKAN",resim2)

toplam = cv2.add(resim1,resim2) 

#Oran verelim. tarik_akan resminden 0.3 oranında yani %30 luk bir görüntü saydamlığı olsun.
#kemal_sunal resminden de %70 oranında bir görüntü olsun. Şöyle yaparız:

agirliklitoplama = cv2.addWeighted(resim1,0.7,resim2,0.3,0)

#cv2.addWeighted() fonksiyonunu kullanırız çünkü ağırlıkları topluyoruz.
#1.parametre: Hangi resmi aldığımız bilgisidir.
#2.parametre: 1.parametrede aldığımız resmi hangi oranda istediğimiz bilgisidir.
#3.parametre: ikinci resim belirtilir.
#4.parametre: ikinci resimden hangi oranda kullanmak istediğimiz bilgisidir.
#!!!!Verdiğimiz oranların toplamı 1 olmak zorundadır: 0.7+0.3 = 1
#5.parametre: son parametrede her zaman 0 verilir.

cv2.imshow("Toplanmis Resimler",toplam)
cv2.imshow("Agirlikli Toplama Sonucu Resim",agirliklitoplama)

cv2.waitKey(0)
cv2.allDestryorWindows()