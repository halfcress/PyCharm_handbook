#fonksiyonlar bir problemi çözer, yani çözümden sonra başka bir işlem yapmaz ve bu çözümü direkt olarak geri gönderir.

"""def topla(birinci,ikinci):
    sonuc = birinci + ikinci
    print(sonuc)""" #iki tane sonuc alıyoruz bunlardan biri topla fonksiyonundan gelen sonucumuz. Diğeri ise zaten print fonksiyonu az önce
    #çözüm yapıp(topla fonksiyonunun içinde) bastığı için basacak bir şey kalmadı. Bir nevi içi boş bir fonksiyon yazdırmış olduk. Bu yüzden NONE basıldı.


#Ancak şu şekilde yapsakdık:

def topla(birinci,ikinci):
    sonuc = birinci + ikinci
    return sonuc  # return demek fonksiyon bittiğinde bu fonksiyon artık returnden sonraki değişkeni alsın demektir. Yani örnekte yapıldığında artık bu fonksiyon
    # sonuc isimli değişkendir.