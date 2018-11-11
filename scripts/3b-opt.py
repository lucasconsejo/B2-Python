#! C:\Users\Lucas\AppData\Local\Programs\Python\Python36-32\python.exe
# 3b-opt
# Description : archive sauvegarde optimisé
# Auteur : Lucas CONSEJO & Théo FERREIRA
# Date : 10/11/2018

import signal
import shutil
import gzip
import os
import sys
import subprocess
import argparse


# Fonction qui ferme le programme
def fermeture(signal, frame):
    exit()

signal.signal(signal.SIGINT, fermeture)


# Fonction qui permet de choisir le chemin du dossier 'Data'
def cheminData():
    arguments = argparse.ArgumentParser()
    arguments.add_argument("-p", "--path", help="chemin vers le dossier à archiver")
    args = arguments.parse_args()
    if args.path:
        return args.path
    else:
        return '../scripts'


# Fonction qui archive une sauvegarde
def sauvegarde():
    os.remove(dossierData + '/archive.tar.gz')
    shutil.move(archive + '.tar.gz', dossierData)


# Fonction qui supprime l'archive
def deleteSauvegarde():
    if os.path.exists(archive + '.tar.gz'):
        os.remove(archive + '.tar.gz')

dossierData = os.path.expanduser(cheminData()+'/data/')
dossierScripts = os.path.expanduser('../scripts')
archive = os.path.expanduser('./archive')

# Création du dossier 'Data'
os.makedirs(dossierData, exist_ok=True)
sys.stdout.write('Le dossier \'data\' vient d\'être créé.\n')

shutil.make_archive(archive, 'gztar', dossierScripts)

# On verifie s' il existe une sauvegarde
if os.path.exists(dossierData + '/archive.tar.gz'):

    with gzip.open(dossierData + '/archive.tar.gz', 'rb') as f:
        exist_save = f.read()

    with gzip.open(archive + '.tar.gz', 'rb') as f:
        new_save = f.read()

    if exist_save != new_save:
        sauvegarde()
        sys.stdout.write('La sauvegarde a été archivé dans le dossier \'data\'.\n')

    else:
        deleteSauvegarde()
        sys.stdout.write('Une erreur s\'est produite lors de la sauvegarde.\n')

else:
    shutil.move(archive + '.tar.gz', dossierData)
    sys.stdout.write('La sauvegarde a été archivé dans le dossier \'data\'.\n')
