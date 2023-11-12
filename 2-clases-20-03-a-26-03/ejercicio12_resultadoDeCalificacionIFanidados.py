#Ejercicio 12: if anidados, resultado de la calificacion

print("Referencia: ","\n", "1-3 Reprobado","\n","4-6 Debe rendir examen final","\n","7-10 Eximido")
nota1=int(input("Ingrese la primer nota: "))
nota2=int(input("Ingrese la segunda nota: "))
nota3=int(input("Ingrsese la tercer nota: "))

promedio=(nota1+nota2+nota3)//3

if promedio>=7:
    print("Su promedio es ",promedio," usted esta aprobado")
else:
    if promedio<7 and promedio>=4:
        print("Su promedio es ",promedio," usted debe rendir examen final")
    else:
        print("Su promedio es ",promedio," usted esta reprobado")