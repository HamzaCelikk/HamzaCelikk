#ehliyet alma için yaş sınırı
#KOŞULLU_İFADELER=Belli bir şart doğrultusunda programın akışını değiştiren koşullu ifadeler.

yaş=int(input("Yaşınızı giriniz: "))
if yaş >= 18:
    print("Ehliyet almaya uygunsunuz.")
else:
    print("Ehliyet almak için 18 yaşına girmeniz gerekiyor.")