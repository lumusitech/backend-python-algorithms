#Ejercicio 15: Calculo de comision

basico=7000
comision=0.1
venta1=float(input("Ingrese el monto de su primer venta: "))
venta2=float(input("Ingrese el monto de su segunda venta: "))
venta3=float(input("Ingrese el monto de su tercera venta: "))

ventas=venta1+venta2+venta3

comisionTotal=ventas*comision

print("Su sueldo final es: ",basico+comisionTotal)