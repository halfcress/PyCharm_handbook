"""
format() Metodunun Kullanım Biçimleri

Herhangi bir yöne veya merkeze konumlandırmak ve alan ayırmak:

string = "|{:<15}|".format("Volkan")
print(string)
|Volkan         |
Yukarıda görüldüğü gibi string sola yaslanmış biçimde fakat string için ayrılan bölme 15 birim.

string = "|{:>15}|".format("Öğrenciler")
print(string)
|     Öğrenciler|
Yine yukarıda görüldüğü gibi string sağa yaslanmış biçimde fakat string için ayrılan bölme 15 birim.

Sıra belirleme:

string = "{} {}".format("isim","soyisim")
print(string)
isim soyisim
string = "{1} {0}".format("isim","soyisim")
print(string)
soyisim isim
Görüldüğü gibi değişkenlerin geleceği sıraları ayarlayabiliyoruz.

İsim Verme:

string = "{ad} {soyad}".format(soyad = "ATATÜRK",ad = "Mustafa Kemal")
print(string)
Mustafa Kemal ATATÜRK
Sıra ile yazmak mecburiyetinde değiliz, istersek değişken gibi isim verebiliyoruz.

String Zorunluluğu:

string = "bu bir string {:s}".format(str(12))
Bunda hata almazken şunda alırız:

string = "bu bir string {:s}".format(12)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-11-c24a602ab5d9> in <module>()
----> 1 string = "bu bir string {:s}".format(12)

ValueError: Unknown format code 's' for object of type 'int'
Sayı Zorunluluğu:
string = "burada sayı var {:d}".format(25)
Tabi eğer şöyle yazarsak hata alırız:

string = "burada sayı var {:d}".format(str(25))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-13-fb6a66e6a1fa> in <module>()
----> 1 string = "burada sayı var {:d}".format(str(25))

ValueError: Unknown format code 'd' for object of type 'str'

ASCII tablosundaki karşılıklar:

string = "--->>  {:c}".format(65)
print(string)
--->>  A
0 ile 256 arası sayıların ASCII tablosundaki karşılıklarını temsil eder.

Sekizlik sistemdeki karşılıklar:

string = "{:o}".format(16)
print(string)
20
Onaltılık sistemdeki karşılıklar:

string = "{:x}".format(42)
print(string)
2a
Eğer büyük 'X' harfi kullanırsak harfler büyük gösterilir:

string = "{:X}".format(42)
print(string)
2A

İkilik sistemdeki karşılıklar:

string = "26 sayısının ikilik karşılığı -->> {:b}".format(26)
print(string)
26 sayısının ikilik karşılığı -->> 11010
Sayıları basamaklarına ayırma:
string = "{:,}".format(2136238213621)
print(string)
2,136,238,213,621
"""