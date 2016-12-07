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
    x=int(input("\nDesea repetir el proceso 1:SI 2:NO: "))
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

def main():
    menu_princ()
    selec=int(input("\nIngrese la opcion que desea: "))
    
    if selec==1:
        print("Hola")
        
    if selec==2:
        print("Adios")

    if selec==3:
        menu_piscina()
        piscina()
            
    if selec==4:
        sys.exit()


main()




