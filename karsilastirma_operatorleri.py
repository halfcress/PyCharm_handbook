"""
== Eşitse
!= Eşit değilse
> Büyükse
< Küçükse
>= Büyük eşitse
<= Küçük eşitse
"""

giris = input("10 ile 100 arasında bir sayı girin")

giris = int(giris)

if giris > 100:
    print("bu 100 den büyük bir sayı programdan çıkış yapılıyor")
    quit()

elif giris == 50:
    print("50 ye eşit")

elif giris > 50:

    print("50 den büyük")

else:

    print("50 den küçük")
    quit()