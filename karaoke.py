#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import os


class KaraokeLocal(ContentHandler):

    def __init__(self, parametro):
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(sys.argv[1]))
        self.lista = sHandler.get_tags()

    def __str__(self):
        val_atr = []
        for i in range(len(self.lista)):
            if type(self.lista[i]) == dict:
                diccionario = self.lista[i]
                lista_tupla = diccionario.items()
                for j in range(len(lista_tupla)):
                    val_atr.append(str((lista_tupla[j])[0]) + "=" +
                                   str((lista_tupla[j])[1]))
                    if j == (len(lista_tupla) - 1):
                        print "\t".join(val_atr)
                        val_atr = []
            else:
                val_atr.append(self.lista[i])

    def do_local(self):
        for i in range(len(self.lista)):
            if type(self.lista[i]) == dict:
                diccionario = self.lista[i]
                lista_tupla = diccionario.items()
                for j in range(len(lista_tupla)):
                    if str((lista_tupla[j])[0]) == 'src':
                        recurso = str((lista_tupla[j])[1])
                        if recurso[:7] == "http://":
                            os.system("wget -q " + recurso)
                            diccionario["src"] = recurso[recurso.rfind('/')
                                                         + 1:]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python karaoke.py file.smil")
    karaoke = KaraokeLocal(sys.argv[1])
    karaoke.__str__()
    karaoke.do_local()
    karaoke.__str__()
