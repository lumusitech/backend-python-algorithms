numero=int(input())
cont=0

for numbers in range(0,101):

    for divisores in range(1,numbers+1):
        if numero%divisores==0:
            cont=cont+1
    if cont==2:
        print("El numero", numbers, " es primo")
##    else:
##        print("El numero", numbers, " NO es primo")
    cont=0 #con esto se resetea la cantidad de divisores, ya que si no me va a dar que todos son primos