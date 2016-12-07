import random
nombre1 = "Josue Cando"
nombre2= "Bryan Pilatuña"
inte1 = [nombre1,len(nombre1)]
inte2 = [nombre2,len(nombre2)]
tamanio = 0
intes = [inte1,inte2]
archivo_min = []
archivo_max = []

def tamanio(lista):
    tam = 0
    for i in range (0,len(intes)):
        for j in range(0,1):
            tam = intes[i][-1]+tam
    return tam

print(tamanio(intes))

def texto_mini():
    tam = 0
    while tam <=100:
        for i in range (0,len(intes)):
            for j in range(0,1):
                archivo_min.append(intes[i][0])
        tam= tam+tamanio(intes)
texto_mini()
print(archivo_min)

def texto_max():
    tam = 0
    while tam <=1000:
        for i in range (0,len(intes)):
            for j in range(0,1):
                archivo_max.append(intes[i][0])
        tam= tam+tamanio(intes)
texto_max()
print(archivo_max)

##def creartxt():
##    archivo=open('integrantes.txt','w')
##    archivo.close()
##creartxt()

##def aleatorio():
##    integrante = "nombre"+str(random.randrange(2))
##    return integrante
##
##
##print(aleatorio())
