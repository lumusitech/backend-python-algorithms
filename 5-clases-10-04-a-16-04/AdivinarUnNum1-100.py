import random

na=random.randint(1,100)
print(na)   #Para ver con qué número aleatorio estoy trabajando (es solo para el programador
            #y una vez que funciona lo elimino)
nu=int(input("Adivina el número de 1 a 100 en 5 intentos: "))
contador=1

while(nu!=na):
    if(nu>na and contador<=5):
        print("El número a adivinar es menor")
    else:
        print("El número a adivinar es mayor")
    nu=int(input("Adivina otro número de 1 a 100: "))
    contador=contador+1

if nu==na and contador<=5:
    print("Adivinaste en ", contador, "intentos")
else:
    print("Superaste los intentos disponibles, Perdiste!")

###############################################################