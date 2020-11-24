#copy kullanımı:

"""

öncelikle oluşturacağımız listenin adı, sonrasında kopyalayacağımız listenin .copy metodu ile yazılımı;

liste1 = ["adkfalsdfklasdfk"]

liste2 = liste1.copy()

artık bu noktadan sonra liste2 diye, liste1 in birebir kopyasını oluşturduk ve liste2 üzerinde yapacağım
değişiklikler liste1 i etkilemiyor, apayrı bir küme.

"""

# extend genişletme demektir. örneğin birbirinden farklı iki listemiz var ve liste1 i liste2 ile geniş
# letmek istiyorsam

liste1 = ["ozan"]
liste2 = ["halfcress"]

liste1.extend(liste2)

print(liste1) # şeklide liste1 ile liste2 yi genişletmiş olduk. bir nevi toplama işlemi yaptık.

print(40*"=")
liste3 = ["Ozan", "halfcress", "1996", "2020"]
print(liste3.index("halfcress"))
print(liste3[1])
#sort harf sırasına göre listenin içeriğini sıralamaya yarar.

print(59*"=")

liste3.sort() #önce sort işlemini yaptırdık, daha sonra bastıracağız.

print("listenin harf sırasına göre dizilimi şu şekilde:\n{}".format(liste3))

#eğer liste içerisinde sayılar varsa, sayıları da küçükten büyüğe sıralar.
