# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:52:27 2023

@author: Usuario
"""

#Secuencial for
lista2=[]
lista = ["R1","R2","R3","S1","S2","S3"]
print(len(lista))
"""
print(lista[0])
print(lista[5])
"""
for item in lista:
    if "R" in item:
        lista2.append(item)
        #print(item,end="*")