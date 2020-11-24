"""isim
soyisim
doğum tarihi ay,yıl,gün
meslek
doğum yeri """

isim = str(input("İsminizi giriniz: "))
soyisim = str(input("Soyadınızı giriniz: "))
dogum_yil = int(input("Hangi senede doğdunuzu giriniz: "))
dogum_yer = str(input("Doğduğunuz yeri giriniz: "))
meslek = str(input("Mesleğinizi giriniz: "))

yas_hesap = str(2020 - dogum_yil)
cikti= """
==================
Ad-Soyad = {} {}
Doğum tarihi = {} / {} yaşında
Doğduğu yer = {}
Mesleği = {}
==================
""".format(isim,soyisim,dogum_yil,yas_hesap,dogum_yer,meslek)

print(cikti)

