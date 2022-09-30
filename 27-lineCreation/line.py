#Numpy modülü ile çizgi oluşturabilmemiz mümkündür.
#! Numpy array'ler opencv'de resimlerimizin matematiksel karşılığıdır. 

import cv2
import numpy as np

#Öncelikle yüksekliğini, genişliğini, kanal sayısını belirlediğimiz ve data type'ını belirlediğimiz
#bir yapı oluşturacağız. Daha sonra bunun üzerinde çizgi oluşturucağız.

resim = np.zeros((300,300,3),dtype="uint8")

#çizgi oluşturalım:
cv2.line(resim,(50,50),(100,100),(20,60,255),3)
#çizgi oluşturmak için line() fonksiyonunu kullanırız.
#1.parametre: bu işlemin neyin üzerinde yapılacağı bilgisidir. Bir resim de olur, kendi oluşturduğumuz yapıda olur.
#2.parametre: Çizginin nereden başlayacağı bilgisidir. Her zaman sol üst köşeden başlar. Burada çizgimiz 50,50 den 
#başlayacak şekilde belirledik.
#3.parametre: Çizginin nereye kadar olacağı bilgisidir. Burada 100,100'e kadar gitsin şeklinde belirledik. 
#Yani y ekseninde 100 aşağı iniyor ve x ekseninde 100 sağa gidiyor. Ve bunların kesiştiği yere kadar bir çizgi 
#çekilecektir.
#4.parametre: color yani bgr değeri girilir.
#5.parametre: Bu parametre ile çizginin kalınlığı ayarlanır.

cv2.imshow("Line",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
