#! C:\Users\Lucas\AppData\Local\Programs\Python\Python36-32\python.exe
# 2b-auto
# Description : archive sauvegarde
# Auteur : Lucas CONSEJO
# Date : 06/11/2018

import re
import zipfile


def zipFile():
    zip = zipfile.ZipFile('sauvegarde.tar.gz', 'w')
    zip.write('1a-add.py')
    zip.close()

zipFile()


# Rendre dimanche 11/11  23h59
# jusqu'au 3c-ssh.py --> au moins la logique 
# scripts