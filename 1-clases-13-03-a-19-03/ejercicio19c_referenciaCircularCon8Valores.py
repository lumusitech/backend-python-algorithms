#Ejercicio 19 c: Referencia circular con 8 valores

s=int(input("Ingrese el valor de \"s\": "))
t=int(input("Ingrese el valor de \"t\": "))
u=int(input("Ingrese el valor de \"u\": "))
v=int(input("Ingrese el valor de \"v\": "))
w=int(input("Ingrese el valor de \"w\": "))
x=int(input("Ingrese el valor de \"x\": "))
y=int(input("Ingrese el valor de \"y\": "))
z=int(input("Ingrese el valor de \"z\": "))

aux=s

s=t
t=u
u=v
v=w
w=x
x=y
y=z
z=aux


print(
    " El valor de s es: ",s,"\n",
    "El valor de t es: ",t,"\n",
    "El valor de u es: ",u,"\n",
    "El valor de v es: ",v,"\n",
    "El valor de w es: ",w,"\n",
    "El valor de x es: ",x,"\n",
    "El valor de y es: ",y,"\n",
    "El valor de z es: ",z
    )