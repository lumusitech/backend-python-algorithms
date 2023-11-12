#Clase 29-05-17:
#Ejemplo dado de manejo de archivos:

"""Almaceno la lista a en el fichero.txt LINEA A LINEA EN LA PRIMERA VA A LA
LONGITUD A PESAR DE QUE SE PUEDE LEER CON READLINE."""

def CargoLista(a):
    f=open("fichero2.txt","w")#Abre el archivo, si no esta lo crea. En este caso
                              #es txt pero podria haber sido .xls .doc etc.

    f.write (str (len(a))+"\n")#En la 1er linea escribe el len pasado a str
    for i in range (len(a)):
        b=f.write(str(a[i])+"\n")#Escribe los elementos de lista con un salto
    f.close()#Cierra el archivo

lis=[100,200,300,400,500,600]
#Programa
CargoLista(lis)#Pasa como argumento "lis" al parametro "a" de la funcion

###########################################################################

#Lectura del fichero creado:

def LeoLista():
    lista=[]
    f= open("fichero2.txt","r")
    lng=int(f.readline())#Los archivos estan estructurados en registros,
                         #readline nos trae registro por registro (linea a linea)
    for i in range(lng):
        lista.append(int(f.readline()))

    f.close()
    return (lista)
l=LeoLista()
print(l)

###########################################################################
