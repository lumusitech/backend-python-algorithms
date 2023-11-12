#Ejercicio de ejemplo 3
respuesta=int(input("¿En qué número entero del 1 al 10 estoy pensando?"))

if respuesta==7:
    print("Adivinaste")
else:
    if respuesta<7:
        print("Te quedaste corto")
    else:
        print("Te pasaste")