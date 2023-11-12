n=int(input("Ingrese la cantidad de terminos"))
suma = 0
for i in range(1,n+1): # 1,2,3,4,5,...,n
    if(i%2==0): # i es par
        suma = suma - i/(i**(i+1))
    else: # i es impar
        suma = suma + i/(i**(i+1))
print(suma)

#otra manera
suma=0
signo = -1
for i in range(1,n+1): # 1,2,3,4,5,...,n
    signo = (-1)*signo
    suma = suma + signo*i/(i**(i+1))
print(suma)

#otra manera
suma=0
for i in range(1,n+1, 2): # 1,3,5,...,n
    suma = suma + i/(i**(i+1))

for i in range(2,n+1, 2): # 2,4,6,...,n
    suma = suma - i/(i**(i+1))
print(suma)


#otra manera
suma=0
for i in range(1,n+1,1): # 1,2,3,4,5,...,n
    suma = suma - ((-1)**i) * i/(i**(i+1))
print(suma)
