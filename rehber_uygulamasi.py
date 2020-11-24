rehber = {"ozan": {"cep numarası":"05353333333", "ev numası":"1111111", "adres":"asdasdasd"



},
          "halfcress": {"cep numarası":"05344444444", "ev numarası":"2222222", "adres": "qweqweqwe"




          }


          }

kisi = input("Lütfen rehberde aranın kisinin adını veriniz: ")
if kisi in rehber:
    flag = True

else:
    flag = False

veri = input("Lütfen istenen kisinin hangi bilgisini istediğinizi giriniz: ")

if flag:
    print(rehber.get(kisi).get(veri,"böyle bir veri bulunamdı"))
else:
    print("böyle bir kisi bulunamadı.")