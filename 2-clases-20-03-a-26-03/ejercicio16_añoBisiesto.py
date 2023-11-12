#Ejercicio 16: Calculo de anio bisiesto

anio=1993
if anio%4==0:
    if anio%100==0:
        if anio%400==0:
            print("Es bisiesto")
else:
    print("No es bisiesto")

###############################################################


print("Este programa verifica si un anio es bisiesto")

anio = int(input("Ingrese un anio"))

if(anio % 4 == 0):
    if(anio % 100 == 0 and anio % 400 != 0):
        print("el anio", anio, "No es bisiesto")
    else:
        print("el anio", anio, "Es bisiesto")
else:
       print("el anio", anio, "No es bisiesto")


################################################################

year = int(input("Ingrese un anio"))

if(not(year%100==0 and year%400!=0) and year%4==0):
    print("bis")
else:
    print("no bis")