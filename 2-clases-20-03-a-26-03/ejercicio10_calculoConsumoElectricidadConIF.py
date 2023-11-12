#Ejercicio 10: Costo de consumo de electricidad

kw=int(input("Ingrese los KWs consumidos: "))
fijo=20
precioKW=0.5
impuestos=7.8
if kw>200:
    calculoKW=((kw-200)*precioKW)+fijo+impuestos
    print("Usted debe abonar: $",calculoKW)
else:
    calculoKW=fijo+impuestos
    print("Usted debe abonar: $",calculoKW)

#############################################################

print ("Este programa calcula el precio a pagar en la factura de LUZ")
kwinicial=float(input("Ingrese KW iniciales"))
kwfinal=float(input("Ingrese KW final"))
kw=kwfinal-kwinicial
tarifafija=20
impuestos=7.8

if(kw<200):
    monto=tarifafija+impuestos
else:
    monto=tarifafija+impuestos+0.5*(kw-200)

print("El precio a pagar es:",monto)