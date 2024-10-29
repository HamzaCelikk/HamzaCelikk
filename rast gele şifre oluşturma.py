import random
import string

def rastgele_sifre_olustur():
    uzunluk =10  #şifre uzunluğu
    karakterler = string.ascii_letters + string.digits + string.punctuation
    sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    
    return sifre

print(rastgele_sifre_olustur())
        
