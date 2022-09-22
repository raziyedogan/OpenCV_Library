import imp
import cv2
import numpy as np

resim = cv2.imread("n.jpg")

#resmi grileştirme işlemi yapacağız. Bunun için 2 yol vardır. Birisı kısa diğeri ise uzun yoldur. 
#Öncelikle uzun yolu yapalım:
#resmi grileştirdiğimizde orjinal resimden farklı bir resim oluşturuyoruz. Bu yüzden yeni bir
#değişken oluşyurup yaptığımız gri resmi bu değişkene atarız.

resimGri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

#cv2.cvtColor() fonksiyonu ile renk dönüştürme sağlanır.
#1.parametre: Hangi resmi değiştireceğimizdir.
#2.parametre: Resim değişkenini cv2.COLOR_BGR2GRAY ile gray haline dönüştür işlemi sağlanmıştır.
# cv2.COLOR_BGR2GRAY ve cv2.cvtColor sayesinde resim grileştirilmiştir.

#Resimlerin kanal, yükseklik ve genişlik değerlerine bakalım:
#Hepsi aynı işlem içerisinde olacaksa tanımlamalar peşpeşe yapılabilir:

yukseklik,genislik,kanalsayisi = resim.shape #orjinal renkli resmin shape'i.

#.shape sayesinde resmin yüksekliğini, genişliğini ve kanal sayısını elde edebiliriz.
#shape sonucunda yükseklik değeri, genişlik değeri ve kanal sayısı değeri elde edilir. Bu yüzden
#3 tane değişken tanımladık. shape sonucu elde edilen yükseklik değerini yukselik isimli değişkene atar.
#shape sonucu elde edilen genislik değerini genislik isimli değişkene atar.
#shape sonucu elde edilen kanal sayisi değerini kanalsayisi isimli değişkene atar.
 
yukseklik1,genislik1 = resimGri.shape 

"""
! Resmi grileştirdiğimiz zaman kanal sayısı 1'e düşer. O yüzden shape sonucunda kanal sayısı değeri dönmez. 
Çünkü 1 zaten olabilecek en küçük kanal sayısıdır. Bu 1'i tutmadığı için kanal_sayısı diye bir değişken oluşturmayız.
Eğer böyle bir değişken oluşturursak hata alırız. Çünkü shape nin içerisinde sadece yükseklik ve genişlik degerleri
vardır.

!!! Grileştirme işlemi ile boyut değiştirilmez. Sadece kanal sayısı 1'e indirilir.

!!! Boyutlandırma alırsak orijinal resim, gri resmin 3 katı büyüklüğünde olur. Yani:
Orijinal resim: 560 x 420 x 3
Gri resim: 560 x 420
"""

print("Orijinal resmin degerleri: ", yukseklik,genislik,kanalsayisi)  
print("Gri resmin degerleri: ", yukseklik1,genislik1) 

cv2.imshow("Orijinal Natalie Portman Resmi",resim)
cv2.imshow("Grilestirilmis Natalie Portman Resmi",resimGri)

cv2.waitKey(0)
cv2.allDestroyWindows()


"""
!!!!! Orijinal resim ile resmin gri hali arasındaki fark şu şekildedir:
Orijinal resimde BGR kanallarını kullanırız. Ve resimlerin boyutu "yükseklik x genişlik x kanal_sayısı" dır. 
BGR değerleriyle yani resmi renkli bir şekilde kullandığımız zaman boyutun ve yüksekliğin çarpımını birde 3 katını 
olarak bir boyutlandırılması oluyor. Ancak resmi gri kanalda kullanırsak, gri kanalında kullanmak demek 3 kanaldan 
1 kanala düşürmek demektir. 1 kanala düşürdüğümüz zaman boyutlar aynı ancak renkli resimde 3 katı oluyordu, 
gri resim de ise renkli resmin boyutundan daha az olur. 
Neden grileştiriyoruz, neden boyutu küçültüyoruz? : Çünkü büyük boyutlu görüntülerle uğraşmamız gerektiğinde
sistemde daha ağır yüke sebep olacak şeyler istemeyiz. Olabildiğince küçültmeye çalışırız. 
Mesela zaten bir videodan  arabaları, plakaları vs. okumamız gerektiği durumda renkli olmasına gerek yoktur. Onu 
sadece tanımlayabilmesi yeterlidir. Bu yüzden 3 kanallı kullanmamız yüke sebep olacaktır.
"""