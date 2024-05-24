#Telefon_rehberi

#sözlük için {} kullanalım

rehber={}

def ekleme ():
    ad=(input("Kişinin ismini giriniz: "))
    soyad=(input("Kişinin soyadı giriniz: "))
    telefon=(input("Kişinin telefonu giriniz: "))
    email=(input("Kişinin e-posta adresini giriniz: "))
    sehir=(input("Kişinin şehir  giriniz: "))
    rehber[ad] = {"Soyadı": soyad, "Telefon": telefon, "E-posta": email, "Şehir": sehir}
    print(ad, "rehbere eklendi.")


def silme ():
    ad = input("Silinecek kişinin adını girin: ")
    if ad in rehber:
        del rehber[ad]
        print(ad, "rehberden silindi.")
    else:
        print(ad, "adlı kişi rehberde bulunamadı.")


def arama():
    ad = input("Aranacak kişinin adını girin: ")
    if ad in rehber:
        print(ad, "adlı kişinin bilgileri:")
        print("Soyadı:", rehber[ad]["Soyadı"])
        print("Telefon:", rehber[ad]["Telefon"])
        print("E-posta:", rehber[ad]["E-posta"])
        print("Şehir:", rehber[ad]["Şehir"])  # Şehir olarak kaydettiğimiz için Şehir,sehir,Sehir ayrı anlamlara gelir ve hata alırsın
                                              # yani listeleme ve eklemede de Şehir olarak kullandık yoksa hata alırdık.
    else:
        print(ad, "adlı kişi rehberde bulunamadı.")


def listele():
    print("Telefon Rehberi:")
    for ad in rehber:
        print("Adı:", ad)
        print("Soyadı:", rehber[ad]["Soyadı"])
        print("Telefon:", rehber[ad]["Telefon"])
        print("E-posta:", rehber[ad]["E-posta"])
        print("Şehir:", rehber[ad]["Şehir"])
        print("***********************")

while True:
    print("\nTelefon Rehberi Uygulaması")
    print("1. Kişi Ekle")
    print("2. Kişi Sil")
    print("3. Kişi Ara")
    print("4. kişi Listele")
    print("5. Çıkış")
    
    secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4/5): ")
    if secim == "1":
        ekleme()
    elif secim == "2":
        silme()
    elif secim == "3":
        arama()
    elif secim == "4":
        listele()
    elif secim == "5":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")




