# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 18:54:04 2023

@author: Usuario
"""
#USO IF Y ELSE
datos = 1
nativa  = 100
if datos == nativa:
    print("Las VLAN son iguales")
else:
    print("Las VLAN son diferentes")
    
#USO DE IF ELIF ELSE
edad=int(input("Ingrese la edad:"))
if edad >=18 and edad <= 45:
    print("Es un adulto joven")
elif edad >=45 and edad <= 59:
    print("Es un adulto medio")
elif edad >=65 and edad <=75:
    print("Es un adulto mayor")
elif edad >=75 and edad <= 90:
    print("Es un anciano")
else:
    print("Es un adolescente")