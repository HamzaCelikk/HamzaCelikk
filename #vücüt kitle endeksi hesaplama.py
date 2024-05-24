#vücüt kitle endeksi hesaplama

boy=float(input("boyunuzu giriniz(m): "))
kilo=float(input("kilonuzu giriniz(kg): "))
vki=kilo / (boy*boy)  #Vücut kitle endeksi.

if vki <18.5 :
        print("zayıfsınız.")
elif vki <= 24.9 :
        print("sağlıklısınız.")
elif vki <= 29.99 :
        print("fazla kilolusunuz.")
elif vki <= 34.9 :
        print("1.dereceden obez.")
elif vki <= 39.9 :
        print("2.dereceden obez.")
elif vki <= 40 :
        print("3.dereceden obez.")
else :
        print("lütfen pozitif değer giriniz.")
    
 
