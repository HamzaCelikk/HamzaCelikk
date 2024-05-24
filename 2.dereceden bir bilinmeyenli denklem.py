#2.ddereceden bir bilinmeyenkli denklem çözme

a=float(input("a değerini gir: "))
b=a=float(input("b değerini gir: "))
c=a=float(input("c değerini gir: "))
diskriminant=b*b-4*a*c
if diskriminant<0:
    print("gerçel kökü yoktur.")

elif diskriminant>0:
    x1=(-b+(diskriminant**(1/2)))/2*a
    x2=(-b-(diskriminant**(1/2)))/2*a
    print(f"x1={x1},x2={x2}")

elif diskriminant==0:
    x1=-b/(2*a)
    print(f"x1={x1}")
else:
    print("geçersiz işlem.")

