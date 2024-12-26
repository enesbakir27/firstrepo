import random
karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("kaç karakterlik bir bilgi olsun?"))

sifre = ""

for i in range(uzunluk):
    sifre += random.choice(karakter)
print(sifre)    




