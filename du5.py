#Máte string: "   Python   "
#Odstráňte medzery na začiatku, na konci a na oboch stranách.
#Vypíšte všetky tri varianty (každú v apostrofoch aby boli vidieť medzery)
string = "   Python   "
print(f"'{string.lstrip()}'")  # Odstránenie medzier na začiatku
print(f"'{string.rstrip()}'")  # Odstránenie medzier na konci
print(f"'{string.strip()}'")   # Odstránenie medzier na oboch stranách  