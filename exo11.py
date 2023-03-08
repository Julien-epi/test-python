nombre = 0

while nombre < 1 or nombre > 10:
    nombre = input("Entrez un entier entre 1 et 10 : ")
    nombre = int(nombre)
    if nombre < 1 or nombre > 10:
        print("La saisie doit être comprise entre 1 et 10.")

print("Vous avez saisi :", nombre)
