#Ejercicio 1 del PowerPoint Ciclos While: Division y comprobacion de divisor
a=int(input("ingrese un numero"))
b=int(input("ingrese un numero"))

while(b==0):
    b=int(input("ingrese un numero diferente a cero"))

print("Resultado: ",a/b)