sozluk = {"home":"ev", "book" : "kitap" , "pen" : "kalem"}

print(sozluk)
print(sozluk["book"])

karakter = {"ad" : "ozan" , "güç" : 100 , "silah" : "kılıç", "can" : 100}

print("Karakterin adı    : {}".format(karakter["ad"]))
print("Karakterin gücü   : {}".format(karakter["güç"]))
print("Karakterin silahı : {}".format(karakter["silah"]))

karakter2 = {"ad" : "halfcress" , "güç" : 70 , "silah" : "ok", "can" : 100}

def vur(vuran:dict,vurulan:dict):
    eksilen = vuran["güç"]
    vurulan["can"] = vurulan["can"] - eksilen

vur(karakter,karakter2)
vur(karakter2,karakter)

print("Karakter 1 can : ",karakter["can"])
print("Karakter 2 can : ",karakter2["can"])