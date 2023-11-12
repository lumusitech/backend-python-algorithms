flag=True
divisor=2
n=int(input("Ingrese un numero"))
while n>divisor:
    if n%divisor==0:
        flag=False
    divisor=divisor+1 # o divisor+=1
if flag:
    print("El nuemro es primo")
else:
    print("El numero no es primo")
