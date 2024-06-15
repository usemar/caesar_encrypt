#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: caesar_encrypt.py
Created on Thu Jun 13 09:31:42 2024
This Code creates an encrypted Text from your Input.
It works only with the Chars in the list "alpha_b". 
You havte to give a Keynumber for the Ammount for shifting the Alphabet.
@author: Ulrich Semar
"""
alpha_b = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
     
text = input("Enter your Text for Encrypting:")
key = int(input("Enter a Number between 1 and 26:"))

def encrypt(text,alpha_b,key):
           text = text.lower()
           code = []
           indx = []
           encryptd = []
           code.extend(alpha_b[key:])
           code = code + alpha_b[:key]
           for i in range(len(text)):
               if text[i] in alpha_b:
                indx.append(alpha_b.index(text[i]))
           for n in indx:     
               encryptd.append(code[n]) 
           return ("".join(map(str, encryptd)))#String erzeugen und ausgeben
print (encrypt(text,alpha_b,key))
