import random

isimler = ["Mustafa", "Zülal", "Hüseyin", "Ayşe", "Kamile", "Feyza", "Mehmet"]

def hediye_cekilisi():
    alanlar = isimler.copy()
    verenler = isimler.copy()
    
    for alici in alanlar:
        verici = random.choice(verenler)
        
        while verici == alici:
            verici = random.choice(verenler)
        
        print(verici, "=> şu kişi buna hediye alacak =>", alici)
        
        verenler.remove(verici)

hediye_cekilisi()

