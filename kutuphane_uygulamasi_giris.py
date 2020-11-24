kitaplistesi = list()

menu = """
===============================
[1] - Kitap ekle
[2] - Kitap çıkar
[3] - Kitapları listele
[Q] - Programdan çık
===============================
"""

def kitapekle(kitap,liste):
    liste += [kitap]
    print("Kitap eklendi !")
    input("Ana menüye dönmek için ENTER a basın!")

def kitapcikar(): #çıkarma fonksiyonu sonradan eklenecek.


def listele(liste):
    for i in liste:
        print("{}".format(i))
        input("Ana menüye dönmek için ENTER a basın!")

def cik()
    quit()


while True:
    print(menu)
    secim = input("Seçiminiz: ")

    if secim == "1":
        kitapadi = input("Kitap adi:")
        kitapekle(kitapadi,kitaplistesi)

    elif secim == "2":  #bu fonksiyon sonradan eklenecek.
        kitapcikar()

    elif secim == "3":
        listele(kitaplistesi)

    elif secim == "q" or secim == "Q":
        cik()

    else:
        print("Hatalı Giriş Yaptınız!")
        input("Ana menüye dönmek için ENTER a basın!")



