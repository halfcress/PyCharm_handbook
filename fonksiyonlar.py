#bir çok kodu bir başlık altında toplamaktır. Örneğin print() bir fonksiyondur ve bu fonksiyon çağrıldığında aslında arkada bizim görmediğimiz bir çok komut
#çalışmaktadır.

#Fonksiyon tanımlama:

"""def (topla):
    sonuc = 3+5
    print(sonuc)"""         #şuan topla() adında bir fonksiyon yarattık ve artık bu programda her topla() görüldüğünde ekrana 8 yazdırılacak. Çünkü 3+5 :D



#Parametrize Edilebilme özelliği

#yukarıdaki örnekte her topla fonksiyonunu çağırdığımızda bize 8 değerini veriyordu. Fakat biz her çağırdığımızda toplanacak iki sayı cinsinden farklı sonuçlar
#istiyoruz. Bunu yapabiliriz şu şekilde;

birinci_sayi = float(input("birinci sayiyi giriniz:"))
ikinci_sayi = float(input("ikinci sayiyi giriniz:"))

def topla(birinci_sayi,ikinici_sayi):
    sonuc = birinci_sayi + ikinici_sayi
    print(sonuc)

print(topla(birinci_sayi,ikinci_sayi)) #görüldüğü gibi çıktıda none diye bir değer daha alıyoruz. bu return dersinin konusu.
