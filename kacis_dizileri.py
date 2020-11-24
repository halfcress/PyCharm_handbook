#ters slash ile başlayan her şey bir kaçış dizisi olarak görülür program tarafından bu yüzden print fonksiyonu içerisinde ters slash kullanmak
#istiyorsak iki tane koymamız gerekir. iki tane koymak istiyorsak 4 tane.. bu böyle gidiyor.

print("\\") #örnekte görüldüğü gibi.

#\n alt satıra inme kaçış dizisidir.
#\a bip sesi kaçış dizisi.

print("\a")
print("Bip sesiiiiiii !!") #powershell de çalışıyor.

#\t bir tab boşluğu kadar boşluk bırakma kaçış dizisi.

print("Ozan\thalfcress")

"""
DOKUMANTASYON

Alt satır başı:

print("Hello\nWorld") # \n kaçış dizisi ile alt satıra geçiliyor
Hello
World

Düşey sekme:

print("Hello\vWorld") # \v düşey sekme kaçış dizisi
HelloWorld
Notebook üzerinde görünmesede terminal üzerinde etkisi görünecektir.

İmleci sola kaydırma:

print("www.google.com\bdeneme") # \b kaçış dizi ile imleç bir birim sola kaydırıldı. Bu sayede 'm' harfi yok oldu.
www.google.comdeneme
Unicode
UNICODE, karakterlerin, harflerin, sayıların ve bilgisayar ekranında gördüğümüz öteki bütün işaretlerin her biri için tek ve benzersiz bir numaranın tanımlandığı bir sistemdir. Bu sistemde, ‘kod konumu’ (code point ) adı verilen bu numaralar özel bir şekilde gösterilir. Örneğin ‘ı’ harfi UNICODE sisteminde şu şekilde temsil edilir:

#u+0131
Python programlama dilinde ise, yukarıdaki kod konumu düzeni şöyle gösterilir:

#\u0131
print("\u0131")
ı
Gördüğünüz gibi, Python UNICODE sistemindeki her bir kod konumunu gösterebilmek için, önce \u şeklinde bir kaçış dizisi tanımlıyor, ardından UNICODE sisteminde + işaretinden sonra gelen sayıyı bu kaçış dizisinin hemen sağına ekliyor.

Etkisizleştirme:

print("\u0131")
print(r"\u0131")
ı
\u0131
Görüldüğü gibi string ifadenin soluna 'r' karakteri koyulduğunda kaçış dizileri etkisiz hale geliyor.

"""
