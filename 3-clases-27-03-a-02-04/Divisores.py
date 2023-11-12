#Conocer los divisores de un numero

n=int(input("Ingresar numero"))
i=1
cd=0    #para saber la cantidad de divisores y ademas de acuerdo a esa cantidad evaluar
        #si es primo o no

while(i<=n):
    if n%i==0:  #tambien (Not n%i)
        print(i)
        cd=cd+1 #al sumarse solo cuando n%1==0 cuenta los divisores
    i=i+1
if cd==2:
    print("El numero de divisores de",n," es: ",cd,", es un numero primo")
else:
    print("El numero de divisores de",n," es: ",cd," no es un numero primo")

###############################################################################3

