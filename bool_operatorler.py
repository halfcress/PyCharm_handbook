"""
and
or
not

"""

sayi = int(input("5 ten büyük ve çift bir sayi gir: "))

"""if sayi > 5:
    if sayi % 2 == 0:
        print("DOĞRU")
"""       #Bunu tek satırda yazdırmak için, yani 5 ten büyük ve çift bir sayı olması  koşulunu;

if sayi > 5 and sayi % 2 == 0:
    #şeklinde tek satıra indirmiş olduk
    print("Doğru")

else:
    print("Yanlış")

#or da aynı şekilde kullanılır. Bildiğimiz mantık operatörü. Ve veya daki veya  kısmıdır.
#or ile bağlanmış herhangi bir şey true ise, sonuç true olacaktır.

#not true ise false yapar, false ise true yapar.

#not_ornek te örnek yaptım.