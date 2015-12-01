import xml.etree.ElementTree as ET
import unittest, sys

class Info:
    @staticmethod
    def fileNotFound(path):
        print ("File: " + path + " - not found!")

    @staticmethod
    def invalidFile(path):
        print ("File: " + path + " - has an invalid construction.")

class Parser:

    def __init__(self, path):
        self.path = path
        self.catalog = []
 
    def __parseFile(self):
        return ET.parse(self.path)
    def __parseXml(self):
        tree = self.__parseFile()
        data = self.__getDataFromXml(tree)
        self.catalog = data

    def __getDataFromXml(self, tree):
        root = tree.getroot()
        catalog = []
        for child in root:
            childElements = []
            for innerChild in child:
                childElements.append(innerChild.text)
            catalog.append(childElements)
        return catalog

    def run(self):
        try:
            self.__parseXml()
        except IOError:
            Info.fileNotFound(self.path)
        except ET.ParseError:
            Info.invalidFile(self.path)    

    def __repr__(self):
        out = ''
        for i in self.catalog:
            out += '_id: ' + i[0] + '\n'
            out +='    --> author: ' +  i[1] + '\n'
            out += '    --> title: ' +  i[2] + '\n'
            out += '    --> genre: ' +  i[3] + '\n'

        return out

if __name__ == '__main__':
    p = Parser('xml_files/Books.xml')
    p.run()
    print(p)

