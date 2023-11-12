#Ejercicio: def funcion que llene una lista con la cantidad que diga el usuario
#Usuario: Ingresa cantidad de elementos de una lista
#Generar un ciclo para llenar una lista

#Definicion de funcion:
def llenadoDeLista(i):
    lista=[]
    cont=0
    while(cont<i):
        palabra=input("ingrese una palabra")
        lista.append(palabra)
        cont+=1
    return lista

#Programa
cantidad=int(input("cantidad de palabras que desea ingresar"))
print(llenadoDeLista(cantidad))