flag=True
divisor=2
alcance=100
numeros=2

while(numeros<alcance): #va desde 2(numeros) hasta 100 (alcance)
    #cuerpo externo: todo lo que esta en la primer tabulacion
    #se resetea:
    divisor=2
    flag=True

    while numeros>divisor:

        #cuerpo interno: todo lo que esta en la segunda tabulacion
        if numeros%divisor==0:
            flag=False
        divisor=divisor+1 # o divisor+=1

    if flag:
        print("El numero ",numeros," es primo")
    numeros+=1

