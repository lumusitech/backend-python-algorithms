"""Ejercicio 7 - Practica 5: Devuelve el/los indice/s en el que aparece un
entero dado dentro de una lista, si no esta en la lista devuelve y-1"""
n=20
lista=[0,7,5,6,20,7,35,8,7]

def dondeAparece(n,lista):
    listaAparecidos=[]
    for i in range(len(lista)):
        if n==lista[i]:
            listaAparecidos.append(i)
    if listaAparecidos:
        return listaAparecidos
    else:
        return "y-1"


#programa
print(dondeAparece(n,lista))