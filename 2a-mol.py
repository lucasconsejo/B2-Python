#! C:\Users\Lucas\AppData\Local\Programs\Python\Python36-32\python.exe
# 2a-mol
# Description : Plus ou moins avec saisie à l'aide d'un fichier .txt
# Auteur : Lucas CONSEJO
# Date : 05/11/2018

import random
import re
import signal


# Fonction qui affiche le résultat avant la fermeture
def fermeture(signal, frame):
    ecrire('La solution etait '+str(nbAleatoire)+'\nAu revoir !')
    exit()


signal.signal(signal.SIGINT, fermeture)


# Fonctions qui lit la saisie de l'utilisateur dans le fichier .txt
def lire():
    file = open("saisie-2a-mol.txt", "r")
    msg = file.readline().strip()
    file.close()
    return msg


# Fonctions qui écrire une réponse dans le fichier .txt
def ecrire(msg):
    file = open("saisie-2a-mol.txt", "w")
    file.write(msg)
    file.close()


# Fonction qui fait tourner le jeu
def plusOuMoins(finBoucle):
    while(finBoucle is False):
        saisie = lire()

        if(pattern.match(saisie)):
            saisie = int(saisie)

            if(saisie > nbAleatoire):
                ecrire("C'est moins")

            elif(saisie < nbAleatoire):
                ecrire("C'est plus")
            else:
                ecrire('Felicitation\nLa solution etait '+str(nbAleatoire)+'\nAu revoir !')
                finBoucle = True


pattern = re.compile("[0-9]+$")

finBoucle = False
nbAleatoire = random.randint(0, 100)

ecrire('Bienvenue dans le Jeu du Plus ou Moins !')

plusOuMoins(finBoucle)
