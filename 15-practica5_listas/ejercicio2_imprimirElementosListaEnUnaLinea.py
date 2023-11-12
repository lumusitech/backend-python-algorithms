"""Ejercicio 2 - Practica 5: Mostrar en una linea los elementos de una lista
separados por un espacio usando funciones y lista"""
lista=["casa","barco","torre","mirador"]
def mostrarEnUnaLinea(lista):
    i=0
    while i<len(lista):
        print(lista[i],end=" ")
        i+=1

#programa
mostrarEnUnaLinea(lista)

##############################################################################
print("\n")
def mostrarEnUnaLinea2(lista):
    for i in range(len(lista)):
        print(lista[i],end=" ")

#programa
mostrarEnUnaLinea2(lista)

##############################################################################
print("\n")
def mostrarEnUnaLinea3(lista):
    for elemento in lista:
        print(elemento,end=" ")

#programa
mostrarEnUnaLinea3(lista)