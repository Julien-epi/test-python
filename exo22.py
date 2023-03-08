def compterMots(chaine):
    comptes = {}
    
    mots = chaine.split()
    
    for mot in mots:
        if mot in comptes:
            comptes[mot] += 1
        else:
            comptes[mot] = 1
            
    return comptes
