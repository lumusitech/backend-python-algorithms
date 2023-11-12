#Ejercicio 22 - Practica 5:

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
            print (letra, ": ",cantApariciones(letra,cadena))
            listaAparecidos.append(letra)

palabra=input("Ingrese una palabra")
print(palabra)
imprimeCantidadApariciones(palabra)

#Analizar profundamente anotando en papel cada paso con una palabra sencilla de
#3 letras como ala para que sea mas sencillo entender el proceso completo