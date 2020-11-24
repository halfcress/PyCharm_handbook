#is işleci
#id fonksiyonu

a = 5
b = 5

if a == b:
    print("Aynı")

if a is b:
    print("kimlikleri aynı")

    print(id(a))
    print(id(b))
    print(id(5))

    #bir program çalıştırılırken bilgisayar örneğin 5 için bir kimlik tanımlar ve onu kullanır.
    #programı her seferinde yeniden başlattığımızda farklı kimlikler olsada o an hepsi için aynı kimlik
    #atanmış durumda oluyor. Bu sebeple is işleci kimlik için kullanılırken eşitlik operatörü eşitlik için kullanılır.
    #aynı gibi gözükseler de aynı şey değillerdir.
