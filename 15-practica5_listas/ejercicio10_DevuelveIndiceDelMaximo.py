"""Ejercicio 10 - Practica 5: Devuelve el indice del maximo elemento de una
lista"""
def maximoIndice(lista):
    maximo=lista[0]
    for i in range(1,len(lista)):
        if lista[i]>maximo:
            maximo=lista[i]



    for i in range(len(lista)):
        if maximo==lista[i]:
            return i

#programa
lista=[120,35,1400,36,56,360]
print(maximoIndice(lista))

