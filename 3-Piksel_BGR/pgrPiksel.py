import cv2
import numpy as np

kurtResmi = cv2.imread("kurt.jpg")

cv2.imshow("Kurt Resmi",kurtResmi)

#Sağdan ve soldan yerini ifade ettiğimiz herhangi bir pikselin BGR değerlerini görmek için yapmamız gerekenler:

print(kurtResmi[(230,80)])  #Resmin belli bir noktasını [()] şeklinde belirtiriz.

"""
Resmin sol köşesi baz alınarak aşağı doğru 230 ve sağa doğru 80 piksel gidildiğinde, o konumdaki pikseli 
belirtmiş olduk. Çıktıda ilgili pikselin BGR değerlerini görürüz.
"""

print("Resmin boyutu: " + str(kurtResmi.size))  

"""
Burada resmin boyut kısmını yani kurtResmi.size kısmını stringe çevirmeliyiz çünkü string bir şey yazdık ve devamını stringe 
çevirebilmek için str() fonksiyonunu kullanırız.
"""

print("Resmin Özellikleri: " + str(kurtResmi.shape))

print("Resmin Veri Tipi: " + str(kurtResmi.dtype))

cv2.waitKey(0)
cv2.destroyAllWindows()