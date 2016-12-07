from time import time
## Busqueda de la palabra

lista_multiple = []
lista_simple = []
guardar_resultados = []
def lectura():
    archivo = open("integrantes100kb.txt","r")
    linea = archivo.readline()
    while linea != "":
        minusc = linea.lower()
        separar = minusc.split()
        lista_multiple.append(separar)
        linea = archivo.readline()
    archivo.close()
lectura()
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
    
lectura()  
transformar(lista_multiple)

palabra = input("Busqueda: ")
while palabra !="":
    busqueda(lista_simple,palabra)
    palabra = input("Busqueda: ")
if len(guardar_resultados) !=0:
    print("\nTermino! \nHistorial:"+"\n"+str(guardar_resultados)+"\nSe generó un scrip de su busqueda")
    grabar(str(guardar_resultados))
else:
    print("No realizó ninguna busqueda!")

