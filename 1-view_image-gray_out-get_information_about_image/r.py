import cv2  #opencv kütüphanesini import ettik.

"""
Görüntü işleme, bir görüntüyü elde etmek ya da elimizde bulunan görüntüden yararlı bilgiler çıkarmak 
için çeşitli algoritmalar kullanılarak görüntü üzerinde bazı işlemlerin gerçekleştirilmesi 
yöntemidir.

Görüntü işleme aslında matrisler üzerinde yapılan işlemler bütünüdür. Matrisler üzerinde bulunan her
bir hücreye piksel denir. Bu pikseller üzerinde sayısal değerler vardır. Her bir değer bir rengi 
temsil eder. Aslında pikseller üzerindeki sayıları renklere çevirerek görüntüyü elde etmiş oluyoruz.

Her bir matris hücresinde (pikseller üzerinde) bulunan sayılar, RGB (red, green, blue) renk uzayının 
0 ile 255 arasında değerleridir.
Temel olarak 3 renk vardır ve tüm renklerde aslında bu renklerin karışımından oluşmaktadır. 
Kırmızı, yeşil ve mavi renklerini belli oranlarda (0 ile 255 arasında) karıştırdığımız zaman 
tüm renklerin tüm tonlarını elde edebiliriz.
Bu durum resimlerin Kırmızı, yeşil ve mavi şeklinde 3 kanallı olmasından kaynaklanıyor. 
Kırmızının, yeşilin, mavinin sayısal değerlerine minimum 0, maksimum 255 olacak 
şekilde değerler vererek farklı tonlar elde edebiliriz.
"""

"""
Resmi neden grileştiririz? : rgb 3 kanallıdır. Resmi 3 kanallı yani resmi tamamen kendi 
renkleriyle kullanmamız yaptığımız sistemi yavaşlatabilir. Sonuçta 3 kanal kullanılıyor. Fakat 
resmi yada videoyu 3 kanallı değilde gri yani siyah beyaz kanal aralığında kullanmak bu konuda
avantaj sağlayabilir.
"""

#Şimdi bir resmin nasıl görüntüleneceğini, resmi gri tona nasıl dönüştüreceğimizi ve resim hakkında boyut, veri tipi, genişlik, yükseklik, kanal sayısı bilgilerini nasıl elde edeceğimizi inceleyelim:

resim1 = cv2.imread("image.jpg",0) #resmi 0 parametresi sayesinde grileştirdik. 0 parametresini görünce kanal kullanılmayacağını anlar. Yani siyah beyaz, tek kanallı bir resim elde eder.    
#imread fonksiyonunun yaptığı işlem şudur: parametre olarak resmi alıyor ve bir numpy array'ine dönüştürüyor. 

#Resmin görüntülenmesi için imshow() fonksiyonunu kullanmamız gerekir.
#imshow() fonksiyonu parametreleri:
#İlk parametre: resmin gözüktüğü pencerede yazacak ifade belirtilir.
#ikinci parametre: resmi, resim1 isimli değişkende tutuyoruz. Göstermek istediğimiz resim 'resim1' değişkeninde olduğu için 2.parametreye bu değişken yazılır.
cv2.imshow("Street Lamps",resim1) 

#Resmin boyutunu öğrenmek istersek:
print(resim1.size)    

#Resmin data tipini öğrenmek istersek:
print(resim1.dtype) 

#Resmin genişliğini, yüksekliğini ve kaç kanaldan oluştuğunu öğrenmek için:
print(resim1.shape)  

#Temel iskelet olarak kapanışta yazmamız gereken kodlar:
cv2.waitKey(0)  #Bu satır herhangi bir tuşa basmamızı bekler. Yani pencere açıldığı zaman o pencerenin kapanması için herhangi bir tuşa basılması beklenir.
cv2.destroyAllWindows() #Bu satır ile yapılan, çarpıya bastığımızda opencv ye bağlı tüm pencerelerin kapanması sağlanır. Yani resimle alakalı tüm kısımları kapatmış oluruz.
