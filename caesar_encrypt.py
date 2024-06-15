#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: caesar_encrypt.py
Created on Thu Jun 13 09:31:42 2024
This code creates an encrypted Text from your Input.
You havte to give a Keynumber for the Ammount for shifting the Alphabet.
@author: Ulrich Semar
"""
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
       
text = input("Please insert your Text for Encrypting:")
key = int(input("Please insert a Number between 1 and 26:"))

def encrypt(text,key,abc):
           text = text.lower() #Alle zeichen zu kleinen Buchstaben umwandeln
           code = [] #Leere Liste für das verschobene Alphabet
           code.extend(abc[key:]) #Neues alphabet ab Verschiebung erzeugen mit splice des Key werts
           cutpart = abc[:key] #Den fehlenden Teil von abc ermitteln
           code = code + cutpart #Den fehlenden Teil an das neue verschobene Alphabet mit dem Namen code anfügen
           crypted = [] #Leere Liste für die Übersetzung aus abc in code
           for abc in text: #Nach den Buchstaben des Textes im abc suchen
              codind = text.index(abc) #Index im Alphabet ermitteln
              crypted.append(code[codind]) #Index vom Alphabet auf Code übertragen
           return ("".join(map(str, crypted))) #String erzeugen und ausgeben
print (encrypt(text,key,abc)) #Funktion aufrufen
