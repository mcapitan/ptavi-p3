#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
import os

parser = make_parser()
lista_SSH = smallsmilhandler.SmallSMILHandler()
parser.setContentHandler(lista_SSH)
parser.parse(open('karaoke.smil'))    

lista = lista_SSH.get_tags()

val_atri = []
for i in range(len(lista)):
    if type(lista[i]) == dict:
        diccionario = lista[i]
        lista_tupla = diccionario.items()

        for j in range(len(lista_tupla)):
            val_atri.append(str((lista_tupla[j])[0]) + "=" + 
                            str((lista_tupla[j])[1]))
            if str((lista_tupla[j])[0]) == 'src':
                recurso = str((lista_tupla[j])[1])
                if recurso[:7] == "http://":
		            os.system("wget -q " + recurso)
            if j == (len(lista_tupla) - 1):
                print "\t".join(val_atri)
                val_atri = []
    else:
        val_atri.append(lista[i])
