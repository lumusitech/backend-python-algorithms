"""Ejercicio 5 - Practica 5: Funcion que devuelve True si los enteros de una
lista son factores de un numero dado"""
n=41
lista=[1,2,4,5,10,20]

def sonFactores(n,lista):
    for i in lista:
        if n%i:
            return False
            break
    return True


#Programa
print(sonFactores(n,lista))
