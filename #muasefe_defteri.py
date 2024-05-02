#muasefe_defteri

#fonksiyon ile tanımlayalım.
def muhasebe_hesap():
    
    #Boş listleri oluşturalım.
    giderList=[]  
    kalanList=[]

    #gerekli bilgileri kullanıcıdan isteyelim.
    toplam_Paranız=int(input("Toplam paranızı giriniz(TL): "))
    finans=int(input("Toplam borsa,hisseye giden paranızı giriniz(TL): "))
    okul=int(input("Toplam okul harçlığına giden paranızı giriniz(TL): "))
    eğitim=int(input("Toplam eğitime giden paranızı giriniz(TL): "))
    borç=int(input("Toplam ödenecek borç (TL): "))


    #bakiye ve giderler üzerinde işlem yapalım.
    toplam_Gider=(finans + okul + eğitim + borç)
    toplam_Kalan=toplam_Paranız-toplam_Gider
    
    #listeye ekleyelim.
    kalanList.append(toplam_Kalan)
    giderList.append(toplam_Gider)
    
     #ekrana yazdıralım.
    print(f"Giden Tutarlar:(finans:{finans} + okul:{okul} + eğitim:{eğitim} + borç:{borç}):toplamgider={giderList}, Kalan Bakiyeler={kalanList}")
    
    #borcumuz varmı? var ise ne kadar?
    if toplam_Gider < toplam_Kalan:
        print("Borcunuz bulunmamaktadır.")
    else:
        print(f"kalan borcunuz={toplam_Kalan}")

muhasebe_hesap()





 


