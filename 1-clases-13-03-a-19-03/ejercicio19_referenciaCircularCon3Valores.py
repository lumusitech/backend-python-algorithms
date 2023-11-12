#Ejercicio 19: Referencia circular con 3 valores

x=int(input("Ingrese el valor de \"x\": "))
y=int(input("Ingrese el valor de \"y\": "))
z=int(input("Ingrese el valor de \"z\": "))

aux=x

x=y
y=z
z=aux

print(
    " El valor de x es: ",x,"\n",
    "El valor de y es: ",y,"\n",
    "El valor de z es: ",z
    )