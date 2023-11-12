#Ejercicio 23 - Practica 5:

def cantApariciones(letra,cadena):
    cant=0
    for i in range(len(cadena)):
        if (letra==cadena[i]):
            cant+=1
    return (cant)

def imprimeCantidadApariciones(cadena):
    listaAparecidos=[]
    for i in range(len(cadena)):
        letra=cadena[i]
        if (cantApariciones(letra,listaAparecidos)==0):
            print (letra, ": ", end=" ")
            print("*"*cantApariciones(letra,cadena))
            listaAparecidos.append(letra)

palabra=input("Ingrese una palabra")
print(palabra)
imprimeCantidadApariciones(palabra)