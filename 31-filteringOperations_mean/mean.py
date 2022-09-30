#Filtreleme görüntü işlemede yaygın olarak kullanılır. Görüntüdeki istenmeyen özelliklerin kaldırılmasını sağlar. 
#Farklı filtreleme tekniklerinin gürültüyü gidermede veya görüntünün belli yerlerini belirginleştirme gibi kendine 
#özel işlevleri vardır. 
#Peki gürültü giderme nedir? : Gürültüde görüntüyü kirleten veya görüntünün kalitesini düşüren harici kaynaklardan 
#oluşan etkidir. Bir çok farklı nedenden dolayı gürültülü görüntüler olabilir. 

#Görüntüyü yumuşatmak için filtreler vardır. Bunlar: Mean filtering (ortalama filtresi), gausing filter, 
#median filter'dır. 

#Resimler piksellerden oluşur ve her bir pikselin arka tarafta 0 ile 255 arasında değişen matrissel bir değeri vardır. 

#MEAN FILTERING

#Mean filtering sayesinde bir yumuşatma yapılıyor ve böylece gürültünün giderilmesi sağlanıyor. Mean filtresi, 
#doğrusal bir filtredir. Mean filtresine, yaygın olarak ortalama filtresi de denir. 

#Mean filtering'in 3x3 lük, 5x5 lik, 7x7 lik şablonları bulunmaktadır. Yani matris üzerinde 3x3 lük bir alan alınır 
#veya 5x5 lik bir alan alınır veya 7x7 lik bir alan alınır. Mean filtering'in yaptığı şey, şablon içerisinde 
#(bulunulan alan içerisinde) komşu piksellerin ortalamasını alarak ortalama işlemidir. Yani içinde bulunulan 
#alanlardaki değerlerin ortalaması alınır ve elde edilen sonuç, yeni görüntüde yani bulanıklaştıracağımız, 
#yumuşatacağımız görüntüde o an içinde bulunulan alanın ortasındaki indise yazılır. Sonra orjinal görüntüye ait 
#matriste bir yana kayılarak şablonumuz 3x3 lük ise 3x3 lük alan içerisinde tekrar aynı ortalama alma işlemi yapılır 
#ve sonra yeni görüntüdede bir sola kayarak şablon kadarlık alan içerisindeki orta yerdeki indise elde edilen 
#ortalama değeri yazılır.


#3x3 LÜK ŞABLON KULLANILARAK MEAN FILTERING KODU:

import cv2

#Resme filtreleme işlemi yapabilmek için resmi çağırmamız gerek:

image = cv2.imread("ev.jpeg")

#Gürültülü resme mean filtresini uygulayalım ve elde edilecek yeni resmi meanFilter  isimli değişkene atayalım:

meanFilter = cv2.blur(image,(3,3))

#mean filter işleminde blur() fonksiyonu kullanılır. 
#1.parametre: İşlem yapacağımız resim bilgisidir.
#2.parametre: Kaça kaçlık şablon kullanılacağı bilgisidir. Şablon dediğimiz şey, matris üzerinde 
#gezinirken belli sayıda bir alan kapsanarak geziniyor ve kapsanan alan içindeki değerlerin
#ortalaması alınıyor. Şablon 3x3, 5x5 ya da 7x7 olabilir. (3,3) diyerek 3x3 lük bir alan
#yani orijinal matrisin 3x3 lük kısmını kapsayacak şekilde 1 piksel kayarak gezinilir. 

#5x5 LİK BİR ŞABLON KULLANARAK MEAN FILTER KODU:

#Gürültülü resme mean filtresini uygulayalım ve elde edilecek yeni resmi meanFilter2 isimli değişkene atalım:

meanFilter2 = cv2.blur(image,(5,5)) 

#3x3 lük şablona göre 5x5 lik bir şablon kullandığımız zaman daha yumuşak bir görüntü elde ediyoruz. 
#!!!! Yani şablonu ne kadar büyütürsek yumuşama o kadar fazla oluyor.




#7x7 LİK BİR ŞABLON KULLANARAK MEAN FILTER KODU:

#Gürültülü resme mean filtresini uygulayalım ve elde edilecek yeni resmi meanFilter3 isimli değişkene atalım:

meanFilter3 = cv2.blur(image,(7,7)) 

cv2.imshow("Orijinal Resim",image)

#mean filter yaptığımız resimleri çağıralım:

cv2.imshow("3x3 SABLON KULLANILAN MEAN FILTER",meanFilter)
cv2.imshow("5x5 SABLON KULLANILAN MEAN FILTER",meanFilter2)
cv2.imshow("7x7 SABLON KULLANILAN MEAN FILTER",meanFilter3)

cv2.waitKey(0)
cv2.destroyAllWindows()



#!! Görüldüğü üzere 7x7 lik şablon kullandığımızda resimde daha fazla yumuşama olmaktadır. Ve hatta artık resmin 
#orijinalliği biraz daha bozulmaya başlamıştır ve kenarlar kaybolmuştur.