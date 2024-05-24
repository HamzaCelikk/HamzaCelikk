#fonks ve listeleme

import random
import string

def rastgele_sifre_olustur():
    uzunluk =10
    karakterler = string.ascii_letters + string.digits + string.punctuation
    sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    
  
    print(f"{sifre}: şifreniz:{sifre}.")
    return sifre

print(rastgele_sifre_olustur())
        
