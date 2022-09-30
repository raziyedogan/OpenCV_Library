import cv2
import numpy as np

#Canlı görüntüye her seferinde şekilleri vs. ekleme işlemine dair kod gerçekleştirilmiştir.
#Peki bu işlemi nerede kullanabiliriz? : Yüz, araba gibi nesneleri algılama işlemleri için 
#canlı görüntüye şekil ekleme gerekebilmektedir.

kamera = cv2.VideoCapture(0)

#Görüntüleri döngü içerisinde sürekli alacağımız için bir döngü oluşturmalıyız:

while True:
    ret,goruntu=kamera.read()

    #Dikdörtgen ekleyelim:
    cv2.rectangle(goruntu,(100,100),(200,200),(25,36,98),3)
    #1.parametre: bu işlemin ne üzerine yapılacağı bilgisidir.
    #Video ilerlediği sürece bu şekli görüntüde tutmak için döngünün içerisinde yapıyoruz bu işlemi. Yani döngü 
    #döndüğü sürece rectangle görüntü içerisine çizilecektir.
    #2.parametre: rectangle nin sol üst köşesinin nereden başlayacağı bilgisidir.
    #3.parametre: rectangle nin sağ alt köşesi yani bitiş yerinin neresi olacağı bilgisidir.
    #4.parametre: color bilgisidir. (blue, green, red) şeklinde değerler verilir.
    #5.parametre: dikdörtgenin kalınlık bilgisidir.

    #Çizgi ekleyelim:
    cv2.line(goruntu,(0,0),(100,100),(0,0,255),2)
    #1.parametre: bu işlemin ne üzerine yapılacağı bilgisidir.
    #2.parametre: başlangıç noktası bilgisidir.
    #3.parametre: bitiş noktası bilgisidir.
    #4.parametre: color bilgisidir. (blue, green, red) şeklinde değerler verilir.
    #5.parametre: çizginin kalınlık bilgisidir.

    #Daire ekleyelim:
    cv2.circle(goruntu,(150,150),50,(80,150,35),2)
    #1.parametre: bu işlemin ne üzerine yapılacağı bilgisidir.
    #2.parametre: merkezinin neresi olacağı bilgisidir. Bu merkezin etrafına daire çizilecektir.
    #3.parametre: yarıçap bilgisidir. Yarıçap bilgisine göre daire çizilir. Burada yarıçapı 50 cm olarak 
    #belirlenmiştir. Böylece dairenin, dikdörtgenin içinde olması sağlanmıştır.
    #4.parametre: color bilgisidir. (blue, green, red) şeklinde değerler verilir.
    #5.parametre: dairenin kalınlık bilgisidir.

    #Text ekleyelim:
    cv2.putText(goruntu, "Raziye", (220,220), cv2.FONT_HERSHEY_DUPLEX,1,(200,0,0),2)
    #1.parametre: bu işlemin ne üzerine yapılacağı bilgisidir.
    #2.parametre: texte ne yazılacağı bilgisidir.
    #3.parametre: koordinat bilgisidir.
    #4.parametre: Font yani yazı tipi bilgisidir.
    #5.parametre: yazının boyut bilgisidir.
    #6.parametre: color bilgisidir. (blue, green, red) şeklinde değerler verilir.
    #7.parametre: kutunun kalınlık bilgisidir.


    cv2.imshow("Result",goruntu)

    if cv2.waitKey(25) & 0xFF==('q'):
        break
#Her 25 milisaniyede bir biz q ya basana kadar görüntü alınır.

#Şekilleri döngü içerisinde çizdirdiğimiz için q ya basılmadığı sürece yani çıkış yapılmadığı sürece
#şekillerde görünür.

kamera.release()    #kamera serbest bırakılır.

cv2.destroyAllWindows()