import os
kitap1 = ("Yalnızlık","Peyami safa")
kitap2 = ("headbang","dergi")

kitaplistesi = [kitap1,kitap2]

def kontrolmekanizm(kitap:tuple,liste:list):
    if kitap in liste:
        return True
    else:
        return False

def kitapekle(kitap:tuple,liste:list):
    liste.append(kitap)
    print("Kitap ekleme başarılı. ")
    print("Ana menüye dönmek için lütfen bir tuşa basınız.")
    input()

def kitapcikar(kitap:tuple,liste:list):

    if kontrolmekanizm(kitap,liste) == 1:
        liste.remove(kitap)

        print("Kitap alma işlemi başarılı. ")
        print("Ana menüye dönmek için lütfen bir tuşa basınız.")
        input()
    else:
        print("Bu kitap çoktan alınmış.")
        print("Ana menüye dönmek için herhangi bir tuşa basın.")
        input()

def kitaplistele(liste:list):
    print(liste)
    print("Ana menüye dönmek için herhangi bir tuşa basınız.")
    input()

menu = """

[1] Kitap ekleme
[2] Kitap alma
[3] Kitap listeleme
[Q] Uygulamadan Çıkış

"""

while True:
    os.system("cls")
    print(menu)

    secim = input("Lütfen Seçiminizi Giriniz: ")

    if secim == "1":
        kitapadi = input("Lütfen kitabın adını giriniz: ")
        kitapyazari = input("Lütfen kitabın yazarını giriniz: ")
        kitap = (kitapadi,kitapyazari)

        kitapekle(kitap,kitaplistesi)

    elif secim == "2":
        kitapadi = input("Lütfen kitabın adını giriniz: ")
        kitapyazari = input("Lütfen kitabın yazarını giriniz: ")
        kitap = (kitapadi, kitapyazari)
        kitapcikar(kitap, kitaplistesi)


    elif secim == "3":
        kitaplistele(kitaplistesi)


    elif secim == "q" or secim == "Q":
        quit()
        print("Programdan Çıkış yapılıyor.")
        input()
    else:
        print("Hatalı giriş yaptınız.")
        input()

