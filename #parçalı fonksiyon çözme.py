#parçalı fonksiyon çözme
y=int
x=float(input("x değerini giriniz: "))
if x<1:
    y=3*x-4
elif 1 <= x <= 10:
    y=x+2
else:
    y=2*x+4

print(y)
