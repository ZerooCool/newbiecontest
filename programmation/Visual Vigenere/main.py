#! /usr/bin/env python3
# coding: utf-8

from fonctions import get, post

import binascii
import re
from PIL import Image
import io

chemin = '/home/florian/dev/challenges/newbiecontest/programmation/Visual Vigenere/imgcrypted.png'
pngMagicNumbers = '89504e470d0a1a0a'

f = open(chemin, 'rb')
content = f.read()
texte = binascii.hexlify(content).decode('ascii')
# print(texte)
nombreDePng = texte.count(pngMagicNumbers)
if nombreDePng != 3:
    exit('Il y a '+nombreDePng+' PNG au lieu de 3')
# on recupère chaque images
images = texte.split(pngMagicNumbers)
pngStrings = []
pngs = []
# on ajoute le suffixe
for image in images:
    if image:
        pngStrings += [pngMagicNumbers+image]
# on convertit chaque pngString en Image Pillow
for i, pngString in enumerate(pngStrings):
    fichier = 'png'+str(i+1)+'.png'
    fout = open(fichier, 'wb')
    fout.write(binascii.unhexlify(pngString))
    fout.close()
    try:
        im = Image.open(fichier)
        pngs += [im]
    except Exception as e:
        print("erreur : ", e)
        exit()
