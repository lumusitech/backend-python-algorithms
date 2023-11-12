#Ejercicio 6:
#a
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
if num1>num2:
    print("El numero mayor es el ",num1,"(primero)")
else:
    if num2>num1:
        print("El numero mayor es el ",num2,"(segundo)")
    else:
        print("Los valores ingresados son iguales")
#############################################################
#b
if num1<num2:
    print("El numero menor es el ",num1,"(primero)")
else:
    if num2<num1:
        print("El numnero menor es el ",num2,"(segundo)")
    else:
        print("Los valores ingresados son iguales")
