#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import os

parser = make_parser()
sHandler = SmallSMILHandler()
parser.setContentHandler(sHandler)
parser.parse(open(sys.argv[1]))
lista = sHandler.get_tags()

if len(sys.argv) != 2:
    sys.exit("Usage: python karaoke.py file.smil")

val_atr = []
for i in range(len(lista)):
    if type(lista[i]) == dict:
        diccionario = lista[i]
        lista_tupla = diccionario.items()
        for j in range(len(lista_tupla)):
            val_atr.append(str((lista_tupla[j])[0]) + "=" + 
            str((lista_tupla[j])[1]))
            if j == (len(lista_tupla) - 1):
                print "\t".join(val_atr)
                val_atr = []
    else:
        val_atr.append(lista[i])
