liste = ["deneme","deneme2"]

print(liste)

liste += ["deneme3"]

print(liste)  #bu metodsuz yöntem.

liste2 = ["deneme","deneme2"]
for i in dir(liste): #alt alta yazsın diye for döngüsü kullandık.
    print(i)

#daha önce += ile listeye item ekleme işini artık append metodu ile kullanabiliriz.
#pycharm da dir komutu ile hangi metodları kullanacağımızı görebildiğimiz gibi, nokta tuşu ile de
#metodları görebiliriz. bu bir kolaylıktır. append ekleme, remove çıkarma işlemi yapmaya yarar.




liste3 = ["deneme100","deneme200","deneme300"]
print(liste3)
liste3.append("deneme400")
print(liste3)
liste3.remove("deneme100")
print(liste3)