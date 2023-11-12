import math
n = int(input("Ingrese n�mero entero")) #cuanto mayor el numero de term, mejor la aprox
# suma de los primeros n t�rminos de la serie.
#alternada ejercicio 15 pr�ctica 3
suma = 1
for i in range(1, n+1):
    suma = suma + 1/((-1)**i * (2*i + 1))

print ("La suma hasta el t�rmino n es ", suma)
print ("pi/4 es ", math.pi/4)