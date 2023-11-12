#clase 03-05-17: Funciones predefinidas
import math
#x=float(input("Ingrese un flotante"))
#ai ingresan 1 me daria error porque 1-1 da 0 y 0 no tiene log
#y=math.sqrt(math.log(abs(1-x))) #abs no requiere importar nada como las funciones math
#z=math.pow(a,b) -> toma a base y b exponente
#el_mayor=max(2,5,9,4,1,7) devuelve el valor mayor. Es una funcion predefinida tambien
#print(y)

#######################################################################

#Para definir una funcion se debe usar def mas el nombre de la funcion ()
#en azul se muestran los comandos en celeste los metodos o funciones

#Definir funcion
def mostrarGuion():
    print("-",end="")

def mostrarLinea():
    for i in range(20):
        mostrarGuion()

#prueba del programa
mostrarGuion()

#inprimo algo para verificar que se cumple end=""
print("hola")

########################################################################
#Comienza mi programa principal conviene como habito comentar donde empieza:

#programa principal
print("Lista de compras:")
mostrarGuion()
print("Queso")
mostrarGuion()
print("Leche")
mostrarGuion()
print("Huevos")

#se pueden poner varias sentencias en un renglon usando ;

########################################################################

#En lugar de escribir 6 veces la funcion uso un ciclo for:
mostrarGuion()
mostrarGuion()
mostrarGuion()
mostrarGuion()
mostrarGuion()
mostrarGuion()

print()#es para dar un salto de linea. Rompe el end=""

#Podemos usarlo dentro de un ciclo y lograr separaciones por ejemplo
for i in range(20):
    mostrarGuion()

print()#es para dar un salto de linea

#O podemos hacer una funcion que incorpore todo eso. Se definio arriba mostrarLinea
mostrarLinea()
########################################################################
#Mostrar linea 3 veces

print()

for i in range(3):
    mostrarLinea()

########################################################################

#Cuando hagamos nuestras funciones guardarlas en archivo con extension miFunciones.py
#Cuando las quiera usar uso como siempre - from miFunciones import *
#Por supuesto debe estar en el directorio adecuado de python
#Esto es muy util para trabajar en equipo o recibir, dar funciones creadas por otros por nosotros

########################################################################

#Paso de argumentos a una funcion

cadena="Nunca digas nunca tampoco siempre"

def imprimirDosVeces(argumento):
    print(argumento)
    print(argumento)

imprimirDosVeces(cadena)#a la funcion le pase el argumento cadena, la funcion la toma y guarda en argumento y despues procesa eso.

########################################################################

#Devolucion de valor - return

def area(radio):
    return(math.pi*radio*radio)
    #con esto devuelve el valor de ese calculo

print("El area es" ,area(2))
print("El area es" ,area(3))
a=int(input("Ingrese el radio"))
print("El area es" ,area(a))

########################################################################

#Funciones puras: Una funcion en computacion se considera pura si siempre que se
#la llame con parametros adecuados retorna algun valor y nunca
#tiene efectos colaterales (como imprimir cosas en la pantalla).
#En IP nos gustan las funciones puras.
#Y ademas, a partir de ahora, IP es puras funciones

















