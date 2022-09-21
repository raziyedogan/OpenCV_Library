import cv2
import numpy as np

resim = cv2.imread("h.jpg")

print(resim[50,50]) #Bu satır ile 50 piksel altta ve 50 piksel sağda bulunan BGR değeri yazdırılmıştır.

cv2.imshow("Hababam Sinifi",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()

#OUTPUT: [164 178 137]
#Çıktıdan anlaşılacağı üzere, 50 piksel aşağıda ve 50 piksel sağda yer alan pikselin rengi 164 tonunda blue değeri, 
#178 tonunda green değeri, 137 tonunda red değerinin karışımından oluşan bir renktir.