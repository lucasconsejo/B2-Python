#! C:\Users\Lucas\AppData\Local\Programs\Python\Python36-32\python.exe
# 1b-dic
# Description : Ajouter plusieurs nom dans un tableau
# Auteur : Lucas CONSEJO
# Date : 15/10/2018

import re

print('LISTE DE NOM')
pattern = re.compile("^\S[a-zA-Z]+$")
print("(Entrez 'q' pour quitter)\n")

nom = input("Entrez un nom : ")
listeNom = []

#Fonction ajouter des noms à la liste de noms
def ajouterNom(nom):

    #Boucle pour saisir plusieurs noms
    while nom != "q" :
        if pattern.match(nom):
            listeNom.append(nom)
            nom = input("Entrez un nom : ")
        else:
            nom = input("Entrez un nom correct : ")
        
    if len(listeNom) > 0:
        listeNom.sort() #Trier la liste dans l'ordre alphabétique

        #Afficher la liste des noms
        print('\nVoici la liste des noms :')
        for nom in listeNom:
            print(" -"+nom)

ajouterNom(nom)
        
input("\n(Appuyer sur Entrer pour quitter)")