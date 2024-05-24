#vize final notu  geçti/kladı.

vize=float(input("vize notunuzu giriniz: "))
final=float(input("final notunuzu giriniz: "))
ortalama=vize*40/100 + final*60/100

if ortalama>50:         #iki ifadeyi koşulu bir arada kullandık.
    if final >= 50:
        print(f"sınavı geçtiniz. ortalamanız:{ortalama}")
else:
     print(f"sınavı geçemediniz. ortalamanız:{ortalama}")
