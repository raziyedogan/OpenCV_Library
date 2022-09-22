#numpy sınıfını kullanacağız.

from pickletools import uint1
import cv2
import numpy as np

# "as" isim değiştirmek için kullanılır. numpy ismine np takma ismini verdik ve numpy kütüphanesini
#çağırmak istediğimizde np ismini kullanarak çağırma işlemini yapabiliriz.

#numpy modülünden zeros fonksiyonunu kullanacağız. zeros fonksiyonu bir matris döndürmektedir.
#Aslında birden fazla liste elemanı tutan bir yapı tutuyor. İlk parametre olarak boyutlarını ve kaç
#kanaldan oluşmasını istediğimizi yazıyoruz. 2.parametre de ise saklayacağımız değerin ne olduğunu
#istiyor. Yani parametre olarak shape ve datatype istiyor.
 
resim = np.zeros((300,300,3), dtype="uint8")

#1.parametre: shape değerini yani şeklini istiyor. Yani yüksekliği, genişliği, kanal sayısı değerlerini
#ister. (300,300,3) ile 300 yüksekliği, 300 genişliği ve 3 tane kanal sayısı olan yani bgr 
#değerleri olan bir şekil oluşturduk. Arka planda bunu bir liste olarak döndürecek. Bizim
#karşımızada bir matris olarak çıkaracak.
#2.parametre: data type'ını istiyor. dtype="uint8" yazarız çünkü: 0 ile 255 arasında kullandığımız
#için 8 olucak şekilde uint8 deriz.

#resim = np.zeros((300,300,3), dtype="uint8") satır ile yaptığımız: 300 yüksekliğinde, 300
#genişliğinde, 3 tane kanalı olan ve dtype'ı yani data type'ı uint8 olan bir şekil oluşturulmuştur.
#Bu sefer elimizde bir resim yok, şekli kendimiz oluşturduk. Kendi oluşturduğumuz resmin 
#görüntüsünü göremem. Ancak arka planda dönen işlemleri görebilirim:

#Oluşturduğum şekli resim isimli değişkene atadım. O yüzden print içerisine "resim" yazarız:
print(resim)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
OUTPUT:
[[[0 0 0]
  [0 0 0]
  [0 0 0]
  ...    
  [0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]
  ...
  [0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]
  ...
  [0 0 0]
  [0 0 0]
  [0 0 0]]

 ...

 [[0 0 0]
  [0 0 0]
  [0 0 0]
  ...
  [0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]
  ...
  [0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]
  ...
  [0 0 0]
  [0 0 0]
  [0 0 0]]]
  
Çıktıda görüldüğü üzere 0'lardan oluşan matrisler döndürdü. Tüm matris değerlerinin 0 olma sebebi, numpy'in zeros 
fonksiyonundan dolayıdır. Zeros fonksiyonu tüm elemanları 0 içeren bir matris oluşturur. 
300 genişliğinde, 300 yüksekliğinde bir matris oluşturduk fakat indekslerde görüldüğü üzere BGR değerleri hep 0 dır.
[0 0 0] şeklinde Blue 0, Green 0, Red 0 dır.
Bunların hepsi 0 çünkü bir resim oluşturmadık. Sadece boş bir yapı oluşturduk. Bu yüzden matristeki tüm değerleri 
0 olarak aldık. 

Böylece numpy kullanarak zeros fonksiyonu ile shape ürettik yani boyut ürettik ve data tipini belirledik. 
print ile de terminalde bunun matrissel döngüsünü görmüş olduk.
"""