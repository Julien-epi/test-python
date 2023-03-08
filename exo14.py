liste = [17, 38, 10, 25, 72]

liste.sort()
print("Liste triée : ", liste)

liste.append(12)
print("Liste avec élément ajouté : ", liste)

liste.reverse()
print("Liste inversée : ", liste)

print("Indice de l'élément 17 : ", liste.index(17))

liste.remove(38)
print("Liste avec élément supprimé : ", liste)

print("Sous-liste du 2e au 3e élément : ", liste[1:3])

print("Sous-liste du début au 2e élément : ", liste[:2])

print("Sous-liste du 3e élément à la fin de la liste : ", liste[2:])

print("Sous-liste complète de la liste : ", liste[:])