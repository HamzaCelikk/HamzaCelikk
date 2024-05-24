#2.derece denklem
import math
print("ax2+bx+c değeri gibi 2. dereceden bir denklemi çözelim")

a=int(input("a değerini giriniz : "))
b=int(input("b değerini giriniz : "))
c=int(input("c değerini giriniz : "))

delta=b**2 - 4 * a * c

x1= ((-1 * b + delta **(1/2)) /(2 * a)) # hatam ** (1/2) üssü almamakmış.
x2= ((-1* b - delta ** (1/2)) /(2 * a)) # hatam ** (1/2) üssü almamakmış.

print(f"denklem={a}x2+{b}x1+{c} ")
print(f"x1={x1} , x2={x2}, delta={delta}")
