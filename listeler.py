kitapliste = ["abc",12,10.5] #listeler string,int,float gibi her türden tipi tutabilir. Başka bir liste de tutabilir.

for i in kitapliste:
    print(type(i))

kitapliste2= ["Şeker portakalı","Nutuk","Witcher serisi","Küçük şeyler","Das Kapital"]

for i in kitapliste2:
    print("Kitap adı: {}".format(i))

eklenecek = input("Eklenecek kitabın adını yazınız: ")

kitapliste2 += eklenecek #eğer bu şekilde yaparsak ve ozan diye bir kitap girersek;
#['Şeker portakalı', 'Nutuk', 'Witcher serisi', 'Küçük şeyler', 'Das Kapital', 'o', 'z', 'a', 'n'] böyle bir çıktı ile karşılaşacağız.
#bunun önüne geçmek için eklenecek değişkeninin bir liste elemanı olduğunu [eklenecek] şeklinde belirtmemiz gerekiyor ki, tek bir eleman olarak eklesin.

kitapliste3= ["Şeker portakalı","Nutuk","Witcher serisi","Küçük şeyler","Das Kapital"]

for i in kitapliste3:
    print("Kitap adı: {}".format(i))

eklenecek = input("Eklenecek kitabın adını yazınız: ")

kitapliste3 += [eklenecek] #aynen bu şekilde.

print(kitapliste3)

#ancak bu düz mantıkla += operatörünü kullandığımız gibi -= operatörü ile listeden çıkartma yapamıyoruz. Bunun sebebi;

"""
string = "abc"

string -= "b" diye bir şey yapamayacak olmamız. Stringlerde çıkartma işlemi yapılamaz, ancak toplama ve çarpma yapılabilir.

"""