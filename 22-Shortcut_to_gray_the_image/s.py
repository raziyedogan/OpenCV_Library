import cv2
import numpy as np

#Resmi grileştirmenin basit yolu:

resim = cv2.imread("n.jpg",0)

cv2.imshow("Orijinal Natalie Portman Resmi",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()


"""
!! "resim = cv2.imread("n.jpg",0)" satırında 2.parametreye 0 değeri girildiğinde resmi grileştirme işlemi yapılmış 
olur. cv2.imread fonksiyonu ile resim alınmıştır ve anında burada grileştirilmiştir. Yani resim değişkeninin 
içerisine gri bir resim atanmıştır. 
Resmin orijinali ile işimiz yok ise, direk resmin gri haliyle işlemler yapacak isek bu yöntemi kullanabiliriz.
"""