mot1 = input("Entrez un premier mot: ")
mot2 = input("Entrez un deuxième mot: ")

if mot1 < mot2:
    print("Le mot le plus petit est:", mot1)
elif mot1 > mot2:
    print("Le mot le plus petit est:", mot2)
else:
    print("Les deux mots sont identiques.")
