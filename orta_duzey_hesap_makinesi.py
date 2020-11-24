print("""
[1] Toplama İşlemi
[2] Çıkarma İşlemi
[3] Çarpma İşlemi
[4] Bölme İşlemi
[5] Üs alma İşlemi
[Q] Çıkış
""")

giris = input("Seçiminiz :")

if giris == "1":    #if true döndürdüğünde yani gerçekleştiğinde eğer elif yerine if ler ile devam etseydik program onları da tek tek okuyacaktı
    #ancak elif koyduğumuzda 1 tanesi döndüğü anda diğer elif leri görmezden geliyor.


    x = input("İlk Sayı: ")
    x = float(x)
    y = input("İkinci Sayı: ")
    y = float(y)
    print("=================================")
    print("İşlem Sonucu : ", x+y)
    print("=================================")


elif giris == "2":

    x = input("İlk Sayı: ")
    x = float(x)
    y = input("İkinci Sayı: ")
    y = float(y)
    print("=================================")
    print("İşlem Sonucu : ", x-y)
    print("=================================")
elif giris == "3":

    x = input("İlk Sayı: ")
    x = float(x)
    y = input("İkinci Sayı: ")
    y = float(y)
    print("=================================")
    print("İşlem Sonucu : ", x*y)
    print("=================================")
elif giris == "4":

    x = input("İlk Sayı: ")
    x = float(x)
    y = input("İkinci Sayı: ")
    y = float(y)
    print("=================================")
    print("İşlem Sonucu : ", x/y)
    print("=================================")
elif giris == "5":

    x = input("Taban: ")
    x = float(x)
    y = input("Kuvvet: ")
    y = float(y)
    print("=================================")
    print("İşlem Sonucu : ", x**y)
    print("=================================")
elif giris == "q" or giris == "Q":

    print("=================================")
    print("ÇIKILIYOR")
    print("=================================")
    quit()

else:
    print("=================================")
    print("HATALI GİRİŞ PROGRAMDAN ÇIKILIYOR")
    print("=================================")
    quit()






