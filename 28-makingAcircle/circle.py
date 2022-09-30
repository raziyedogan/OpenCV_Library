#Numpy modülü ile daire oluşturabilmemiz mümkündür.

import cv2
import numpy as np

#Öncelikle yüksekliğini, genişliğini, kanal sayısını belirlediğimiz ve data type'ını belirlediğimiz
#bir yapı oluşturacağız. Daha sonra bunun üzerinde daire oluşturucağız.

resim = np.zeros((300,300,3),dtype="uint8")

#Daire oluşturalım:
cv2.circle(resim,(150,150),25,(0,255,0),2)
#circle() fonksiyonu ile daire oluşturulur.
#1.parametre: Bu işlemin neyin üzerinde yapılacağı bilgisidir. Bir resim de olur, kendi oluşturduğumuz yapıda olur.
#2.parametre: Dairenin merkezinin nerede olacağı bilgisidir. y ekseninde 150, x ekseninde 150 noktalarının 
#kesiştikleri yer dairenin merkezi olur.
#3.parametre: yarıçap değeridir. Yarıçap değerini verelim ki daireyi çizebilsin. Yani merkezi belirledik ve 
#yarıçapıda belirlersek bir daire çizilebilmesi mümkündür.
#4.parametre: color yani bgr değeri girilir.
#5.parametre: Çizginin kalınlığı ayarlanır.

cv2.imshow("deneme",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()