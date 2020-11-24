sozluk = {"princess":"prenses", "poet":"ozan", "marry":"meryem"}

def kontrol(x,sozluk):
    if x in sozluk:
        return True
    else:
        return False


x = input("Lütfen ingilizce kelimeyi giriniz: ")

kontrol(x,sozluk)

if kontrol(x,sozluk) == 1:


    print("yazdığınız kelimenin sözlükteki karşılığı: {}" .format(sozluk[x]))

else:
    print("aradığınız sözcük sözlükte bulunamadı.")

#BURADA kontrol fonksiyonu kullanmamızın sebebi programın çökmemesi idi. ancak bu klasik yöntemdir bunu
#bu kadar uzatmak yerine get metodunu kullanarak kontrol fonksiyonunu tek satıra indirgeyebiliriz.

#örneğin: fonksiyon tanımlamak yerine print(sozluk.get(x,"Aratılan sözcük bulunamadı")) şeklinde kullansaydık
#get metodu öncelikle while true/false döngüsüne göre işlem yapacak, true olduğu zamanlar için x'i
#olmadığı zamanlar için 2. parametre olan "Aratılan sözcük bulunamadı" bastıracaktı. Bir nevi kontrol
#fonksiyonunun kolay kullanımı.

#items : items metodunun kullanım şeması ; for i in sozluk.items():
                                                #print(i)  şeklindedir. bu bize listeleme yapmayı sağlar.

#keys metodu sadece key'leri bastırmaya yarar. Örneğin bu örnekte sadece ingilizce keyleri bi yere
#toplamak isteseydik bu metodu kullanabilirdik bastırmak için.
#values metodu keys metodunun tam tersidir. (türkçe kelimeler)
