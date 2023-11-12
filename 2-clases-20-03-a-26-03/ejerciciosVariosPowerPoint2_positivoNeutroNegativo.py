#Ejercicios varios del power point, positivo, neutro o negativo

a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))

if a>0 and b>0:
    print("El producto es positivo")
else:
    if a==0 or b==0:
        print("El numero 0 es neutro")
    else:
        print("El producto es negativo")