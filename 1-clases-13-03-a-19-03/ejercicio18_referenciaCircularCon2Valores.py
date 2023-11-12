#Ejercicio 18: Referencia circular

x=int(input("Ingrese el valor de \"x\": "))
y=int(input("Ingrese el valor de \"y\": "))

xI=x
x=y
y=xI

print("El valor de \"x\" es: ",x," y el valor de \"y\" es: ",y)