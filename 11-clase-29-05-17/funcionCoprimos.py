#Ejercicio del segundo modelo de parcial hecho el 19-05-17 se toma en parcial estudiar: Numeros co-primos
#En el parcial se deben definir las funciones de interseccion, divisores o lo que pida
def coPrimos(num1,num2):
    if len (interseccion(divisores(num1),divisores(num2)))==1:#verifico si en la lista interseccion hay un solo elemento
        if interseccion(divisores(num1),divisores(num2))[0]==1:#verifico si ese solo elemento de la lista es el 1
            return True
##############################################################################
#Otra forma para resolverlo sin el uso de funciones externas
def coPrimos2(num1,num2):
    for i in range(2,num2+1):
        if num1%i==0 and num2%i==0:
            return False
    return True

print(coPrimos2(5,3))
