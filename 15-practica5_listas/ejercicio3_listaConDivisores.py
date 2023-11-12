"""Ejercicio 3 - Practica 5: Funcion que devuelve una lista de divisores de un
entero dado"""
numero=150
def listaDivisores(numero):
    i=1
    listaDivisores=[]
    while i<numero+1:
        if not numero%i:
            listaDivisores.append(i)
        i+=1
    return listaDivisores

#Programa
print(listaDivisores(numero))

#############################################################################
def listaDivisores2(numero):
    listaDivisores=[]
    for i in range(1,numero+1):
        if not numero%i:
            listaDivisores.append(i)
    return listaDivisores

#programa
print(listaDivisores2(numero))
