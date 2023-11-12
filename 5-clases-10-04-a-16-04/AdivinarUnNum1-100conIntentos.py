import random

na=random.randint(1,100)
print(na)
nu=int(input("Adivina el nÃºmero de a 100 en 3 intentos"))
contador=1 #variable de control
intentos=3 #cuando quiera dar ams intentos solo cambio eso

while nu!=na and contador <intentos:
    print("Ese no es el nÃºmero, vuelve a intentar")
    nu=int(input("Adivina el nÃºmero de 1 a 100"))
    contador=contador+1
if nu==na:
    print("Adivinazte en ",contador," intentos")
else:
    print("Game Over!")