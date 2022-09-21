import cv2
import numpy as np

resim = cv2.imread("adilenasit.jpg")

#Aynalama işlemi gerçekleştirelim. 
# Aynı resmi, resmin üstünde sağında solunda aşağısında vs. aynalamak için gerekli işlemler:

#Resmi aynalama işlemleri yeni bir değişkenin içerisine atamalıyız.

aynalananResim = cv2.copyMakeBorder(resim,75,75,125,125,cv2.BORDER_REFLECT)

#Uzatmada, aynalamada, tekrak etme ve sarmalamada hepsinde cv2.copyMakeBorder() fonksiyonunu kullanırız.
#Bu fonksiyon ile sınır yapacağımı ve bunu kopyalayacağımı söylüyorum. 
#Bir uzatma yaptığımız zaman da aslında ekstra bir sınır yapıyorum. Ya da aynalama, tekrar etme, sarmalama yaptığım 
#zaman hepsinde bir border yani çerçeve, sınır yaptığım için kullanacağımız fonksiyon copyMakeBorder() dır.

#1.parametre: hangi resmi aynalamak istediğimiz bilgisidir.
#2.parametre: top (üst) sınır değeri (boyutu yani)
#3.parametre: bottom (alt) sınır değeri (boyutu yani)
#4.parametre: left (sol) sınır değeri (boyutu yani)
#5.parametre: right (sağ) sınır değeri (boyutu yani)
#2,3,4,5. parametreler ile resmin boyutu belirlenmiş olur.
#6.parametre: cv2.BORDER_REFLECT ile yansıtma yapacağız. Aynalama da zaten yansıtmadır. 
#Üste, alta, sağa, sola yansıtma yaparız. Yani BORDER_REFLECT ile sınırları, kenarlıkları tekrarla dedik.
#Aynalama işlemi yapacağımız için tekrarla dedik. BORDER_REFLECT aynalanan resme özel bir durumdur.
#Üst ve alt kısımlara resmin 75 pikselini ekledim. Sağ ve sol kısımlara resmimin 125 pikselini ekledim.


cv2.imshow("Aynalanan Adile Nasit Resmi",aynalananResim) 
#aynalanan resmi görebilmek için ilgili değişken çağrılmıştır.

cv2.waitKey(0)
cv2.destroyAllWindows()