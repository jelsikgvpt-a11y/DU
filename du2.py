#Máte vetu: "Python je skvelý programovací jazyk"
#Zistite dĺžku vety a koľkokrát sa v nej vyskytuje písmeno 'a'.
#Výsledky vypíšte vo formáte: "Dĺžka: X, Počet 'a': Y"
veta = "Python je skvelý programovací jazyk"
dlzka = len(veta)   
pocet_a = veta.count('a')
print(f"Dĺžka: {dlzka}, Počet 'a': {pocet_a}")