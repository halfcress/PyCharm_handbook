x = input("x gir:")
y = input("y gir:")

if not bool(x):
    print("Doğru!")

    #Bu örnekte y etkisiz elemandır ancak x değeri sorulduğunda hiç bir şey yazmaz isek
    #normalde bool(x) false olacakken başında not operatörü yüzünden true olacaktır.
    #bu sayede if bloğu true kabul edilecek ve print fonksiyonu bastırılacaktır.

