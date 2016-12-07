
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

def texto_min():
    archivo=open('integrantes100kb.txt','w')
    archivo.close()
    archi=open('integrantes100kb.txt','a')
    for i in range(len(archivo_min)):
        archi.write(archivo_min[i])
    archi.close()
    
def texto_max():
    archivo=open('integrantes1000kb.txt','w')
    archivo.close()
    archi=open('integrantes1000kb.txt','a')
    for i in range(len(archivo_max)):
        archi.write(archivo_max[i])
    archi.close() 

texto_min()
texto_max()
