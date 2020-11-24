#köşeli parantez demek illa liste demek değildir. Verilere erişirken kullanırız.

liste = ["ozan","halfcress","12312312",13224323,65.4,["asdasd",12,34.6,"1996"]]

print(liste[1]) #bu liste değişkenindeki 1. indexi bastır demektir. 0.index ozan, 1. index halfcress dir. halfcress bastırılacaktır.

print(liste[-1]) #son elemanı bastır demektir. ancak örnektede görüldüğü gibi son eleman bir liste elemandır ve liste içerisindeki listeyi bastıracaktır.
#bütün olarak o bir elemandır.

print(liste[-1][3])  #liste değişkenindeki son elemanın İÇİNDEKİ 3. indexi aldırmaya yarar. bunu şu şekilde de kullanabiliriz;

print(liste[0][1]) #liste değişkenindeki 0. indexte olan ozanın, 1. indexi olan z harfini yazdırmaya yarar.

#özetle illa liste olmasına gerek yok köşeli parantez için.

print(liste[-1][0][1]) #bu şekilde de derinleşebiliyoruz.

kelime = "ozan"

print(kelime[1]) #yine z harfini alırız, dediğimiz gibi listeyle alakalı bir durum değil.