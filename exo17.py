email = input("Entrez un email : ")

if "@" in email and "." in email:
    parts = email.split(".")
    if len(parts) <= 3:
        print("L'email est valide")
    else:
        print("L'email n'est pas valide")
else:
    print("L'email n'est pas valide")
