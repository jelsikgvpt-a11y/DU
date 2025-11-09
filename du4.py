#Máte email: "jan.novak@example.com"
#Rozdeľte ho na používateľské meno a doménu pomocou split().
#Vypíšte vo formáte: "Používateľ: XXX, Doména: YYY"
email = "jan.novak@example.com"
pouzivatel, domena = email.split("@")
print(f"Používateľ: {pouzivatel}, Doména: {domena}")
