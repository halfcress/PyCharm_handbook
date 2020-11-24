#öncelikle range() fonksiyonunu öğreneceğiz.
for sayi in range (0,100):
    print(sayi) #burada range fonksiyonu 0'ı dahil ederek, 99 a kadar sayı bastırmaya yarar. Şu şekilde daha açık olur.

for sayi in range (0,100):
    print("Bu",str(sayi)+"ıncı döngü")

"""
range(0,100): demek range(100) demek ile aynı şeydir
Çünkü aksi belirtilmediği sürece 0'dan 99'a kadar yazar bu tip bir durumda. İkiside sıfırdan başla belirtilen yere kadar yaz anlamına gelmektedir.

!! 0.index + 99.index = 100 index !!


range(0,100,2): demek ise 2 şer 2 şer yaz demektir, türetilebilir, 100 er 100 er de yazdırabiliriz.
"""


