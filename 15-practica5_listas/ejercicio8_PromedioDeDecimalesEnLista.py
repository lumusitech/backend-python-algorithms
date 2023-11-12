"""Ejercicio 8 - Practica 5: Da el promedio de decimales dentro de una lista"""

def promedio(lista):
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]
    return suma/len(lista)


#programa
lista=[7.5,3.66,9.5,6.33]
print(promedio(lista))