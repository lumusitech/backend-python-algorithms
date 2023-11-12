#Ejercicio 17: Calcular x en funcion lineal

a=7
b=5

if a==0 and b==0:
    print("la solucion son todos los reales")
else:
    if a==0 and b!=0:
        print("No tiene solucion")
    else:
        print("La ecuacion tiene como solucion x: ", (-b)/a)


################################################################

print("Este programa calcula ax + b  = 0")

a = float(input("Ingrese el valor de a"))
b = float(input("Ingrese el valor de b"))

if(a==0 and b==0):
    print("todos los reales")
else:
    if(not a):
        print("no tiene solucion")
    else:
        print("x vale:",(-b)/a)