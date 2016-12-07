#ESCUELA POLITECNICA NACIONAL
#ESCUELA DE FORMACION DE TECNOLOGOS

#PROGRAMACION AVANZADA

#EXAMEN BIMESTRAL

#FECHA:07-12-2016

import sys
from time import time

## Datos globales

nombre1 = "Josue Cando "
nombre2= "Bryan Pilatuña "
nombre3 ="Lizeth Toasa "
nombre4="Edison Chulde "
nombre5 = "Katherine Montoya"
inte1 = [nombre1,len(nombre1)]
inte2 = [nombre2,len(nombre2)]
inte3 = [nombre3,len(nombre3)]
inte4 = [nombre4,len(nombre4)]
inte5 = [nombre5,len(nombre5)]
intes = [inte1,inte2,inte3,inte4,inte4]
archivo_min = []
archivo_max = []
lista_multiple = []
lista_simple = []
guardar_resultados = []

def menu_princ():
    print("\t\tESCUELA POLITECNICA NACIONAL")
    print("\t\tESCUELA DE FORMACION DE TECNOLOGOS")
    print("\t\t***MENU PRINCIPAL***")
    print("1.-Creacion de archivos")
    print("2.-Concurrencia")
    print("3.-Volumen de una piscina")
    print("4.-Salir")

def menu_piscina():
    print("\t**CALCULO DEL VOLUMEN DE UNA PISCINA**")
    print("1.-Forma rectangular ")
    print("2.-Forma eliptica")
    print("3.-Forma circular")
    print("4.-Regresar al Menu Principal")

def rect():
    largo=float(input("Ingrese el largo: "))
    ancho=float(input("Ingrese el ancho: "))
    prof=float(input("Ingrese la profundidad: "))
    volumen=largo*ancho*prof
    print("El volumen de forma rectagular es:",volumen)

def elip():
    largo=float(input("Ingrese el largo: "))
    ancho=float(input("Ingrese el ancho: "))
    prof=float(input("Ingrese la profundidad: "))
    pi=3.1416
    volumen=(4/3)*pi*largo*ancho*prof
    print("El volumen de forma eliptica es:",volumen)

def circ():
    radio=float(input("Ingrese el radio: "))
    altura=float(input("Ingrese la altura: "))
    pi=3.1416
    volumen=pi*radio*radio*altura
    print("El Volumen de una piscina Circular es:",volumen)
    
def reg():
    x=int(input("\nDesea repetir el proceso 1=SI 2=NO: "))
    if x==1:
        menu_piscina()
        piscina()
    else:
        main()
    
def piscina():
        opc=int(input("\nIngrese la opcion que desea:"))
 
        if opc==1:
            print("\nForma rectangular")
            rect()
            reg()
        
        if opc==2:
            print("\nForma eliptica")
            elip()
            reg()

        if opc==3:
            print("\nForma circular")
            circ()
            reg()
            
        if opc==4:
            main()
#
def tamanio(lista):
    tam = 0
    for i in range (0,len(intes)):
        for j in range(0,1):
            tam = intes[i][-1]+tam
    return tam

def texto_mini():
    tam = 0
    while tam <=100000:
        for i in range (0,len(intes)):
            for j in range(0,1):
                archivo_min.append(intes[i][0])
        tam= tam+tamanio(intes)
texto_mini()

def texto_max():
    tam = 0
    while tam <=1000000:
        for i in range (0,len(intes)):
            for j in range(0,1):
                archivo_max.append(intes[i][0])
        tam= tam+tamanio(intes)
texto_max()

def creacion_texto_min():
    archivo=open('integrantes100kb.txt','w')
    archivo.close()
    archi=open('integrantes100kb.txt','a')
    for i in range(len(archivo_min)):
        archi.write(archivo_min[i])
    archi.close()
    
def creacion_texto_max():
    archivo=open('integrantes1000kb.txt','w')
    archivo.close()
    archi=open('integrantes1000kb.txt','a')
    for i in range(len(archivo_max)):
        archi.write(archivo_max[i])
    archi.close() 
def lectura():
    archivo = open("integrantes100kb.txt","r")
    linea = archivo.readline()
    while linea != "":
        minusc = linea.lower()
        separar = minusc.split()
        lista_multiple.append(separar)
        linea = archivo.readline()
    archivo.close()
def transformar(lista):
    for i in range(0,len(lista)):
        for j in range(0,len(lista[i])):
            palabra = lista[i][j]
            lista_simple.append(palabra)
def busqueda(lista,palabra):
    contador = 0
    busqueda = False
    inicio = time()
    for i in range(0,len(lista)):
        if lista[i] == palabra:

            contador = contador+1
            busqueda = True
    if busqueda == True:
        final = time()
        tiempo = final-inicio
        print(palabra,"se repite",contador,"Tiempo:",tiempo)
        guardar_resultados.append(guardar(palabra,contador,tiempo))
    else:
        print("No existe")

def guardar (palabra,cantidad,tiempo):
    lista = []
    lista.append(palabra)
    lista.append(cantidad)
    lista.append(tiempo)
    return lista

def grabar(lista):
    archivo = open("resultado.txt","w")
    archivo.close()
    archivo = open("resultado.txt","a")
    archivo.writelines(lista)
    archivo.close()
    
def main():
    menu_princ()
    selec=int(input("\nIngrese la opcion que desea: "))
    
    if selec==1:
        texto_mini()
        texto_max()
        creacion_texto_min()
        creacion_texto_max()
        print("Se crearon los archivos\n")
        main()
        
    if selec==2:
        lectura()  
        transformar(lista_multiple)
        palabra = input("Busqueda: ")
        while palabra !="":
            busqueda(lista_simple,palabra)
            palabra = input("Busqueda: ")
        if len(guardar_resultados) !=0:
            print("\nTermino! \nHistorial:"+"\n"+str(guardar_resultados)+"\nSe generó un scrip de su busqueda\n")
            grabar(str(guardar_resultados))
        else:
            print("No realizó ninguna busqueda!\n")
        main()

    if selec==3:
        menu_piscina()
        piscina()
            
    if selec==4:
        sys.exit()


main()
