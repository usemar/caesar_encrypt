#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: caesar_encrypt.py
Created on Thu Jun 13 09:31:42 2024
This code creates an encrypted Text from your Input.
You havte to give a Keynumber for the Ammount for shifting the Alphabet.
@author: Ulrich Semar
"""
alpha_b = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
     
text = input("Text für verschlüsselung eingeben:")
key = int(input("Bitte eine Zahl zwischen 1 und 25 eingeben:"))

def encrypt(text,abc,key):
           text = text.lower()
           code = []
           index = []
           crypted = []#leere Liste
           code.extend(abc[key:])#neues verschlüsselung erzeugen mit splice verschiebung des Key werts
           code = code + abc[:key]
           for i in range(len(text)):
               if text[i] in abc:
                index.append(abc.index(text[i]))
                crypted.append(code[index[i]])   
           return ("".join(map(str, crypted)))#String erzeugen und ausgeben
print (encrypt(text,alpha_b,key))
