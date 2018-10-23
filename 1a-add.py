#! C:\Users\Lucas\AppData\Local\Programs\Python\Python36-32\python.exe
# 1a-add
# Description : Addition de 2 nombres
# Auteur : Lucas CONSEJO
# Date : 15/10/2018

import re

print('ADDITION')
pattern = re.compile("^\S[0-9]*$")
nombre1 = input("Entrez le premier nombre : ") #Saisie 1er nombre

#boucle tant que la saisie n'est pas un nombre valide
while not pattern.match(nombre1):
    nombre1 = input("veuillez entrer un premier nombre correct : ")

nombre2 = input("Entrez le second nombre : ") #Saisie 2nd nombre

#boucle tant que la saisie n'est pas un nombre valide
while not pattern.match(nombre2):
    nombre2 = input("veuillez entrer un second nombre correct : ")

#fonction qui additionne les 2 nombres de l'utilisateur, puis affiche le résultat
def addition(nb1, nb2):
    nb1 = int(nb1)
    nb2 = int(nb2)
    result = str(nb1 + nb2)
    print(str(nb1)+" + "+str(nb2)+" = "+ result)

addition(nombre1, nombre2)
input("\n(Appuyer sur Entrer pour quitter)")