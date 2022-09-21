import cv2
import numpy as np

resim = cv2.imread("23nisan.jpg")

kesit = resim[30:100,80:200]

resim[0:70,0:120] = kesit

#Resme efekt eklemek istenmesi durumunda yapılması gerekenler şu şekildedir:

resim[: , : , 0] = 255

#1.parametre yükseklik ve 2.parametre genişlik olduğu için bu kısımlar kullanılmamıştır ve ":" koyulmuştur.  
#Son parametreye 0 değeri verilmiştir ve 255'e eşitlenmiştir. Bu satırda yapılan işlem: Son parametre BGR'ın
#olduğu parametredir. Blue yani mavi rengi ile değişiklikler yapılacağından 0 değeri verilmiştir.
#yer alıyor. Green 1.indekste, Red 2.indekste yer alıyor. Burada resmin tamamına 255 tonunda mavi efekt uyguladık.
#Çünkü BGR ifadesine bakıldığında Blue 0.indekstedir. Efekt olarak 255 değeri verilmiştri. Yani mavinin en üst 
#tonu kullanılmıştır.

cv2.imshow("23 Nisan",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()