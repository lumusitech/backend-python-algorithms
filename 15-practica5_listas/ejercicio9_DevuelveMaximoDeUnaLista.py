#Ejercicio 9 - Practica 5: Devuelve el valor maximo de una lista

def maximo(lista):
    maximo=lista[0]
    for i in range(1,len(lista)):
        if lista[i]>maximo:
            maximo=lista[i]
    return maximo

#prrograma
listaA=[8,6,2,4]
print(maximo(listaA))