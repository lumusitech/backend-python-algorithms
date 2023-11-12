#Ejercicio 13: El mayor de dos numeros
a=int(input("Ingrese el primer numero:"))
b=int(input("Ingrese le segundo numero: "))

if a>b:
    mayor=a
    menor=b
else:
    mayor=b
    menor=a
print("El mayor es: ",mayor)
print(mayor, menor)