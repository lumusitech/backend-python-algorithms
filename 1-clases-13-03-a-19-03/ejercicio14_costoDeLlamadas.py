#Ejercicio 14: Calculo para el costo total de llamadas

costo=3
segundo=0.25
cantidad=int(input("Ingrese la cantidad de llamadas efectuadas: "))
tiempo=int(input("Ingrese el tiempo total de comunicacion en minutos: "))

costoLlamadas=cantidad*costo
tiempoLlamadas=tiempo*segundo

print("Importe total: ",costoLlamadas+tiempoLlamadas)