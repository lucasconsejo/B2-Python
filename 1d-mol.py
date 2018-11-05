#! C:\Users\Lucas\AppData\Local\Programs\Python\Python36-32\python.exe
# 1d-mol
# Description : Plus ou moins
# Auteur : Lucas CONSEJO
# Date : 23/10/2018

import re
import random
import signal
import sys
from time import sleep

print('PLUS OU MOINS\n')
print("Vous devez trouver le nombre compris entre 0 et 100")
pattern = re.compile("[0-9]+$")
print("(Entrez 'q' pour quitter)\n")

nbAleatoire = random.randint(0, 100) # Genere un nombre aléatoire entre 0 et 100
nbCoups = 0

# Fonctions du Plus ou Moins
def plusOuMoins(nbUtilisateur, nbCoups):
    while(nbUtilisateur != "q"):
        if(pattern.match(nbUtilisateur)): # verification d'une saisie correct
            if(int(nbUtilisateur) > nbAleatoire):
                print("C'est moins")
                nbCoups += 1
                nbUtilisateur = input("Entrez un nombre : ")
            elif(int(nbUtilisateur) < nbAleatoire):
                print("C'est plus")
                nbCoups += 1
                nbUtilisateur = input("Entrez un nombre : ")
            else:
                nbCoups += 1
                print("\nFélicitation ! Vous avez trouvé en "+str(nbCoups)+" coups.")
                resultat()
                sleep(1)
                sys.exit(0)
                break 
        else:
            print("Saisie invalide") 
            nbUtilisateur = input("Entrez un nombre valide : ")
    if(nbUtilisateur == "q"):
        resultat()
        sleep(1)
        sys.exit(0)


# Fonction fermeture lors du signal CTRL+C
def fermeture(signal, frame):
    resultat()
    sleep(1)
    sys.exit(0)

# Fonction qui affiche le résultat avant la fermeture  
def resultat():
    print("\nLa solution était "+str(nbAleatoire))
    print("Au revoir !")

signal.signal(signal.SIGINT, fermeture)

nbUtilisateur = input("Entrez un nombre : ") # saisie utilisateur
plusOuMoins(nbUtilisateur,nbCoups)