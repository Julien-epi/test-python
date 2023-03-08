

mail = input("Tapez votre adresse mail: ")

if "@" in mail and ".com" in mail:
    print("Adresse mail valide")
else:
    print("Adresse mail invalide")