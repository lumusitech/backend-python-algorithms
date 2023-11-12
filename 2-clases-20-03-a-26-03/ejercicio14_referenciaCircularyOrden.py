#Ejercicio 14: Referencia circular y orden de mayor a menor
a=int(input("Ingrese un numero: "))
b=int(input("Ingrese otro numero: "))
if a<=b:
    aux=b;b=a;a=aux
    mayor=a;menor=b
else:
    mayor=a;menor=b

print(mayor,menor)