#!/usr/bin/env python

# Visitor Design Pattern

# Abstract base classes support framework
from abc import ABCMeta, abstractmethod

import xml.etree.ElementTree as ET
import json

class Inventory(metaclass=ABCMeta):

    @abstractmethod
    def accept(self, visitor):
        pass

class Book(Inventory):

    def __init__(self, name, author, no_of_pages):
        self.name = name
        self.author = author
        self.no_of_pages = no_of_pages

    def accept(self, visitor):
        visitor.visit_book(self)

class AudioCD(Inventory):

    def __init__(self, name, artist, no_of_disks):
        self.name = name
        self.artist = artist
        self.no_of_disks = no_of_disks

    def accept(self, visitor):
        visitor.visit_audio_cd(self)

class Visitor(metaclass=ABCMeta):

    @abstractmethod
    def visit_book(self, book):
        pass

    @abstractmethod
    def visit_audio_cd(self, audio_cd):
        pass    

class XmlVisitor(Visitor):

    def visit_book(self, book):
        data = ET.Element('book')
        ET.SubElement(data, 'name').text = book.name
        ET.SubElement(data, 'author').text = book.author
        ET.SubElement(data, 'pages').text = str(book.no_of_pages)
        print(ET.tostring(data, encoding='unicode'))

    def visit_audio_cd(self, audio_cd):
        data = ET.Element('audio_cd')
        ET.SubElement(data, 'name').text = audio_cd.name
        ET.SubElement(data, 'artist').text = audio_cd.artist
        ET.SubElement(data, 'disks').text = str(audio_cd.no_of_disks)
        print(ET.tostring(data, encoding='unicode'))

class JsonVisitor(Visitor):

    def visit_book(self, book):
        data = {}
        data['book'] = ({
            'name' : book.name,
            'author' : book.author,
            'pages' : book.no_of_pages
        })
        print(json.dumps(data))

    def visit_audio_cd(self, audio_cd):
        data = {}
        data['audio_cd'] = ({
            'name' : audio_cd.name,
            'artist' : audio_cd.artist,
            'disks' : audio_cd.no_of_disks
        })
        print(json.dumps(data))

def main():
    book = Book("Design Patterns: Elements of Reusable Object-Oriented Software", "GoF", 416)
    audio_cd = AudioCD("Complete Clapton", "Eric Clapton", 2)
    
    xmlPrinter = XmlVisitor()
    jsonPrinter = JsonVisitor()

    book.accept(xmlPrinter)
    audio_cd.accept(xmlPrinter)
    book.accept(jsonPrinter)
    audio_cd.accept(jsonPrinter)

if __name__ == "__main__":
    main()