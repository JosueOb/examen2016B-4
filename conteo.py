def creartxt():
    archi=open('conteo.txt','w')
    archi.close()
    
def grabartxt(a):
    archi=open('conteo.txt','a')
    archi.write("El Total de la palbra Bryan son:\t")
    archi.write(str(a))
    archi.close() 


def leertxt():
    b=0
    archi=open('integrantes1000kb.txt','r')
    linea=archi.readline()
    while linea!="":
        print(linea)
        for i in range(len(linea)):
            if linea[i] =="Bryan":
                b=b+1
        a=len(linea)-b
        linea=archi.readline()
               
    archi.close()
    grabartxt(a)
        
creartxt()       
leertxt()
