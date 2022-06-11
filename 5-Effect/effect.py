import cv2
import numpy as np

kemalsunal1 = cv2.imread("saban.jpg")

kemalsunal1[:,:,0]=255   

cv2.imshow("SABAN_BLUE",kemalsunal1)

"""
3.parametre BGR kısmıdır. Ve BGR kısmına 0 dediğimizde B (Blue) kısmı aktifleşir.
Resme 255 tonunda mavi bir efekt ekledik.
"""

kemalsunal2 = cv2.imread("saban.jpg")
kemalsunal2[:,:,1]=255 

cv2.imshow("SABAN_GREEN",kemalsunal2)

"""
3.parametreye 1 dediğimiz için BGR 'ın green kısmını ifade etmiş olduk.
Bu durumda resme 255 tonunda yeşil bir efekt vermiş olucaz.
"""

kemalsunal3 = cv2.imread("saban.jpg")
kemalsunal3[:,:,2]=255 

cv2.imshow("SABAN_RED",kemalsunal3)

"""
3.parametreye 2 dediğimiz için BGR 'ın red kısmını ifade etmiş olduk.
Bu durumda resme 255 tonunda kırmızı bir efekt vermiş olucaz.
"""

cv2.waitKey(0)
cv2.DestroyAllWindows() 

"""
Mesela 'kemalsunal[:,:,1]' ifadesinde 3.parametre BGR 'ı ifade eder. 
1. ve 2. parametrelere bir değer girmediğimiz için resmin tamamına efekt uygular. Ama bu parametrelere değer 
verirsek belirli bir kısma efekt eklemiş oluruz.
"""