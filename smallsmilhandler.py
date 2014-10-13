#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.etiquetas = {
            "root-layout": ["width", "heigth", "background-color"],
            "region": ["id", "top", "bottom", "left", "right"],
            "img": ["src", "region", "begin", "dur"],
            "audio": ["src", "begin", "dur"],
            "textstream": ["src", "region"]
        }
        self.lista = []

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        dic_attrs = {}
        if name == 'root-layout':
            self.lista.append(str(name))
            # De esta manera tomamos los valores de los atributos
            for atributo in attrs.keys():
                dic_attrs[str(atributo)] = str(attrs.get(atributo, ""))

            self.lista.append(dic_attrs)
        elif name == 'region':
            self.lista.append(str(name))

            for atributo in attrs.keys():
                dic_attrs[str(atributo)] = str(attrs.get(atributo, ""))

            self.lista.append(dic_attrs)
        elif name == 'img':
            self.lista.append(str(name))

            for atributo in attrs.keys():
                dic_attrs[str(atributo)] = str(attrs.get(atributo, ""))

            self.lista.append(dic_attrs)
        elif name == 'audio':
            self.lista.append(str(name))

            for atributo in attrs.keys():
                dic_attrs[str(atributo)] = str(attrs.get(atributo, ""))

            self.lista.append(dic_attrs)
        elif name == 'textstream':
            self.lista.append(str(name))

            for atributo in attrs.keys():
                dic_attrs[str(atributo)] = str(attrs.get(atributo, ""))

            self.lista.append(dic_attrs)

    def get_tags(self):
        return self.lista

if __name__ == "__main__":
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    print sHandler.get_tags()
