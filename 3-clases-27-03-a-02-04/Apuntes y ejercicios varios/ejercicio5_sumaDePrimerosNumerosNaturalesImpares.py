#Ejercicio 5 del PowerPoint Ciclos While: serie de impares n numeros naturales

n=int(input("ingrese una cantidad de terminos para sumar"))
i=0
suma=0

while i<n:
    if i%2:
        suma+=i
    i+=1
print(suma)
