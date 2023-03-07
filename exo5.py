pSeuil = 2.3
vSeuil = 7.41

pression = float(input("Entrez la pression: "))
volume = float(input("Entrez le volume: "))

if volume > vSeuil and pression > pSeuil:
    print("Erreur: Arrêt immédiat")
elif pression > pSeuil:
    print("Veuillez augmentr le volume")
elif volume > vSeuil:
    print("Veuillez diminuer le volume")
else:
    print("Tout va bien")