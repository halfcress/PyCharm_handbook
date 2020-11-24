#set küme demektir. -> int,float gibi belirteçtir ancak köşeli süslü parantez gibi bir tanımlayıcı imleci yoktur. O yüzden
# set() şeklinde tanımlanır.
# set içerisinde demet, liste, sözlükler kullanılabilir. Ancak sayılar kullanılamaz (çakışma olmasın diye).
# bir öğe yalnızca bir kez eklenebilir. Fazla eklesek bile çıktı olarak yalnızca bir tanesini gösterir.

#küme metodları:
"""
Öğe ekleme: add -
fark : difference -
öğe silme : discard -
öğe silme : remove -
kesişim : intersection
"""
# discard ' ın remove'dan farkı : discard o eleman varsa çıkartır, yoksa ses veya hata vermez. Ancak remove ile bir şey kaldırmaya
#çalıştığımızda eğer o eleman kümenin içerisinde yoksa hata verir (bu zaten yok der).

a = set([1,2,3,4,5,6,7,8,9])
b = set([4,5,6,7,8,9,10,11])

print("a kümesi = {}".format(a))
print("b kümesi = {}".format(b))

print(45*"=")

print("a kümesinin b den farkı: {} ".format(a.difference(b)))
print("b kümesinin a den farkı: {} ".format(b.difference(a)))

print("a kümesi ile b kümesinin kesişimi : {} ".format(a.intersection(b)))