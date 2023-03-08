x = int(input("Saisissez le nombre de chaînes à enregistrer : "))

with open("data.txt", "w") as f:
    for i in range(x):
        chaine = input("Saisissez la chaîne numéro {} : ".format(i+1))
        f.write(chaine + "\n")

f.close()
