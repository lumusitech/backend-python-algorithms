



# 1/0! + 1/1! + 1/2! + ... + 1/n!

suma = 2
fact = 1
k = 2
while ( math.exp(1) - suma > 0.001): # numero e elevado a la 1
     fact = fact * k
     suma = suma + 1/fact
     k = k + 1
print(suma, math.exp(1), k-1)

