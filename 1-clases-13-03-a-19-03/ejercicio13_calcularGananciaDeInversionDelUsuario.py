#Ejercicio 13: Calcular ganancia de inversion

capital=float(input("Ingrese el capital a invertir: "))
meses=int(input("Ingrese la cantidad de meses: "))

ganancia=capital*(meses*6/100)

print("Total: ",capital+ganancia,"\n","Ganancia: ",ganancia)

