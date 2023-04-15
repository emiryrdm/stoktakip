import time
from stokList import liste
from stokList import  materialList
import matplotlib.pyplot as plt

class malzeme():

    def __init__(self,name,piece,price):
        self.name = name
        self.piece = piece
        self.price = price

    def addMaterial():
        deterjan = malzeme("Deterjan", "60", "45")
        ekmek = malzeme("Ekmek", "150", "2")
        yogurt = malzeme("Yoğurt", "30", "12")
        bebek_bezi = malzeme("Bebek Bezi", "20", "60")
        seker = malzeme("Şeker", "75", "15")
        sut = malzeme("Süt", "40", "5")
        materialName = str(input("Malzame İsmi: ")).capitalize()
        time.sleep(0.5)
        materialPiece = str(input("Adet: "))
        time.sleep(0.5)
        materialPrice = str(input("Fiyatı: "))
        materialList = [deterjan, ekmek, yogurt, bebek_bezi, seker, sut]
        newMaterial = malzeme(materialName,materialPiece,materialPrice)
        materialList.append(newMaterial)
        for i in materialList:
            x = i.name + " " + i.price + " " + "Adet " + " " + i.piece + " " + "TL"
            liste.append(x)
        print(f"{newMaterial.name} Başarıyla Eklendi")
        time.sleep(1)


    def listMaterial():
        for i in materialList:
            x = i.name + " " + i.price + " " + "Adet " + " " + i.piece + " " + "TL"
            if x not in liste:
                liste.append(x)
        for i in liste:
             print(i)

    def deleteMaterial():
        for i in materialList:
            x = i.name + " " + i.price +" " + "Adet "+ " " + i.piece + " " +"TL"
            if x not in liste:
                while True:
                    liste.append(x)
                    break
        x = 0
        y = 1
        while True:
            print(f"{liste[x]} Ürünü Silmek İçin {y} Tuşlayınız")
            x +=1
            y +=1
            if x == len(liste):
                break
        a = int(input("Seçiminiz: "))
        b = a
        a = liste[a-1]
        liste.remove(a)
        b = materialList[b-1]
        materialList.remove(b)
        print(f"{a} Listeden Başarıyla Kaldırıldı")
        



    def showGraphics():
        lst1 = list()
        lst2 = list()

        for i in materialList:
            x = i.name
            y = i.piece
            y = int(y)
            lst1.append(x)
            lst2.append(y)

        plt.figure(figsize=(8,6))
        plt.title("Ürün Stok Durumu",color = "purple")
        plt.xlabel("Stok Adedi",color = "orange" ,size = 12)
        plt.ylabel("Ürün İsmi", color = "orange" , size =12)
        plt.bar(lst1,lst2,color="red")
        plt.show()


while True:
    try:
        print("""
        
        *** MARKET OTOMASYON UYGULAMAMIZA HOŞ GELDİNİZ ***
        
         [1] STOKLARA YENİ ÜRÜN EKLEMEK İÇİN
         
         [2] STOKLARDAN ÜRÜN SİLMEK İÇİN
         
         [3] STOKLARINIZI LİSTELEMEK İÇİN
         
         [4] STOKLARINIZIN GRAFİKLERİNİ GÖRÜNTÜLEMEK İÇİN
         
         """)

        tercih = int(input("Lütfen Yapmak İstediğiniz İşlemi Tuşlayınız: "))
        if tercih ==1:
                malzeme.addMaterial()
                time.sleep(2)

        if tercih ==2:
            malzeme.deleteMaterial()
            time.sleep(2)

        if tercih == 3:
            malzeme.listMaterial()
            time.sleep(2)

        if tercih==4:
            malzeme.showGraphics()
    except ValueError or TypeError:
        print("Lütfen 1 ile 4 Arasında Bir Seçim Yapınız!!")
        print("\a")
        time.sleep(1)
        continue

