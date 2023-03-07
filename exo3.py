nombre = float(input("Entrez un nombre: "))

if nombre >= 0:
    racine = (nombre ** 0.5)
    racine_arrondie = round(racine, 2)
    print("La racine carrée de", nombre, "est", racine_arrondie)
else:
    print("Erreur: le nombre saisi est négatif.")
