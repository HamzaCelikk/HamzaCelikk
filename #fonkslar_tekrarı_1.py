#fonkslar
#fonkslar,uzun işlem yerine daha kolay ve istenilince çağırılandır.

#Örnek_1:("fonks aynı şeyi tekrar tekrar yazmamızı engeller.")
def bilgiver():
    print("işlem Başarılı")
bilgiver()  #fonks çağırma.

#Örnek_2:
def selamla():
    print("merhaba")
selamla()  #fonks çağırma.

#Örnek_3:(Bir parametre verdik.)
def selamla2(isim):
    print("merhaba " + isim)
selamla2("Ali") #paremetrideki isimin ne olacağını belittik.

#Örnek_4:("a ve b değişkenini atayıp printte değerleri atayıp toplatırız.")
#2 parametre aldı.
def topla(a,b):
    print(a+b) 
topla(3,6) #a=3,b=6

#Örnek_5:(2 parametre ve daha gelişmiş.)
def topla_ve_carp(a,b):
    print(f"toplamı: {a+b}")

    print(f"çarpımı: {a*b}")
topla_ve_carp(3,6) #a=3,b=6

#Örnek_6:(parametre,listeler ve matematiksel işlemler.)
def ortalama_hesaplama(liste):
    toplam = sum(liste)     #sum() bir dizi veya listedeki tüm elemanalrı toplama
    print(f"Ortalama: {toplam/len(liste)}")  #len() listedeki eleman sayısını alır.
    #bir fonksiyonun sonucunu dışarıya döndürmek (geri göndermek) için kullanılır.

ortalama_hesaplama([ 1, 2, 3, 4, 5, 6, 7, 8 ]) #fonk çağırma ve değer döndürme.

#Örnek_7:("metinleri büyük harf yapma.")
def buyuk_harf_yap(metin): #bu kısım neler yapacağımızı yazdığımız kısım.
    metin=metin.upper() #metini büyük yaz dedik.
    print(metin) #yapılan işlemi ekrana yazdırdık.

buyuk_harf_yap("Merhaba,bugün günlerden perşembe.") #burası fonks çağırır ve en son verdiğimiz metini alır fonks içinde gerekli işlevi yapar.

#Örnek_8:
def kucuk_harf_yap(metin):
    metin=metin.lower()
    print(metin)

kucuk_harf_yap("Merhaba, bugün günlerden perşembe.")

#Örnek_9: 9,15,25
def  ilk_harf_buyuk_yap(metin):
    print(metin[0].upper() + metin[1:])  #metin[0] ilk harfi alır ve büyük harfe çevirir. metin[ 1:] metin'in 1. indexten sonuna kadar alır.


ilk_harf_buyuk_yap("merhaba, bugün günlerden perşembe.")  #ilk harfi büyük harfe çevirir.

#Örnek_10:
def kelimelerin_baş_harfini_büyük_yap(metin):
    kelimeler = metin.split()  # Metni kelimelere böler
    yeni_metin = ' '.join([kelime.capitalize() for kelime in kelimeler])  # Her kelimenin baş harfini büyütür
    print(yeni_metin)

kelimelerin_baş_harfini_büyük_yap("merhaba, bugün günlerden perşembe.")

#Örnek_11.1:
def selamla3(mesaj, isim="anonim"):
    print(f"{isim}, {mesaj}.")

selamla3("Selam")  # anonim isimli kişiye selam verdi.
#Örnek_11.2:
def selamla3(mesaj, isim="Ali"):
    print(f"{isim}, {mesaj}.")

selamla3("elif","Selam")
selamla3("Selam","elif")  # Ali yerine elif yazar isimli kişiye selam verdi.

#Örnek_12:
def indirim(fiyat,yüzde):
    indirim_tutari = fiyat * (yüzde / 100)
    fiyat_indirilmis = fiyat - indirim_tutari
    print(f"ürün fiyat:{fiyat}")
    if float(fiyat_indirilmis)<=0  :
        print("indirimli tutar:ücretsiz")
    elif float(fiyat_indirilmis)>0 :
        print(f"indirimli tutar:{fiyat_indirilmis}")
    print(f"İndirim oranı: {yüzde}%")

indirim(50, 90)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#RETURN İŞLEMLERİ(fonks içindekini başka yerlerde kullanma sağlama,tekrar döndürme.)
#Hangi işlemi yapacağınıda söyler mesela return x*y print(çarpma(3,5)) çıktısı 3*5=15 oldu 
#return ederken yapacağınıda söyler mesela sen x+y lazımsa onu return x+y fonks da yazarsın ileride işine lazımsa çağırırsın.

#Örnek_1:
def topla2(x,y):
    print(x+ y)
toplam=topla2(4,5)  #fonks çağırma.

print(toplam)  #none olur dışarda çalışmaz. onun için return gerekli.

#Örnek_1.1:
def topla3(x,y):
    print(x+ y)
    return x+y  #fonksiyonun sonucunu geri döndürür.
total=topla3(4,5)
print(total)

#Örnek_1.2:
def topla3(x,y):
    print(x+ y)
    return x+y  #fonksiyonu çağırdığında bu işlemi yapacak
print(topla3(4,5)) #return x+y parametresi olduğu için 4,5 yazdık.

#Örnek_2:

def kare_al(x):
    return x*x  #x*x olarak dışarıda işlem yapacak

print(kare_al(5))

#Örnek_3:

def topla_ve_kare_al(x,y):
    return x+y, x*x  #return ettiğimiz değerler bir tuple olarak döndürür.

toplam, kare=topla_ve_kare_al(3,4)
print(f"Toplam: {toplam}, Kare: {kare}")

#Örnek_4:

def kare_al(x):
    if x<0:
        return "Negatif sayı girdiniz."
    else:
        return x*x

print(kare_al(5))

#Örnek_5:(birden fazla parametre ver değişkenlerin sonucunu toplama)
def birden_fazla_ortalama(x,y,z):
    return (x+y+z)/2
a=birden_fazla_ortalama(2,6,2) #parametreleri boş bırakma(2,4) hata alırsın,(2,4,0) yaparsan sorun olmaz.
b=birden_fazla_ortalama(6,14,4)
c=birden_fazla_ortalama(2,5,0)
print(a+b+c)

#Örnek_6:
def buyuk_harf_yap2(metin): #bu kısım neler yapacağımızı yazdığımız kısım.
    return metin.upper() #metini büyük yaz dedik.
k=buyuk_harf_yap2("merhaba") 
l=buyuk_harf_yap2("nasılsın") 
m=buyuk_harf_yap2("ben Ali") 

print(k,l,m)
print(k+l+m)

print(buyuk_harf_yap2("bunu artık dışarıda çağırabiliyoruz(return sayesinde)."))
print(kare_al(3)) #ÜSTLERDEKİ FONKSU BURADA KULLANABİLİRİZ(ÇAĞIRDIK).



