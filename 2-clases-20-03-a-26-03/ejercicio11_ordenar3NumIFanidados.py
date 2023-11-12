#Ejercicio 11: Ordenar de mayor a menor 3 numeros ingresados con if anidados

a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segudo numero: "))
c=int(input("Ingrese el tercer numero: "))

if a>b and a>c:
    print("El mayor de los tres es el primero ingresado: ",a)
else:
    if b>a and b>c:
        print("El mayor de los tres es el segundo ingresado: ",b)
    else:
        print("El mayor de los tres es el tercer numero ingresado: ",c)

################################################################################
#Solucion subida al campus virtual de ip
# asumimos que los tres son distintos

if a>b:
  if a>c:
    mayor=a
    if b>c:
        medio=b
        menor=c
    else:
        medio=b
        menor=c
  else:
    mayor=c
    medio=a
    menor=b
else:
    if b>c:
        mayor=b
        if a>c:
            medio=a
            menor=c
        else:
            medio=c
            menor=a
    else:
        mayor=c
        medio=b
        menor=a

print("El mas grande es ", mayor,
    "\nEl del medio es ", medio,
    "\nEl mas chico es", menor)
################################################################################
#Solucion dada en clases (Estudiar forma)
if a>=b and a>=c:
    print(a,end=" ")
    if b>=c:
        print(b,c)
    else:
        print(c,b)
else:
    if b>=a and b>=c:
        print(b,end=" ")
        if a>=c:
            print(a,c)
        else:
            print(c,a)
    else:
        print(c,end=" ")
        if a>=b:
            print(a,b)
        else:
            print(b,a)
################################################################################
#Solucion 2 dada en clases (Estudiar forma)
if a>=b and a>=c:
    mayor=a
    if b>=c:
        medio=b;menor=c
    else:
        medio=c;menor=b
else:
    if b>=a and b>=c:
        mayor=b
        if a>=c:
            medio=a;menor=c
        else:
            medio=c;menor=a
    else:
        mayor=c
        if a>=b:
            medio=a;menor=b
        else:
            medio=b;menor=a


print(mayor,medio,menor)