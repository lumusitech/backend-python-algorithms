#Ejercicio 16: Conversor de segundos a minutos, horas y dias

segIn=int(input("Ingrese la cantidad de segundos a convertir: "))

#Minutos:
print(segIn," segundo/s ---> ",segIn//60," minuto/s")

#Horas
print(segIn," segundo/s ---> ",segIn//3600," hora/s")

#DÃ­as
print(segIn," segundo/s ---> ",segIn//86400," dias")