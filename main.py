import hashlib

mot_de_passe = ""
mot_de_passe_hasher = ""
majuscule = 0
miniscule = 0
chiffre = 0
caractere = 0
valide = 0


while valide != 1:
    mot_de_passe = input("Choisissez votre mot de passe : ")

    for i in mot_de_passe:

        if i.islower() == True:
            miniscule = 1
            
        elif i.isupper() == True:
            majuscule = 1
            
        elif i == "@" or i == "!" or i == "#" or i == "$" or i == "%" or i == "^" or i == "&" or i == "*":
            caractere = 1

        try:
            i = int(i)
            chiffre = 1
        except ValueError:
            continue
            
        

    if len(mot_de_passe) >= 8 and miniscule == 1 and majuscule == 1 and chiffre == 1 and caractere == 1:
        mot_de_passe_hasher = mot_de_passe
        mot_de_passe_hasher = hashlib.sha256().hexdigest()

        print("Le mot de passe est correct")
        print("Le mot de passe hasher est " + str(mot_de_passe_hasher))
        valide = 1

    else:
        print("ERREUR!!! Ressayez un nouveau mot de passe")

