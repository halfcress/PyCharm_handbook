alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
for x in alfabe:  #2 kısım olarak incelersek for döngüsü şu şekilde çalışır. 2. kısımdaki yani şuanki örneğimizde alfabe içerisindeki her bir öğeyi
    #teker teker 1. kısımdaki değişkene yani x değişkenine ata ve her atama için 1 kez çalış.
    print(x)

    #saydırma işlemini de şu şekilde yapabiliriz:

alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
sayi = 0
for x in alfabe:
    sayi += 1
    print("Öğe sayısı: ",sayi)  #bu sayede for her döngüye girdiğinde sayı değişkenimiz 1 artacak ve en nihayetinde bize 29 çıktısını verecek.
