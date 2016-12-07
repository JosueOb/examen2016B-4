#ESCUELA POLITECNICA NACIONAL
#ESCUELA DE FORMACION DE TECNOLOGOS

#PROGRAMACION AVANZADA

#EXAMEN BIMESTRAL

#FECHA:07-12-2016

import sys

def menu_princ():
    print("\t\tESCUELA POLITECNICA NACIONAL")
    print("\t\tESCUELA DE FORMACION DE TECNOLOGOS")
    print("\t\t***MENU PRINCIPAL***")
    print("1.-Archivos con nombres")
    print("2.-Archivos con repeticiones")
    print("3.-Volumen de una piscina")
    print("4.-Salir")

def rect():
    largo=float(input("Ingrese el largo: "))
    ancho=float(input("Ingrese el ancho: "))
    prof=float(input("Ingrese la profundidad: "))
    volumen=largo*ancho*prof
    print("El volumen de forma rectagular es:",volumen)
