#! C:\Users\Lucas\AppData\Local\Programs\Python\Python36-32\python.exe
# 1c-moy
# Description : Top 5 des meilleurs élèves
# Auteur : Lucas CONSEJO
# Date : 15/10/2018

import re

print('MOYENNE ELEVE')
pattern = re.compile("^\S[a-zA-Z]+\s[0-9]+$")
print("(Entrez 'q' pour quitter)\n")

listEleve = {}
moyenne = []

eleve = input("Entrez un nom d'élève et une note : ") # Saisie de l'élève et de sa note par l'utilisateur

# Fonction pour calculer la moyenne des élèves
def calculMoy(moyenne):
    moy = 0
    counter = 0

    for note in moyenne:
        counter += 1
        moy += note

    moy = moy/counter
    print("\nLa moyenne des élèves est de "+str(moy)+"\n") 


# Fonction pour afficher le Top 5 des meilleurs élèves
# Si le nombre d'élève est inférieur à 5, alors on affiche tous les élèves dans l'ordre des meilleurs
def classementEleve(listTrier):
    if len(listTrier) >= 5:
        for i in range(0, 5):
            print("N°"+str(i+1)+" : "+str(listTrier[i][0])+" avec une note de "+str(listTrier[i][1]))
    else:
        for i in range(0, len(listTrier)):
            print("Le n°"+str(i+1)+" est "+str(listTrier[i][0])+" avec une note de "+str(listTrier[i][1]))


# Fonction qui vérifie la saisie de l'utilisateur / Trier dans l'ordre des meilleurs notes /
# Appelle la fonction de la moyenne / Appelle la fonction du classement des élèves
def topEleve(eleve):
    while eleve != 'q':
        if(pattern.match(eleve)):
            saisie = eleve.split(" ")
            nomEleve = saisie[0]
            note = int(saisie[1])
            moyenne.append(note)
            listEleve[nomEleve] = note
            eleve = input("Entrez un nom d'élève et une note : ")
        else:
            print("Format incorrect...Veuillez réessayer\n")
            eleve = input("Entrez un nom d'élève et une note : ")

    listTrier = sorted(listEleve.items(), reverse=True, key=lambda t: t[1])

    calculMoy(moyenne)
    classementEleve(listTrier)
    
topEleve(eleve)

input("\n(Appuyer sur Entrer pour quitter)")