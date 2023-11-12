import random

aleatorio = random.choice(range(1, 11, 1))

print("Vamos a jugar !!:\n\n")

ganaste = False
max_intentos = 4
intentos = 1

##	 verifico que no gane y que no llegue a la cantidad
##	 maxima de intentos
while(not ganaste and intentos <= max_intentos):

##   print("ayuda el numero es ", aleatorio)
   numero = int(input("Ingrese su numero:" ))

   if(numero==aleatorio):
        ganaste = True
   else:
        intentos = intentos + 1
        print("Segui participando...\n\n\n")
        if (intentos == max_intentos):
            print("Pero ojo que te queda una sola chance!!\n\n")


if(ganaste):
    print("Adivinaste !! ")
    print("El numero era el: ", numero)
else:
	print("Alpiste!! Se acabaron los intentos!\n\n")
	print("El numero era el: ", aleatorio)