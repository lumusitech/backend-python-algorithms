#10-05-17--------Trabajo con funciones
#Practica 4:
#Ejercicio 15:

#Hacer un programa que solicite al usuario un número a entero positivo e indique cuál es el
#número primo mayor b más cercano. Usar funciones. Por ejemplo, si el usuario ingresa 24, el
#programa devolverá 29 (29 es el número primo más cercano mayor que 24). Si el usuario ingresa
#5 el programa devolverá 7.

def cantidadDivisores(num):
    cont=0
    for div in range(1,num+1): #Cuando es un divisor exacto
        if(num%div==0):
            cont=cont+1
    return cont

def esPrimo(num):
    if(cantidadDivisores(num)==2):
        return True
    else:
        return False

#esPrimo se puede simplificar asi­, sigue devolviendo true o false sin el if
def esPrimo(num):
    return cantidadDivisores(num)==2

def primoCercano(num):   #Devuelve de un primo ingresado el primo mas cercano a este Ej: 5--->7
    numero=num+1
    while(not esPrimo(numero)):
        numero+=1
    return numero

#Estas funciones se pueden guardar en archivo .py para ser usado en otros lados
print(cantidadDivisores(5))
print(esPrimo(5))
print(primoCercano(5))
