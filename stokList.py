import  time
class malzeme():

    def __init__(self,name,piece,price):
        self.name = name
        self.piece = piece
        self.price = price
liste = list()
deterjan = malzeme("Deterjan", "60", "45")
ekmek = malzeme("Ekmek", "150", "2")
yogurt = malzeme("Yoğurt", "30", "12")
bebek_bezi = malzeme("Bebek Bezi", "20", "60")
seker = malzeme("Şeker", "75", "15")
sut = malzeme("Süt", "40", "5")
materialList = [deterjan, ekmek, yogurt, bebek_bezi, seker, sut]
