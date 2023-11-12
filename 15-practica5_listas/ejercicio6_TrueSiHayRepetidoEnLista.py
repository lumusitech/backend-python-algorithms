"""Ejercicio 6 - Practica 5: Funcion devuelve True si hay algun elemento
repetido en una lista dada"""
lista=[0,3,5,3,6,1,"casa","auto"]
def repetido(lista):
    cont=0
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i]==lista[j]:
                cont+=1

    if cont>len(lista):
        return True
    else:
        return False

#Programa
print(repetido(lista))
