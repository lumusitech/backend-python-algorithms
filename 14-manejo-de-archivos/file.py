archivo=open("lista.txt","r")
mide=archivo.readline()
lista=archivo.readlines()

for i in range(int(mide)):
    print(lista[i])

archivo.close()

################################################################

archivo=open("lista.txt","a")
archivo.write("\nCiudad")
archivo.close()

################################################################

archivo=openn("lista","w")
