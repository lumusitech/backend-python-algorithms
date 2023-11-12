#Ejercicio 19: Referencia circular con 4 valores

x=int(input("Ingrese el valor de \"x\": "))
w=int(input("Ingrese el valor de \"w\": "))
y=int(input("Ingrese el valor de \"y\": "))
z=int(input("Ingrese el valor de \"z\": "))

aux=x

x=w
w=z
z=y
y=aux

print(
    " El valor de x es: ",x,"\n",
    "El valor de w es: ",w,"\n",
    "El valor de z es: ",z,"\n",
    "El valor de y es: ",y
    )