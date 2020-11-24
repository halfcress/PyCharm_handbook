a = int(input("Bir kenarı giriniz: "))
b = int(input("Diğer kenarı giriniz"))
hipotenüs = int(input("hipotenüsü giriniz"))

def ucgenmi(a,b,hipotenüs):
    if a**2 + b**2 == hipotenüs**2:
        return "bu bir üçgendir"
    else:
        return "bu bir üçgen değildir"


print(ucgenmi(a,b,hipotenüs))

