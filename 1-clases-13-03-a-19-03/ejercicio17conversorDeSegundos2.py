#Ejercicio 17: Conversion de segundos exacto a dias, horas, minutos y segundos

segIn=int(input("Ingrese la cantidad de segundos a convertir: "))

minutos=60
horas=60*minutos   #3600
dias=horas*24      #86400

print(segIn," segundos son: ","\n")

print(
        segIn//dias," dias, ",
        (segIn%dias)//horas," hora/s, ",
        ((segIn%dias)%horas)//minutos," minuto/s y ",
        (((segIn%dias)%horas)%minutos)%minutos," segundo/s."
    )


