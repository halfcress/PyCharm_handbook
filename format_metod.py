"""
konumları belirleme
sözcük atama
:> sağa yaslama ve alan ayırma
:< sola yaslama ve alan ayırma
:^ merkezde alan ayırma
:s yalnızca string ifade
:d yalnızca sayısal ifade (decimal karşılık)
:b ikili sistemdeki karşılık

"""

degisken1 = "ozan"
degisken2 = "halfcress"

ifade1 = "{} {}".format(degisken1,degisken2)
ifade2 = "{} {}".format(degisken2,degisken1)  #normal çıktımız şu şekilde  #ozan halfcress
                                                                           #halfcress ozan
print(ifade1)
print(ifade2)

#fakat şöyle yaparsak

degisken1 = "ozan"
degisken2 = "halfcress"

ifade1 = "{1} {0}".format(degisken1,degisken2) #şimdiki çıktımız #halfcress ozan
ifade2 = "{1} {0}".format(degisken2,degisken1)                   #ozan halfcress oldu. Normalde python her zaman önce 0 sonra 1 atayarak işlem yapar. Biz sırayı değiştirebiliriz.
#buna konumları belirleme denir. ilk süslü parantezin içine yazdığımız 1, parantez içindeki degisken2 indexini alır. (index0,index1 olarak gidiyor çünkü)

print(ifade1)
print(ifade2)

#sözcük atama ise şu şekilde yapılır:

ifade3 = "{ad} {soyad}".format(ad = degisken1, soyad = degisken2)


print(ifade3)

#sağa yaslama ve alan ayırma özelliği;

ifade4 = "==={:>15}===".format(degisken1) #süslü parantezlerin dışındaki eşittir sadece güzel görünsün diye konuldu. #içerideki operatör olan :> sağa yaslama ve alan
#ayırma özelliğinden geliyor, 15 ise kaç birimlik alan ayırmak istediğimiz ile alakalı. yani formatta belirteceğimiz ne ise 15 birimlik alana SIĞMIŞ oluyor.

print(ifade4)

ifade5 = "==={:<15}===".format(degisken1)

print(ifade5)

ifade6 = "==={:^15}===".format(degisken1)

print(ifade6) #genel çalışma prensibi bu şekilde.

#string ifade ve sayısal ifade operatörlerinin de çalışma prensibi şu şekilde. Eğer :s operatörü koyulduysa ve formattan sonraki değişkende bir sayı değeri varsa
#program otomatik olarak hata verecektir. Aynı mantık sayısal ifade operatörü için de geçerli.

#binary kullanımı ise şu şekilde:

ifade7 = "==={:b}===".format(99) #eşittirlerin yine hiç bir anlamı yok, format içerisine yazdığımız sayının binary karşılığını bize verecek bu operatör.4

print(ifade7)