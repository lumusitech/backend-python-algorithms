alcance=101
contDiv=0

for numeros in range(1,alcance):
    for divisores in range(1,numeros+1):
        if(numeros%divisores==0):
            contDiv+=1
    if(contDiv==2):
        print(numeros)
    contDiv=0

##

alcance=101
numeros=2

while(numeros<alcance):
    divisor=1
    contDiv=0
    while(divisor<=numeros):
        if(numeros%divisor==0):
            contDiv+=1
        divisor+=1
    if(contDiv==2):
        print(numeros)
    numeros+=1


#algortimo para demostrar que no todos los numeros son primos
numeros=2
alcance=100

while(numeros<alcance):
    esPrimo=True
    divisores=2
    while(numeros>divisores):
        if(numeros%divisores==0):
            esPrimo=False
        divisores+=1
    if(esPrimo):
        print(numeros)
    numeros+=1