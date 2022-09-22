"""
Görüntü alıcaz ve görüntüyü yine bir değişkene atıcaz. 
Aslında videolar resimlerin bir bütünüdür. Örneğin resimlerin çekilme milisaniyesini daha kısa tutarsam daha akıcı 
bir video olur. Mesela 20 milisaniyede resim çekecek şekilde ayarlamış olalım. 20 milisaniyede bir sürekli 
resim çekilirse ve onları birleştirdiğimiz zaman aslında bir video elde ederiz. Ya da mesela 1 saniyede bir resim 
çek dersek bu daha kesik kesik bir video olur. O yüzden aslında burada anlamamız gereken mantık bir döngü 
oluşturduğumuzdur. Bu döngüde resimleri sürekli döndürüyor. Mesela 20 milisaniyede bir sürekli görüntüleri alıyor 
ve döndürüyor. Bu şekilde devam ediyor ve bu bir döngü içerisinde gerçekleşiyor.
"""

import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

#VideoCapture() fonksiyonu ile yapılan işlem kamera isimli değişkene atanmıştır. Bu fonksiyona 
#yazdığımız parametre önemlidir çünkü eğer parametreye 0 yazarsak kendi bilgisayarıma tanımlı olan
#kamerayı alır. Yani 0 yazdığımız zaman kendi bilgisayarımın kamerasını görüntü olarak açar.
#Eğer parametreye 1 yazarsak usb'de tanımlı olan kamerayı yani bir usb takarız ve orada tanımlı
#olan kamerayı alır. Eğer parametreye 2 yazarsak video'dan yani bir video alıp soldaki dosyaların
#olduğu yere yerleştirmişizdir ve o videodan görüntüleri almaktadır ya da direk video'nun
#adresini yazarak da video tanımlı olan kamerayı kullanacaktır.

#Örneğin  araba sayma işlemi olabilir ya da plakaları tanımlama olabilir, araba tanımlama, nesneleri tanımlama 
#ya da bir yolda insanları vs tanımlama gibi işlemler gerçekleştirilebilir .Bu direk canlı bir görüntü alarak 
#olabileceği gibi kayıtlı bir video üzerinden de işlemleri gerçekleştirebiliriz.

#Önceki derslerde resimle uğraşmak için öncelikle resmi imread ile tanımlama işlemi yapıyorduk ve
#burada da aynı şekilde kamerada görüntülerle uğraşmadan önce, öncelikle kameramızın nereden geldiğini
#hangi videoyu kullandığımızı belirtmemiz lazım. 
#Bu kısımda direk kendi bilgisayarımızın kamerasını kullanacağımızdan dolayı parametreye 0 yazarız.

#Şimdi bir döngü oluşturalım:
while True:
    ret, goruntu=kamera.read()

    #kameranın çalışıp çalışmadığını kontrol etmesi için ret isimli bir değişken oluşturduk.
    #goruntu isimli değişkeni oluşturma sebebimiz: Sürekli görüntü alıcak.Yani böyle tek tek 
    #görüntüler alıcak ve bunları benim belirlediğim milisaniye boyunca çekip birleştirdiği
    #için bir while yani bir döngü içerisinde çekiyor. Mesela 20 milisaniye sonra bir tane daha
    #çekiyor sonra 20 milisaniye sonra bir tane daha çekiyor... ve bunları sürekli
    #birleştirdiği zaman aslında bir video elde etmiş oluyoruz.  
    #kamera = cv2.VideoCapture(0) satırı ile videonun kendi bilgisayarımdan alınacağını söyledim
    #ve bunu kamera isimli değişkenin içerisine atadım. Bunu goruntu=kamera.read() şeklinde 
    #burada tanımlatırız. Aslında ben cv2.VideoCapture(0) satırı ile kendi bilgisayarımdan alıcak
    #dedik ve bunuda kamera değişkenini içerisine attım. Döngü içerisindede goruntu=kamera.read()
    #satırı ile bunu okutturuyoruz. Yani sürekli döngü içerisinde bunu okucak. Dicek ki kendi
    #bilgisayarımda tanımlattığım kamerayı oku, görüntüyü al, çalışıp çalışmadığını kontrol et
    #vs. şeklinde sürekli döngü dönecek. 
    #Bu arka planda dönüyor olabilir. Bizim birde bunu göstermemiz gerek. Bunu da imshow 
    #fonksiyonu ile yaparız:

    cv2.imshow("ozengineer",goruntu)
    
    #ilk parametre pencerenin sol üt köşesinde görünecek isimdir. İkinci parametre ise neyi göstermek
    #istediğimizdir. kamerayı tanımlattık, kameramı okuttum ve burda göstereceğim şey "goruntu" dür.
    #Görüntüyü gösteriyoruz ama görüntünün bir video olması için bunu bir döngü içerisine
    #yerleştirdiğim için bir döngü olması lazım ve bunun içinde örneğin 30 milisaniyede bir sürekli
    #çekim yapsın yani resmi çeksin birleştirsin, çeksin birleştirsin... Bunun içinde şart 
    #sunarız:

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

      #cv2.waitKey(30) ile 30 milisaniyede bir görüntüleri yani resimleri çek diyoruz. 
      #"0xFF == ord('q')" ile de hangi tuşa basıldığında çıkılması gerektiğini belirttik. 0xFF ifadesi çıkış demektir
      #ve çıkışım eşit ise q ya if çalışır ve if içerisinde break ile çıkış sağlanır.
      #Böylece döngünün bitiş şartını da belirtmiş olduk.

      #Bir döngüye giriyoruz 30 milisaniyede bir görüntü çekiyor ve q ya basılmadıysa
      #break a uğramıyor, tekrar döngüye giriyor. "goruntu" yü alıyor kamerayı okutuyor, 
      #o görüntüyü gösteriyor 30 milisaniyede tekrar okuyor ve q ya basılmadıysa tekrar döngüye
      #giriyor. Ta ki 30 milisaniye oldu ve q ya basıldı o zaman döngüye tekrar girmez ve break
      #diyerek çıkış yapar.

#Daha sonra çıkış yaptığımızda:
kamera.release()   #kamerayı release ile serbest bırakmalıyız. Yani artık kamerayı okutmuyoruz.

#Ve son olarakta yine bitiş olan şu ifadeyi yazarız:
cv2.destroyAllWindows()

"""
KODU OKUYALIM:
kamera = cv2.VideoCapture(0) satırı ile: Videonun nasıl alınacağını belirttik. Ve bunuda kamera isimli değişkene 
atadık.
Daha sonrasında bir video zaten görüntülerden oluştuğu için "while True:" şeklinde bir döngü oluşturduk. Bu döngü 
içerisinde birden fazla görüntü çekilecek.
"if cv2.waitKey(30) & 0xFF == ('q'):" satırında milisaniyeyi 30 olarak belirledik. Böylece video kesik kesik 
olmayacaktır. Mesela 30 yerine 300 gibi daha büyük bir sayı yazsaydık 300 milisaniyede bir görüntü çekilecekti ve 
daha yavaş olucaktır. 
"ret, goruntu=kamera.read()" satırında kamerayı okuyor ve goruntu değişkenine atıyor. ret ile de kameranın çalışıp 
çalışmadığını kontrol ediyor.
Daha sonra da "cv2.imshow("ozengineer",goruntu)" satırı ile görüntüyü bize gösteriyor.
Döngünün içerisinde bulunan 
if cv2.waitKey(30) & 0xFF == ('q'):
        break
koşulu ile 30 milisaniyede bir olacağını belirttik. 30 milisaniye olduysa ve çıkışı belirten 0xFF i kullanıyoruz 
ve 0xFF, q ya eşit ise yani q ya basıldıysa if bloğu çalışır ve break ile çıkış yapılır. Eğer q ya basılmadıysa 
döngü tekrar çalışır yani videoyu devam ettiriyor. Döngünün tekrar çalışma sebebi videoyu devam ettirmesidir.
break ile çıkış yapıldığında kamera.release() satırına gelinir ve bu satır ile kamera serbest bırakılır.
"""