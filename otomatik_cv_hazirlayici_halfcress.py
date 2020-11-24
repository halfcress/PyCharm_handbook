"""
isim
soyisim
mezun olunan yıl
hangi bölümden mezun olduğu
doğum yılı
eğitim aldığı üniversite
diploma notu
yabancı diller
staj yaptığı yerler/iş tecrübeleri
medeni hali
telefon numarası
yetenekler
"""

isim = str(input("Lütfen isminizi giriniz: "))
soyisim = str(input("Lütfen soyisminizi giriniz: "))
universite_isim = str(input("Lütfen mezun olduğunuz üniversitenin adını giriniz: "))
mezun_yil = str(input("Lütfen mezun olduğunuzu yılı giriniz: "))
mezun_bolum = str(input("Lütfen mezun olduğunuz bölümü giriniz: "))
universite_ortalama = str(input("Lütfen 4 üzerinden kaç ile mezun olduğunuzu giriniz: "))
dogum_yil = int(input("Lütfen yalnızca doğduğunuz seneyi giriniz: "))
yas_hesap = str(2020-dogum_yil)
yabanci_dil = str(input("Lütfen bildiğiniz yabancı dili/dilleri giriniz: "))
tecrubeler1 = str(input("Lütfen iş tecrübelerinizi giriniz: "))
tecrubeler2 = str(input("Lütfen staj tecrübelerinizi giriniz: "))
medeni_hal = str(input("Lütfen medeni halinizi giriniz: "))
tel_no = str(input("Lütfen telefon numaranızı giriniz: "))
yetenekler = str(input("Lütfen sertifika aldığınız veya kendinizi geliştirdiğiniz yeteneklerinizi giriniz: "))


cikti = ("""
======================================================================
Ad-soyad = {} {}
Okuduğu Üniversite = {}
Mezun olduğu yıl = {}
Mezun olduğu bölüm = {}
Üniversite ortalaması = {}
======================================================================
Yaşı = {}
Yabancı dil = {}
İş tecrübesi = {}
Staj tecrübesi = {}
Medeni hali = {}
======================================================================
Telefon = {}
Yetenekler = {}


""").format(isim,soyisim,universite_isim,mezun_yil,mezun_bolum,universite_ortalama,yas_hesap,yabanci_dil,tecrubeler1,tecrubeler2,medeni_hal,tel_no,yetenekler)

print(cikti)